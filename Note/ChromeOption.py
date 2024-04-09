from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create ChromeOptions object
options = Options()

# Set window size
options.add_argument("--window-size=1920,1080")

# Enable headless mode
options.add_argument("--headless")

# Disable infobars
options.add_argument("--disable-infobars")

# Ignore certificate errors
options.add_argument("--ignore-certificate-errors")

# Set user-agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36")

# Set download directory
options.add_experimental_option("prefs", {
    "download.default_directory": "/path/to/download/directory",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": False
})

# Create WebDriver instance with options
driver = webdriver.Chrome(options=options)

# Use the driver for further automation
driver.get("https://www.example.com")
