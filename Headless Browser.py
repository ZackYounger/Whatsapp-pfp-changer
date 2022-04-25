from playwright.async_api import async_playwright
import asyncio

image =  "_image name_"

async def main():
    async with async_playwright() as p:
        print("Loading Whatsapp")
        browser = await p.chromium.launch_persistent_context(user_data_dir="cookies",headless=True,extra_http_headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'})
        page = await browser.new_page()
        url = "https://web.whatsapp.com/"
        await page.goto(url)
        await page.click("._3GlyB")
        print("Im in!")
        await page.click("._3yg5l")
        print("Starting Uploading Image")
        page.on("filechooser", lambda file_chooser: file_chooser.set_files(image))
        await page.click("[aria-label='Upload photo']")
        print("Finished Uploading")
        for i in range(5):
            await page.locator(".P6r3N", has=page.locator('[data-testid="minus"]')).click()
            await asyncio.sleep(.1)
        await page.click('[data-testid="checkmark-large"]')
        print("Verifying upload")
        while True:
            if await page.is_visible("text=Profile photo set"):
                break
            await asyncio.sleep(0.1)
        print("Done!")

asyncio.run(main())
