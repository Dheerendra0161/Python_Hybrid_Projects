import random
from selenium_dolphin import DolphinAPI
from selenium.webdriver.chrome.options import Options

# Initialize Dolphin API with your API key
api = DolphinAPI(
    api_key='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMjIxNGMzZmUzMGY4Y2EyMDhjMTcwZDRmODU1NGZkMDA4YTY4ZTdkMDA1ZjQxOTczY2QyMjZmNWYzNDMzMDEzZGQyOThhMjdhMTc2ODcwZjAiLCJpYXQiOjE3MTIxMzg5MTUuMjAxMTQyLCJuYmYiOjE3MTIxMzg5MTUuMjAxMTQ1LCJleHAiOjE3MTQ3MzA5MTUuMTkyNTUsInN1YiI6IjMyNTYzNDAiLCJzY29wZXMiOltdfQ.k3oJbtD3ClLz1FgGkPTxyrIcOHKR4EXX6EhvFMiFhfZjdYtpKKRxRHQUXcqeHt6jMazLvIchVCVXRFZBKbcLMYJMs62Ycjl9I9TILSID2iBnTcMmOcy4sCH27PMTDgt5RjbGndov7mnYM8IlJDlDqi0I_ytRwcWC_JDIxE6W8huLeGy9MoLi_G-Hgh_qcoz77r_b4zTFU1bX9Rj2llKFzgTv-On61Qe9Vico0QejN0_UiN_e2L6x8rQJB4kAqMUPjEzutGAqK2PMznHdPGSc_ZlOoe6EZnE7Uil8ZK9T7ydERK7vL_gh7KPjGjv6u5Zxji5DQRl2jaw9GoAA4s1i-DebPNBCJ9axubja63n7TOSkvnJpnBj37i6KHrmyIcMxbtA1V6ebe2w42mHkMm0G7RtvOLhzGfVKhUaoAzLD8dqRN9ZFhQuK6Cq9TOcLnuLdKmQkTDlcsjUBqC-clFRFMZynhy6aGmwaoLzX-mNrnNCdWMLnFJV6YTpQJ8eKcFhkXtLfbqYTzQ4dl0lYEiIZOpqpRYY0GY6HvRP874zYQrLxy_xU1X_pZIzkUJX7S_nwrVg4dFu8NpkOJs1TAqQmNJJE3gwzAeoLhKZzgpMAj99OZ73WyAVkTuNUDT50W2myKwBF8XP8JivurUh9Sf8oJK9nFoNqRiWj7ztfgklDu2I')
# Path to Dolphin Anty executable
dolphin_path = r"C:\Users\Dheerendra\Downloads\dolphin-anty-win-latest.exe"

# Generate a random fingerprint
fingerprint = []
while not fingerprint:
    fingerprint = api.generate_fingerprint(platform='windows', browser_version=f'{random.randint(114, 160)}')

# Create a new profile with the generated fingerprint
data = api.fingerprint_to_profile(name='Facebook', fingerprint=fingerprint)
profile_id = api.create_profile(data)['dheeruvish1608@gmail']

# Custom Chrome options
options = Options()
options.add_argument("--start-maximized")
options.binary_location = dolphin_path

# Try to get the driver
driver = api.get_driver(options=options, profile_id=profile_id)

if driver:
    print("Successfully got the driver!")
    driver.get('https://www.flipkart.com/')

    # Simulate human-like behavior
    # Example: Scraping data
    data_elements = driver.find_elements_by_xpath("//span[normalize-space()='Login']")

    for element in data_elements:
        print(element.text)

    # Close the browser and profile
    driver.quit()
    # api.close_profile(profile_id)
else:
    print("Failed to get driver from Dolphin API")
