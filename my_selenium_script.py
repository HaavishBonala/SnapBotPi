from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

# Set Chrome options
options = Options()
options.add_argument("--use-fake-ui-for-media-stream")  # Bypass permission dialog
options.add_argument("--use-fake-device-for-media-stream")  # Use a fake device for media input

# Initialize driver
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://web.snapchat.com")

# Wait for the page to load
sleep(15)

# Function to handle waiting and element interaction with logging
def wait_and_click(by, locator, description="", timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))
        element.click()
        if description:
            print(f"Clicked: {description}")
    except Exception as e:
        print(f"An error occurred with {description}: {e}")

def wait_and_send_keys(by, locator, keys, description="", timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))
        element.send_keys(keys)
        if description:
            print(f"Entered text into: {description}")
    except Exception as e:
        print(f"An error occurred with {description}: {e}")

# Locate and enter email address
wait_and_send_keys(By.ID, "ai_input", "haavish911@gmail.com", description="Email input")

# Click the login button
wait_and_click(By.XPATH, "//button[contains(text(), 'Log in')]", description="Login button")

# Wait for accept cookies and then click button
sleep(10)
wait_and_click(By.XPATH, "//span[@class='css-1wv434i' and text()='Accept All']", description="Password input")

# Wait for the password input and enter password
wait_and_send_keys(By.ID, "password", "Haavish#123", description="Password input")

# Click "Next" button
wait_and_click(By.CSS_SELECTOR, 'button[data-testid="password-submit-button"]', description="Next button")

# Wait for page elements to load
sleep(20)

# Get screen width and move cursor to far right
screen_width = driver.execute_script("return window.innerWidth;")
x_position = screen_width * 0.95  # Position cursor at 95% of screen width
ActionChains(driver).move_by_offset(x_position, 0).click().perform()
sleep(15)

# Click the specific button
wait_and_click(By.CSS_SELECTOR, "button.FBYjn.gK0xL.W5dIq", description="Target button")

# Main loop
while True:
    # Step 1: Capture picture
    try:
        picture_button = driver.find_element(By.XPATH, "/html/body/main/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/button[1]")
        picture_button.click()
        print("Captured picture.")
    except Exception as e:
        print(f"Error capturing picture: {e}")

    # Step 2: Click the send button
    wait_and_click(By.CSS_SELECTOR, "button.YatIx.fGS78.eKaL7.Bnaur", description="Send button")

    # Step 3: Select bot accounts (list you bot accounts in the below list)
    bot_names = ['','','']
    for bot_name in bot_names:
        try:
            bot_button = driver.find_element(By.XPATH, f"//div[contains(@class, 'RBx9s') and contains(text(), '{bot_name}')]")
            bot_button.click()
            print(f"Selected bot account: {bot_name}")
        except Exception as e:
            print(f"Error selecting bot account {bot_name}: {e}")

    # Step 4: Click the final send button
    wait_and_click(By.CSS_SELECTOR, "button.TYX6O.eKaL7.Bnaur", description="Final send button")
    print("Message sent.")
