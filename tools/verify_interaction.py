import sys
import json
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

def run_tests():
    errors = []
    page_errors = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()
        
        page.on("pageerror", lambda exc: page_errors.append(str(exc)))
        
        print("[1] Navigating to http://localhost:8765/ ...")
        page.goto("http://localhost:8765/", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        
        # Check title
        title = page.title()
        print(f"    Page title: {title}")
        assert "Code&Colors" in title, f"Unexpected title: {title}"
        
        # Check initial UI mode: should be light
        ui_mode = page.evaluate("document.body.getAttribute('data-ui')")
        print(f"    Initial data-ui: {ui_mode}")
        assert ui_mode == "light", f"Expected light mode, got {ui_mode}"
        
        # Check initial mode: easy (body.classList.contains('easy') or #uimode [data-m="easy"].on)
        is_easy = page.evaluate("document.body.classList.contains('easy')")
        print(f"    Initial body.easy class: {is_easy}")
        assert is_easy, f"Expected body to have 'easy' class, got {is_easy}"
        
        # Check #vtl is hidden
        vtl_display = page.evaluate("window.getComputedStyle(document.getElementById('vtl')).display")
        print(f"    #vtl display: {vtl_display}")
        assert vtl_display == "none", f"Expected #vtl display: none, got {vtl_display}"
        
        # Check stage and canvas
        canvas_dims = page.evaluate("""
            () => {
                const c = document.getElementById('stage');
                return { width: c.width, height: c.height, clientWidth: c.clientWidth, clientHeight: c.clientHeight };
            }
        """)
        print(f"    Canvas dimensions: {canvas_dims}")
        assert canvas_dims['width'] > 0 and canvas_dims['height'] > 0, "Canvas dimensions are 0"
        
        # Test 48-styles drawer
        print("[2] Testing Easy Mode 48-styles drawer...")
        drawer_hidden = page.evaluate("document.getElementById('easystylesdrawer').hasAttribute('hidden')")
        assert drawer_hidden, "Drawer should be initially hidden"
        
        # Click toggle
        page.click("#etogglestyles")
        page.wait_for_timeout(300)
        drawer_hidden = page.evaluate("document.getElementById('easystylesdrawer').hasAttribute('hidden')")
        assert not drawer_hidden, "Drawer should now be visible"
        
        # Filter by paint
        page.click("#easystyletabs button[data-tab='paint']")
        page.wait_for_timeout(200)
        oil_visible = page.evaluate("""
            () => {
                const el = document.querySelector('.easy-style-card[data-val=\"oil\"]');
                return el && !el.hidden && window.getComputedStyle(el).display !== 'none';
            }
        """)
        pencil_hidden = page.evaluate("""
            () => {
                const el = document.querySelector('.easy-style-card[data-val=\"pencil\"]');
                return el && (el.hidden || window.getComputedStyle(el).display === 'none');
            }
        """)
        assert oil_visible, "Oil chip should be visible under paint"
        assert pencil_hidden, "Pencil chip should be hidden under paint"
        
        # Select oil
        page.click(".easy-style-card[data-val='oil']")
        page.wait_for_timeout(500)
        is_oil_active = page.evaluate("""
            () => {
                const el = document.querySelector('.easy-style-card[data-val=\"oil\"]');
                return el && el.classList.contains('on');
            }
        """)
        assert is_oil_active, "Oil card should have 'on' class after selection"
        print("    Successfully selected 'oil' style from 48-styles drawer!")

        # Close drawer via close button
        page.click("#closeeasystyles")
        page.wait_for_timeout(300)
        drawer_hidden_after = page.evaluate("document.getElementById('easystylesdrawer').hasAttribute('hidden')")
        assert drawer_hidden_after, "Drawer should close when close button is clicked"
        print("    Drawer cleanly closed via close button.")
        
        # Test Demo button
        print("[3] Testing Demo button...")
        page.click("#edemo")
        page.wait_for_timeout(1000)
        
        # Test Full Console mode toggle
        print("[4] Testing Mode switch to Full Console...")
        page.click("button[data-m='console']")
        page.wait_for_timeout(500)
        is_easy_console = page.evaluate("document.body.classList.contains('easy')")
        assert not is_easy_console, "Expected body to NOT have 'easy' class in Console mode"
        
        console_col_display = page.evaluate("window.getComputedStyle(document.querySelector('aside.col:not(#easy)')).display")
        assert console_col_display != "none", f"Expected console col visible, got {console_col_display}"
        print("    Full Console active, console column controls visible.")
        
        # Test Theme Toggle
        print("[5] Testing Theme toggle...")
        page.click("#uitheme")
        page.wait_for_timeout(300)
        dark_ui = page.evaluate("document.body.getAttribute('data-ui')")
        assert dark_ui == "dark", f"Expected dark, got {dark_ui}"
        print("    Toggled to dark UI.")
        
        page.click("#uitheme")
        page.wait_for_timeout(300)
        light_ui = page.evaluate("document.body.getAttribute('data-ui')")
        assert light_ui == "light", f"Expected light, got {light_ui}"
        print("    Toggled back to light UI.")
        
        # Test Transport: Pause & Restart
        print("[6] Testing Transport controls...")
        play_btn = page.evaluate("""
            () => {
                const b = document.getElementById('play');
                return { disabled: b.disabled, text: b.textContent.trim() };
            }
        """)
        print(f"    Play/Pause button: disabled={play_btn['disabled']}, text='{play_btn['text']}'")
        if not play_btn['disabled']:
            page.click("#play")
            page.wait_for_timeout(300)
            t_after = page.evaluate("document.getElementById('play').textContent.trim()")
            print(f"    Toggled play button: '{play_btn['text']}' -> '{t_after}'")
            page.click("#play") # resume
        
        restart_disabled = page.evaluate("document.getElementById('restart').disabled")
        print(f"    Restart button: disabled={restart_disabled}")
        if not restart_disabled:
            page.click("#restart")
            page.wait_for_timeout(300)
            print("    Restart triggered cleanly.")
        
        # Switch back to Easy mode
        print("[7] Testing switch back to Easy Mode...")
        page.click("button[data-m='easy']")
        page.wait_for_timeout(500)
        back_easy = page.evaluate("document.body.classList.contains('easy')")
        assert back_easy, "Expected body to have 'easy' class after returning to Easy mode"
        print("    Returned to Easy Mode.")
        
        # Check page errors
        print(f"[8] Checking uncaught JS errors: {len(page_errors)} found")
        if page_errors:
            for err in page_errors:
                print(f"    JS Error: {err}")
            raise AssertionError(f"Encountered {len(page_errors)} JS page errors!")
        
        print("ALL INTERACTION CHECKS PASSED WITH 0 ERRORS!")
        browser.close()

if __name__ == "__main__":
    run_tests()
