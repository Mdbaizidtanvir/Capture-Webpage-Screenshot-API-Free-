from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import base64
import os
from webdriver_manager.chrome import ChromeDriverManager

def get_webdriver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless (no UI)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920x1080")  # Set a large viewport

    # Create WebDriver instance
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def capture_webpage_as_base64(url):
    try:
        driver = get_webdriver()
        driver.get(url)

        # Take a full-page screenshot
        screenshot_path = "screenshot.png"
        driver.save_screenshot(screenshot_path)

        # Convert screenshot to Base64
        with open(screenshot_path, "rb") as img_file:
            base64_image = base64.b64encode(img_file.read()).decode('utf-8')

        # Clean up
        driver.quit()
        os.remove(screenshot_path)  # Remove temporary file

        return f"data:image/png;base64,{base64_image}"
    except Exception as e:
        return {"error": str(e)}
