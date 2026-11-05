import os
import sys
import json
import time
from playwright.sync_api import sync_playwright

def run_capture(target_subfolder='after'):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(root_dir, '.taste-skill', target_subfolder)
    os.makedirs(output_dir, exist_ok=True)

    console_messages = []
    page_errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # 1. Desktop Audit (1440x900)
        context = browser.new_context(viewport={'width': 1440, 'height': 900})
        page = context.new_page()
        page.on('console', lambda msg: console_messages.append({'type': msg.type, 'text': msg.text}))
        page.on('pageerror', lambda err: page_errors.append(str(err)))

        t0 = time.time()
        page.goto('http://localhost:8765/', wait_until='networkidle')
        initial_load_time = (time.time() - t0) * 1000
        page.wait_for_timeout(2000)

        perf_metrics = page.evaluate("""() => {
            const nav = performance.getEntriesByType('navigation')[0];
            const paint = performance.getEntriesByType('paint');
            let fcp = 0;
            for (const p of paint) {
                if (p.name === 'first-contentful-paint') fcp = p.startTime;
            }
            return {
                domContentLoaded: nav ? nav.domContentLoadedEventEnd - nav.startTime : 0,
                load: nav ? nav.loadEventEnd - nav.startTime : 0,
                fcp: fcp,
                transferSize: nav ? nav.transferSize : 0
            };
        }""")

        lcp_cls = page.evaluate("""() => {
            return new Promise((resolve) => {
                let lcp = 0;
                let cls = 0;
                try {
                    const lcpObserver = new PerformanceObserver((entryList) => {
                        const entries = entryList.getEntries();
                        const lastEntry = entries[entries.length - 1];
                        lcp = lastEntry.startTime;
                    });
                    lcpObserver.observe({ type: 'largest-contentful-paint', buffered: true });

                    const clsObserver = new PerformanceObserver((entryList) => {
                        for (const entry of entryList.getEntries()) {
                            if (!entry.hadRecentInput) {
                                cls += entry.value;
                            }
                        }
                    });
                    clsObserver.observe({ type: 'layout-shift', buffered: true });
                } catch(e) {}

                setTimeout(() => {
                    resolve({ lcp, cls });
                }, 1000);
            });
        }""")

        page.screenshot(path=os.path.join(output_dir, '01_desktop_fullpage.png'), full_page=True)
        page.screenshot(path=os.path.join(output_dir, '02_desktop_viewport.png'))

        stagewrap = page.query_selector('#stagewrap')
        if stagewrap:
            stagewrap.screenshot(path=os.path.join(output_dir, '03_creative_workspace.png'))

        page.screenshot(path=os.path.join(output_dir, '04_header_controls.png'))

        # Full console mode
        console_btn = page.query_selector('#uimode button[data-m="console"]')
        if console_btn:
            console_btn.click()
            page.wait_for_timeout(1000)
            page.screenshot(path=os.path.join(output_dir, '09_full_console_desktop.png'), full_page=True)
            page.screenshot(path=os.path.join(output_dir, '10_full_console_viewport.png'))

        # Light mode
        theme_btn = page.query_selector('#uitheme')
        if theme_btn:
            theme_btn.click()
            page.wait_for_timeout(500)
            page.screenshot(path=os.path.join(output_dir, '11_light_mode_console.png'))

            easy_btn = page.query_selector('#uimode button[data-m="easy"]')
            if easy_btn:
                easy_btn.click()
                page.wait_for_timeout(500)
                page.screenshot(path=os.path.join(output_dir, '12_light_mode_easy.png'))

        context.close()

        # 2. Tablet Viewport (820x1180)
        context_tab = browser.new_context(viewport={'width': 820, 'height': 1180})
        page_tab = context_tab.new_page()
        page_tab.goto('http://localhost:8765/', wait_until='networkidle')
        page_tab.wait_for_timeout(1500)
        page_tab.screenshot(path=os.path.join(output_dir, '06_tablet_viewport.png'))
        context_tab.close()

        # 3. Mobile Viewport (390x844)
        context_mob = browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True, has_touch=True)
        page_mob = context_mob.new_page()
        page_mob.goto('http://localhost:8765/', wait_until='networkidle')
        page_mob.wait_for_timeout(1500)
        page_mob.screenshot(path=os.path.join(output_dir, '07_mobile_viewport.png'))
        page_mob.screenshot(path=os.path.join(output_dir, '08_mobile_fullpage.png'), full_page=True)
        context_mob.close()

        browser.close()

        errors = [m['text'] for m in console_messages if m['type'] == 'error'] + page_errors
        warnings = [m['text'] for m in console_messages if m['type'] == 'warning']

        audit_data = {
            'initial_load_ms': round(initial_load_time, 2),
            'domContentLoaded_ms': round(perf_metrics['domContentLoaded'], 2),
            'load_ms': round(perf_metrics['load'], 2),
            'fcp_ms': round(perf_metrics['fcp'], 2),
            'lcp_ms': round(lcp_cls['lcp'], 2),
            'cls': round(lcp_cls['cls'], 4),
            'error_count': len(errors),
            'warning_count': len(warnings),
            'errors': errors,
            'warnings': warnings
        }

        with open(os.path.join(output_dir, 'metrics.json'), 'w', encoding='utf-8') as mf:
            json.dump(audit_data, mf, indent=2)

        print(f"Audit {target_subfolder} finished: {json.dumps(audit_data, indent=2)}")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'after'
    run_capture(target)
