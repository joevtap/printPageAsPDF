from dotenv import load_dotenv
from selenium import webdriver
from setup import setup
import json
import os

# ========== SETUP ========== #

load_dotenv()

print('Do you need to setup enviroment variables? ')
print('1 - Yes')
print('Any other number - No')

option = int(input(">>> "))

if option == 1:
    setup()
else:
    pass

URL = str(input('URL (remember to use "http://" or "https://"): '))
downloads_path = os.getenv('DOWNLOADS_PATH')
driver_path = os.getenv('DRIVER_PATH')

chrome_options = webdriver.ChromeOptions()

settings = {
    'recentDestinations': [{
        'id': 'Save as PDF',
        'origin': 'local',
        'account': '',
    }],
    'selectedDestinationId': 'Save as PDF',
    'version': 2
}

prefs = {
    'plugins.plugins_list': [{
        'enabled': False, 'name': 'Chrome PDF Viewer'
    }],
    'download.default_directory': downloads_path,

    'profile.default_content_settings.popups': 0,
    'download.extensions_to_open': 'applications/pdf',
    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
    'savefile.default_directory': downloads_path
}

chrome_options.headless = False
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--kiosk-printing')
chrome_options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=chrome_options,
                          executable_path=driver_path)

# ========== EXECUTION ========== #

driver.get(URL)

driver.execute_script('window.print();')

driver.close()
