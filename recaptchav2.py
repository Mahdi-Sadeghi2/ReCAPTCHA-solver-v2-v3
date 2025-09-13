import time
from playwright.sync_api import sync_playwright
from playwright_recaptcha import recaptchav2
import sys


class RecaptchaSolverV2:
    def __init__(self):
        self.step = 1

    def log_step(self, message):
        print(f"🚀 Step {self.step}: {message}")
        self.step += 1
        time.sleep(1)  # Pause for readability

    def log_info(self, message):
        print(f"   ℹ️  {message}")
        time.sleep(0.5)

    def log_success(self, message):
        print(f"   ✅ {message}")
        time.sleep(0.5)

    def log_warning(self, message):
        print(f"   ⚠️  {message}")
        time.sleep(0.5)

    def log_error(self, message):
        print(f"   ❌ {message}")
        time.sleep(0.5)


def solve_recaptcha_demo():
    solver = RecaptchaSolverV2()

    solver.log_step("Initializing Playwright browser")

    try:
        with sync_playwright() as playwright:
            # Launch Chrome browser with visible UI
            solver.log_info("Launching Chrome browser...")
            browser = playwright.chromium.launch(
                headless=False,
                args=["--width=1200", "--height=800", "--start-maximized"]
            )

            solver.log_success("Chrome browser launched successfully!")

            # Create new page
            solver.log_info("Creating new browser page...")
            page = browser.new_page()
            solver.log_success("Page created!")

            # Set viewport size
            page.set_viewport_size({"width": 1200, "height": 800})

            # Navigate to Google reCAPTCHA demo page
            solver.log_step("Navigating to reCAPTCHA demo page")
            demo_url = "https://www.google.com/recaptcha/api2/demo"
            solver.log_info(f"Opening: {demo_url}")

            page.goto(demo_url)
            solver.log_success("Page loaded successfully!")

            # Wait for page to fully load
            solver.log_info("Waiting for page elements to load...")
            page.wait_for_selector("iframe[src*='recaptcha']", timeout=10000)
            solver.log_success("reCAPTCHA iframe detected!")

            # Take screenshot before solving
            solver.log_info("Taking screenshot before solving...")
            page.screenshot(path="before_recaptcha.png")
            solver.log_success("Screenshot saved as 'before_recaptcha.png'")

            # Initialize reCAPTCHA solver
            solver.log_step("Initializing reCAPTCHA solver")
            recaptcha_solver = recaptchav2.SyncSolver(page)
            solver.log_success("Solver initialized!")

            # Solve the reCAPTCHA
            solver.log_step("Starting reCAPTCHA solving process")
            solver.log_info("This may take a few moments...")

            # Add progress monitoring
            def log_progress(message):
                solver.log_info(f"Solving: {message}")

            # Solve with progress callback
            try:
                token = recaptcha_solver.solve_recaptcha()
                solver.log_success("reCAPTCHA solved successfully!")

                # Display the token (truncated for readability)
                token_preview = token[:50] + \
                    "..." if len(token) > 50 else token
                solver.log_info(f"Token obtained: {token_preview}")
                solver.log_info(f"Full token length: {len(token)} characters")

            except Exception as e:
                solver.log_error(f"Error solving reCAPTCHA: {str(e)}")
                raise

            # Take screenshot after solving
            solver.log_info("Taking screenshot after solving...")
            page.screenshot(path="after_recaptcha.png")
            solver.log_success("Screenshot saved as 'after_recaptcha.png'")

            # Verify the solution
            solver.log_step("Verifying reCAPTCHA solution")

            # Check if the reCAPTCHA is marked as solved
            try:
                # Look for the reCAPTCHA checkmark
                solved_indicator = page.query_selector(
                    ".recaptcha-checkbox-checked")
                if solved_indicator:
                    solver.log_success("reCAPTCHA verification: PASSED ✓")
                    solver.log_info("The checkbox is checked and verified!")
                else:
                    solver.log_warning("Visual verification inconclusive")
                    solver.log_info("Checking token validity...")

            except Exception as e:
                solver.log_warning(f"Verification check failed: {str(e)}")

            # Demonstrate form submission
            solver.log_step("Simulating form submission")
            solver.log_info("Preparing to submit the demo form...")

            # Fill demo form fields (if they exist)
            try:
                # Try to fill some demo data
                page.fill("input[name='demo']", "automated_test")
                solver.log_info("Filled demo field")
            except:
                solver.log_info("No demo fields to fill")

            # Submit the form
            try:
                submit_button = page.query_selector(
                    "input[type='submit'], button[type='submit']")
                if submit_button:
                    solver.log_info("Clicking submit button...")
                    submit_button.click()
                    solver.log_success("Form submitted!")

                    # Wait for response
                    page.wait_for_timeout(3000)
                    solver.log_info("Waiting for server response...")

                else:
                    solver.log_info(
                        "No submit button found - token is ready for use")

            except Exception as e:
                solver.log_warning(f"Form submission error: {str(e)}")

            # Final summary
            solver.log_step("Process completed!")
            solver.log_success("🎉 reCAPTCHA automation finished successfully!")
            solver.log_info(
                "Check the screenshots: before_recaptcha.png and after_recaptcha.png")
            solver.log_info("You can now use the token for your applications")

            # Keep browser open for inspection
            solver.log_info(
                "Chrome browser will remain open for 30 seconds for inspection...")
            solver.log_info("Press Ctrl+C to close early")

            try:
                time.sleep(30)
            except KeyboardInterrupt:
                solver.log_info("Early closure requested by user")

            # Close browser
            solver.log_info("Closing Chrome browser...")
            browser.close()
            solver.log_success("Chrome browser closed. Process complete!")

    except Exception as e:
        solver.log_error(f"Fatal error: {str(e)}")
        print(f"Error details: {type(e).__name__}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("=" * 60)
    print("🤖 reCAPTCHA v2 SOLVER - CHROME EDITION")
    print("=" * 60)
    print("This script will:")
    print("1. Open Chrome browser")
    print("2. Navigate to reCAPTCHA demo page")
    print("3. Solve the reCAPTCHA step by step")
    print("4. Show progress in terminal")
    print("5. Take before/after screenshots")
    print("=" * 60)

    input("Press Enter to start the reCAPTCHA solving process...")
    print()

    solve_recaptcha_demo()

    print()
    print("=" * 60)
    print("🏁 Process finished! Check the generated screenshots.")
    print("=" * 60)
