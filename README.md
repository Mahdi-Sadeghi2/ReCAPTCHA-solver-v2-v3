# reCAPTCHA Solver Automation

A Python-based automation tool that solves both reCAPTCHA v2 and reCAPTCHA v3 challenges using Playwright and the playwright-recaptcha library.

# Features

reCAPTCHA v2 Support: Solves traditional "I'm not a robot" checkbox challenges

reCAPTCHA v3 Support: Solves invisible reCAPTCHA challenges with token generation

Visual Feedback: Takes before/after screenshots for verification

Detailed Logging: Step-by-step progress reporting in the terminal

User-Friendly: Clear prompts and status messages throughout the process

# Requirements

Playwright

playwright-recaptcha library

Chrome browser (automatically installed by Playwright)

# Installation

Clone or download this repository

Install the required dependencies:

bash
pip install playwright playwright-recaptcha
Install Playwright browsers:

bash
playwright install chromium
Usage
reCAPTCHA v2 Solver
Run the reCAPTCHA v2 solver:

bash
python recaptchav2.py
This script will:

Open a visible Chrome browser

Navigate to the official reCAPTCHA demo page

Solve the reCAPTCHA challenge

Generate screenshots (before_recaptcha.png, after_recaptcha.png)

Display the obtained token

reCAPTCHA v3 Solver
Run the reCAPTCHA v3 solver:

bash
python recaptchav3.py
This script will:

Open a visible Chrome browser

Navigate to the AntCPT Score Detector page

Solve the invisible reCAPTCHA v3 challenge

Generate screenshots (before_recaptcha_v3_chrome.png, after_recaptcha_v3_chrome.png)

Display the generated token for use in your applications

# File Structure

text
recaptcha-solver/
├── recaptchav2.py # reCAPTCHA v2 solver implementation
├── recaptchav3.py # reCAPTCHA v3 solver implementation
├── before_recaptcha.png # Generated screenshot (v2)
├── after_recaptcha.png # Generated screenshot (v2)
├── before_recaptcha_v3_chrome.png # Generated screenshot (v3)
└── after_recaptcha_v3_chrome.png # Generated screenshot (v3)
How It Works
Initialization: Launches a Chrome browser instance with Playwright

Navigation: Loads the target page with reCAPTCHA challenge

Detection: Identifies and analyzes the reCAPTCHA widget

Solving: Uses the playwright-recaptcha library to solve the challenge

Verification: Checks if the solution was successful

Token Extraction: Retrieves the verification token for form submission

Documentation: Captures screenshots and provides detailed logs

# Output

Terminal output with step-by-step progress

Screenshots before and after solving the reCAPTCHA

Generated tokens for use in form submissions

# Notes

The browser remains open for inspection after completion

Press Ctrl+C to close the browser early if needed

reCAPTCHA v3 is invisible and uses a scoring system (0.0-1.0)

Tokens are typically valid for a short period (usually 2 minutes)

# Disclaimer

This tool is intended for educational and testing purposes only. Please use it responsibly and only on websites you own or have permission to test. Always comply with the terms of service of websites you interact with.

# Troubleshooting

If you encounter issues:

Ensure all dependencies are properly installed

Check your internet connection

Verify that the target websites are accessible

Make sure you're using a compatible Python version
