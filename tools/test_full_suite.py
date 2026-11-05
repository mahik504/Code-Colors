import sys
import os
import requests
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

def deep_verification():
    page_errors = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()
        page.on("pageerror", lambda exc: page_errors.append(str(exc)))
        
        print("[1] Verifying server response & local download links...")
        res = requests.get("http://localhost:8765/download/code-colors-local.zip")
        assert res.status_code == 200, f"Expected 200 for code-colors-local.zip, got {res.status_code}"
        print(f"    code-colors-local.zip accessible: {len(res.content)} bytes")
        
        print("[2] Navigating to studio...")
        page.goto("http://localhost:8765/", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        
        # Verify #getlocal href
        getlocal_href = page.evaluate("document.getElementById('getlocal').getAttribute('href')")
        print(f"    #getlocal href: {getlocal_href}")
        assert "code-colors-local.zip" in getlocal_href, f"Expected code-colors-local.zip in href, got {getlocal_href}"
        
        # Check initial easy mode layout & canvas
        stage_dims = page.evaluate("""() => {
            const s = document.getElementById('stage');
            return { w: s.width, h: s.height, cw: s.clientWidth, ch: s.clientHeight };
        }""")
        print(f"    Easy Mode Canvas dimensions: {stage_dims}")
        assert stage_dims['cw'] > 800 and stage_dims['ch'] > 400, "Canvas should be prominently sized in Easy mode"
        
        # Check Easy Mode 4-step sidebar visibility
        for step in range(1, 5):
            visible = page.evaluate(f"() => {{ const el = document.querySelectorAll('.estep')[{step-1}]; return el && el.getBoundingClientRect().height > 0; }}")
            assert visible, f"Easy Mode Step {step} should be visible"
        print("    All 4 Easy Mode steps are rendered and visible.")

        # Test 48 styles drawer tabs
        print("[3] Testing 48 styles drawer categorization...")
        page.click("#etogglestyles")
        page.wait_for_timeout(200)
        
        for tab, count in [('paint', 12), ('draw', 6), ('graphic', 12), ('craft', 6), ('material', 12)]:
            page.click(f"#easystyletabs button[data-tab='{tab}']")
            page.wait_for_timeout(150)
            visible_count = page.evaluate(f"""() => {{
                return Array.from(document.querySelectorAll('.easy-style-card')).filter(c => !c.hidden && window.getComputedStyle(c).display !== 'none').length;
            }}""")
            print(f"    Tab '{tab}': {visible_count} visible styles (expected {count})")
            assert visible_count == count, f"Expected {count} styles under tab {tab}, got {visible_count}"
        
        page.click("#closeeasystyles")
        page.wait_for_timeout(200)
        
        # Switch to Full Console
        print("[4] Switching to Full Console...")
        page.click("#uimode button[data-m='console']")
        page.wait_for_timeout(500)
        
        # Check that canvas is NOT crushed
        console_stage = page.evaluate("""() => {
            const s = document.getElementById('stage');
            return { w: s.width, h: s.height, cw: s.clientWidth, ch: s.clientHeight };
        }""")
        print(f"    Full Console Canvas dimensions: {console_stage}")
        assert console_stage['ch'] > 400, f"Full Console canvas should have height > 400px, got {console_stage['ch']}px"
        
        # Check Playlist Panel: horizontal strip
        playlist_dims = page.evaluate("""() => {
            const pl = document.getElementById('slots');
            return { display: window.getComputedStyle(pl).display, h: pl.clientHeight, w: pl.clientWidth };
        }""")
        print(f"    Playlist panel dimensions: {playlist_dims}")
        assert playlist_dims['h'] < 70, f"Playlist panel should be a compact horizontal strip (<70px), got {playlist_dims['h']}px"
        
        # Check that .sr successfully hides native elements
        sr_hidden = page.evaluate("""() => {
            const slotmode = document.getElementById('slotmode');
            const speed_range = document.getElementById('speed');
            return {
                slotmode_visible: window.getComputedStyle(slotmode).clip !== 'rect(0px, 0px, 0px, 0px)',
                slotmode_clip: window.getComputedStyle(slotmode).clip
            };
        }""")
        print(f"    Screen-reader hidden check: {sr_hidden}")
        assert not sr_hidden['slotmode_visible'], "slotmode select should be sr-clipped"

        # Check 5 View Modes
        print("[5] Testing 5 Display Modes...")
        for mode in ['studio', 'simple', 'painting', 'duo', 'editor']:
            page.click(f"#view button[data-display='{mode}']")
            page.wait_for_timeout(200)
            cur = page.evaluate("document.body.getAttribute('data-display')")
            assert cur == mode, f"Expected data-display={mode}, got {cur}"
        page.click("#view button[data-display='studio']")
        print("    All 5 Display modes switched successfully.")

        # Check Presets store & recall
        print("[6] Testing Presets store & reset...")
        page.click("#pstore")
        page.wait_for_timeout(100)
        page.click(".presets button[data-p='A']")
        page.wait_for_timeout(200)
        is_stored = page.evaluate("""() => {
            const b = document.querySelector(".presets button[data-p='A']");
            return b && b.classList.contains('full');
        }""")
        print(f"    Preset A stored indicator: {is_stored}")
        assert is_stored, "Preset A should have 'full' class after storing"

        # Check Mobile Viewport
        print("[7] Testing Mobile Ergonomics...")
        mob_ctx = browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True, has_touch=True)
        mob_page = mob_ctx.new_page()
        mob_page.on("pageerror", lambda exc: page_errors.append(f"Mobile: {exc}"))
        mob_page.goto("http://localhost:8765/", wait_until="domcontentloaded")
        mob_page.wait_for_timeout(1500)
        
        phone_visible = mob_page.evaluate("window.getComputedStyle(document.getElementById('phone')).display !== 'none'")
        assert phone_visible, "Mobile drawer #phone must be visible on mobile"
        
        # Test look chip click on mobile
        first_look = mob_page.evaluate("""() => {
            const btn = document.querySelector('#phlooks button');
            if (btn) { btn.click(); return btn.textContent; }
            return null;
        }""")
        mob_page.wait_for_timeout(300)
        print(f"    Clicked mobile look: '{first_look}'")
        assert first_look is not None, "Mobile looks chips should exist and be clickable"
        
        mob_ctx.close()
        browser.close()
        
        # Ensure 0 errors
        print(f"[8] Uncaught page errors: {len(page_errors)}")
        assert len(page_errors) == 0, f"Encountered page errors: {page_errors}"
        print("\nALL DEEP VERIFICATION CHECKS PASSED WITH 100% SUCCESS!")

if __name__ == '__main__':
    deep_verification()
