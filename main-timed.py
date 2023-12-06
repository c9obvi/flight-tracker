from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import json
import subprocess
import platform

# Start the timer
start_time = time.time()

# URL of the website || visit their site, enter call sign, grab url 
# I will build a GUI to enter the call sign and then grab the url

# url = "https://globe.adsbexchange.com/?icao=86d5be"
url = "https://globe.adsbexchange.com/?icao=a10343"

# Setup Selenium WebDriver
options = Options()
options.headless = True  # Run in headless mode
driver = webdriver.Chrome(options=options)

# Function to scrape data
def scrape_plane_info(url):
    driver.get(url)
    time.sleep(7)  # Wait for the page to load

    # Using BeautifulSoup to parse the page source
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Dictionary to hold the scraped data
    plane_info = {}

    # Extracting information
    plane_info['Groundspeed'] = soup.find(id='selected_speed1').get_text(strip=True) if soup.find(id='selected_speed1') else 'n/a'
    plane_info['Baro. Altitude'] = soup.find(id='selected_altitude1').get_text(strip=True) if soup.find(id='selected_altitude1') else 'n/a'
    plane_info['WGS84 Altitude'] = soup.find(id='selected_altitude_geom1').get_text(strip=True) if soup.find(id='selected_altitude_geom1') else 'n/a'
    plane_info['Vert. Rate'] = soup.find(id='selected_vert_rate').get_text(strip=True) if soup.find(id='selected_vert_rate') else 'n/a'
    plane_info['Track'] = soup.find(id='selected_track1').get_text(strip=True) if soup.find(id='selected_track1') else 'n/a'
    plane_info['Position'] = soup.find(id='selected_position').get_text(strip=True) if soup.find(id='selected_position') else 'n/a'
    plane_info['Distance'] = soup.find(id='selected_sitedist2').get_text(strip=True) if soup.find(id='selected_sitedist2') else 'n/a'
    plane_info['Source'] = soup.find(id='selected_source').get_text(strip=True) if soup.find(id='selected_source') else 'n/a'
    plane_info['RSSI'] = soup.find(id='selected_rssi1').get_text(strip=True) if soup.find(id='selected_rssi1') else 'n/a'
    plane_info['Message Rate'] = soup.find(id='selected_message_rate').get_text(strip=True) if soup.find(id='selected_message_rate') else 'n/a'
    plane_info['Last Position'] = soup.find(id='selected_seen_pos').get_text(strip=True) if soup.find(id='selected_seen_pos') else 'n/a'
    plane_info['Last Seen'] = soup.find(id='selected_seen').get_text(strip=True) if soup.find(id='selected_seen') else 'n/a'
    # ... Continue for other fields as needed

    return plane_info

# Scrape data from the URL
plane_info = scrape_plane_info(url)

# Calculate elapsed time and time of completion
elapsed_time = time.time() - start_time
time_of_completion = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# Add elapsed time and time of completion to the data
plane_info['Elapsed Time'] = f"{elapsed_time:.2f} seconds"
plane_info['Time of Completion'] = time_of_completion

# Convert to JSON
json_data = json.dumps(plane_info, indent=4)

# Close the driver
driver.quit()

# Print the JSON data
print('\n' + json_data)
print('Flight information has been saved to plane_data-main.json')

# Save the data to a file
file_name = 'plane_data-timed.json'
with open(file_name, 'w') as file:
    json.dump(plane_info, file, indent=4)

# Open the saved file in a browser
if platform.system() == 'Darwin':  # macOS
    subprocess.run(['open', '-a', 'Google Chrome', file_name])
elif platform.system() == 'Windows':  # Windows
    path_to_chrome = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    subprocess.run([path_to_chrome, file_name])
elif platform.system() == 'Linux':  # Linux
    subprocess.run(['google-chrome', file_name])
else:
    print('Platform not supported for browser opening')
