from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Config
screenshotDir = "Screenshots"
screenWidth = 1400
screenHeight = 1400
last_height = 0

# geckodriver_path = "/snap/bin/geckodriver"
# driver_service = webdriver.FirefoxService(executable_path=geckodriver_path)

def getPostScreenshots(filePrefix, script):
    print("Taking screenshots...")
    driver, wait = __setupDriver(script.url)
    script.titleSCFile = __takeScreenshot(filePrefix, driver, wait)
    for commentFrame in script.frames:
        print(commentFrame.commentId)
        commentFrame.screenShotFile = __takeScreenshot(filePrefix, driver, wait, f"[thingid='t1_{commentFrame.commentId}']")
    driver.quit()

def __takeScreenshot(filePrefix, driver, wait, handle="post-title-t3_"):
    global last_height
    method = By.ID if (handle == "post-title-t3_") else By.CSS_SELECTOR #By.CssSelector("[_celltype='celltype']");
    if (handle == "post-title-t3_"):
        handle = f"post-title-t3_{filePrefix}"
    print(f"Looking for element {handle}")
    search = wait.until(EC.presence_of_element_located((method, handle)))
    driver.execute_script("window.focus();")

    fileName = f"{screenshotDir}/{filePrefix}-{handle}.png"
    fp = open(fileName, "wb")
    fp.write(search.screenshot_as_png)
    fp.close()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height != last_height:
        last_height = new_height
    return fileName

def __setupDriver(url: str):
    options = webdriver.FirefoxOptions()
    options.headless = False
    options.enable_mobile = False
    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 10)

    driver.set_window_size(width=screenWidth, height=screenHeight)
    driver.get(url)

    last_height = driver.execute_script("return document.body.scrollHeight")

    return driver, wait