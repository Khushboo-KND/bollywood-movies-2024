from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def initialize_driver(headless=False):
    """Initializes and returns a Selenium WebDriver instance.
    
    Args:
        headless (bool): If True, runs the browser in headless mode.
    
    Returns:
        selenium.webdriver.Chrome: Configured WebDriver instance.
    """
    options = Options()
    if headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')

    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.maximize_window()
        return driver
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        raise
