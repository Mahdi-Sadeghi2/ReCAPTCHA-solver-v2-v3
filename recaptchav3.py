import time
from playwright.sync_api import sync_playwright
from playwright_recaptcha import recaptchav3
import sys


class RecaptchaV3Solver:
    def __init__(self):
        self.step = 1

    def log_step(self, message):
        print(f"🚀 Step {self.step}: {message}")
        self.step += 1
        time.sleep(1)

    def log_info(self, message):
        print(f"   ℹ️  {message}")
        time.sleep(0.3)

    def log_success(self, message):
        print(f"   ✅ {message}")
        time.sleep(0.3)

    def log_warning(self, message):
        print(f"   ⚠️  {message}")
        time.sleep(0.3)

    def log_error(self, message):
        print(f"   ❌ {message}")
        time.sleep(0.3)

    def log_debug(self, message):
        print(f"   🔍 {message}")
        time.sleep(0.2)


def solve_recaptcha_v3_demo():
    solver = RecaptchaV3Solver()

    solver.log_step("Initializing reCAPTCHA v3 Solver")
    solver.log_info("Starting Playwright Chrome browser instance...")

    try:
        with sync_playwright() as playwright:
            # Launch Chrome browser with visible UI
            solver.log_info("Launching Chrome browser (visible mode)...")
            browser = playwright.chromium.launch(
                headless=False,
                args=[
                    "--width=1400",
                    "--height=900",
                    "--start-maximized",
                    "--disable-notifications",
                    "--disable-popup-blocking"
                ]
            )
            solver.log_success("Chrome browser launched successfully!")

            # Create new page with Chrome context
            solver.log_info("Creating new browser page...")
            context = browser.new_context(
                viewport={"width": 1400, "height": 900},
                no_viewport=False
            )
            page = context.new_page()
            solver.log_success("Chrome page created!")

            # Initialize reCAPTCHA v3 solver
            solver.log_step("Initializing reCAPTCHA v3 solver")
            solver.log_info(
                "reCAPTCHA v3 is invisible and uses scoring system")
            solver.log_info("Score range: 0.0 (bot-like) to 1.0 (human-like)")

            with recaptchav3.SyncSolver(page) as recaptcha_solver:
                solver.log_success("reCAPTCHA v3 solver initialized!")

                # Navigate to target page
                solver.log_step("Navigating to AntCPT Score Detector")
                target_url = "https://antcpt.com/score_detector/"
                solver.log_info(f"Opening: {target_url}")
                solver.log_info("This page helps detect reCAPTCHA v3 scores")

                page.goto(target_url, wait_until="domcontentloaded")
                solver.log_success("Page loaded successfully!")

                # Wait for page to fully load
                solver.log_info("Waiting for page to complete loading...")
                page.wait_for_load_state("networkidle", timeout=15000)
                solver.log_success("Page fully loaded!")

                # Take screenshot before solving
                solver.log_step("Capturing initial page state")
                solver.log_info(
                    "Taking screenshot before reCAPTCHA solving...")
                page.screenshot(
                    path="before_recaptcha_v3_chrome.png", full_page=True)
                solver.log_success(
                    "Screenshot saved as 'before_recaptcha_v3_chrome.png'")

                # Analyze page content
                solver.log_info("Analyzing page structure...")
                title = page.title()
                solver.log_debug(f"Page title: {title}")

                # Check for reCAPTCHA elements
                recaptcha_elements = page.query_selector_all(
                    "[class*='recaptcha'], [id*='recaptcha']")
                solver.log_debug(
                    f"Found {len(recaptcha_elements)} reCAPTCHA-related elements")

                # Solve the reCAPTCHA v3
                solver.log_step("Starting reCAPTCHA v3 solving process")
                solver.log_info(
                    "reCAPTCHA v3 is invisible - no visual interaction needed")
                solver.log_info(
                    "Solving involves behavioral analysis and token generation...")

                try:
                    solver.log_info("Generating reCAPTCHA v3 token...")
                    token = recaptcha_solver.solve_recaptcha()

                    solver.log_success("reCAPTCHA v3 solved successfully!")
                    solver.log_success("Token generated!")

                    # Display token information
                    solver.log_step("Token Information")
                    token_preview = token[:60] + \
                        "..." if len(token) > 60 else token
                    solver.log_info(f"Token preview: {token_preview}")
                    solver.log_info(
                        f"Full token length: {len(token)} characters")
                    solver.log_info(
                        "This token can be used for form submissions")

                except Exception as e:
                    solver.log_error(f"Error solving reCAPTCHA v3: {str(e)}")
                    solver.log_info("Trying alternative approach...")
                    raise

                # Take screenshot after solving
                solver.log_step("Capturing final page state")
                solver.log_info("Taking screenshot after reCAPTCHA solving...")
                page.screenshot(
                    path="after_recaptcha_v3_chrome.png", full_page=True)
                solver.log_success(
                    "Screenshot saved as 'after_recaptcha_v3_chrome.png'")

                # Demonstrate token usage
                solver.log_step("Demonstrating Token Usage")
                solver.log_info(
                    "reCAPTCHA v3 tokens are typically used in hidden fields")
                solver.log_info(
                    "or submitted via API calls to the target website")

                # Try to find where to inject the token
                solver.log_info(
                    "Looking for potential token injection points...")

                # Common places where reCAPTCHA tokens might be expected
                potential_selectors = [
                    "input[name*='recaptcha']",
                    "textarea[name*='recaptcha']",
                    "[name*='g-recaptcha-response']",
                    "[id*='g-recaptcha-response']"
                ]

                found_elements = []
                for selector in potential_selectors:
                    elements = page.query_selector_all(selector)
                    found_elements.extend(elements)

                if found_elements:
                    solver.log_success(
                        f"Found {len(found_elements)} potential token injection points!")
                    for i, element in enumerate(found_elements):
                        element_id = element.get_attribute(
                            "id") or element.get_attribute("name") or f"element_{i}"
                        solver.log_debug(f"Injection point: {element_id}")
                else:
                    solver.log_info(
                        "No obvious injection points found - token may be used via JavaScript")

                # Show how to use the token programmatically
                solver.log_step("Programmatic Token Usage Example")
                solver.log_info("Here's how you might use the token:")
                solver.log_debug("""
# Example: Submitting token via form
import requests

data = {
    'username': 'your_username',
    'password': 'your_password',
    'g-recaptcha-response': token  # Your generated token
}

response = requests.post('https://example.com/login', data=data)
print(response.json())
                """)

                # Final output
                solver.log_step("Process Complete!")
                solver.log_success(
                    "🎉 reCAPTCHA v3 automation finished successfully!")
                solver.log_info(
                    "Check the generated screenshots for before/after comparison")
                solver.log_info(
                    "Your token is ready for use in form submissions")

                # Display the token for copying
                print("\n" + "="*80)
                print("📋 YOUR reCAPTCHA v3 TOKEN:")
                print("="*80)
                print(token)
                print("="*80)
                print("Copy this token for use in your applications!")
                print("="*80)

                # Keep browser open for inspection
                solver.log_info(
                    "Chrome browser will remain open for 45 seconds for inspection...")
                solver.log_info("Press Ctrl+C in terminal to close early")

                try:
                    for i in range(45, 0, -1):
                        sys.stdout.write(f"\r   ⏰ Closing in {i} seconds... ")
                        sys.stdout.flush()
                        time.sleep(1)
                    print()
                except KeyboardInterrupt:
                    solver.log_info("Early closure requested by user")

                # Close browser
                solver.log_info("Closing Chrome browser...")
                browser.close()
                solver.log_success("Chrome browser closed. Process complete!")

    except Exception as e:
        solver.log_error(f"Fatal error: {str(e)}")
        solver.log_info(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()

        # Try to close browser if it's still open
        try:
            browser.close()
            solver.log_info("Browser closed due to error")
        except:
            pass


if __name__ == "__main__":
    print("=" * 70)
    print("🤖 reCAPTCHA v3 SOLVER - CHROME EDITION")
    print("=" * 70)
    print("This script will:")
    print("1. Open Chrome browser with visible interface")
    print("2. Navigate to AntCPT Score Detector (reCAPTCHA v3 test page)")
    print("3. Solve invisible reCAPTCHA v3 challenge")
    print("4. Generate and display a valid reCAPTCHA v3 token")
    print("5. Show detailed step-by-step progress in terminal")
    print("6. Take before/after screenshots")
    print("=" * 70)
    print("Note: reCAPTCHA v3 is invisible and uses behavioral scoring")
    print("      (0.0 = bot-like, 1.0 = human-like)")
    print("=" * 70)

    input("Press Enter to start the reCAPTCHA v3 solving process...")
    print()

    solve_recaptcha_v3_demo()

    print()
    print("=" * 70)
    print("🏁 reCAPTCHA v3 process finished!")
    print("📸 Screenshots: before_recaptcha_v3_chrome.png, after_recaptcha_v3_chrome.png")
    print("📋 Token has been generated and displayed above")
    print("=" * 70)
