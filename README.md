# Plane Information Scraper

![](https://maeebnvejslkonktbeha.supabase.co/storage/v1/object/public/cdn/IMG_1239.webp)

## Overview
This tool is designed to scrape plane information from the website "ADS-B Exchange". It captures various details such as Groundspeed, Barometric Altitude, WGS84 Altitude, Vertical Rate, and more. The script is implemented in Python and uses Selenium for web scraping and BeautifulSoup for HTML parsing. Elapsed time of scrape is currently around 300 seconds. 

## Features
- Scrape plane information from ADS-B Exchange.
- Extract specific data like Groundspeed, Altitude, Track, Position, and more.
- Display elapsed time during scraping with a threading-based timer.
- Save scraped data in JSON format.

## Prerequisites
- Python 3.x
- Selenium
- BeautifulSoup4
- ChromeDriver (compatible with the installed Chrome version)

## Installation
1. Clone this repository or download the script.
2. Install the required Python packages:
   ```
   pip install selenium beautifulsoup4
   ```
3. Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/) and place it in a known directory.

## Usage
1. Open the script in a text editor and set the target URL in the `url` variable.
2. Run the script using Python:
   ```
   python main.py
   ```
3. Check the terminal for the elapsed time and the output directory for the generated JSON file named `plane_data.json`. (or plane_data-timed.json if you are using the elapsed time version)

## Output
The script saves the scraped data in a JSON file named `plane_data.json`. This file includes details like Groundspeed, Barometric Altitude, Track, etc., in a structured format.

## Automating 

> [!NOTE]
> `chmod +x` the `flight-tracker.sh` script before adding it to your crontab or other scheduling service of your choice. This script is for the elapsed time version so you can see how long this takes (in terminal)

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
- [0xBerto](https://x.com/0xberto)
