# Academic Calendar Web Scraper

## Description
This Python script is designed to automatically scrape academic calendar data from a university's online calendar. It uses **Selenium** in headless mode to navigate the page, extract key academic dates (such as semester start dates, holidays, and exam schedules), and print the results for easy reference.

The script is designed to be minimal and lightweight, using headless Chrome for efficiency.

## Features
- **Headless Web Scraping**: Runs the browser in headless mode, meaning no GUI is used, and it consumes fewer resources.
- **Error Handling**: Handles potential issues like timeouts and missing data gracefully.
- **Customizable Timeout**: You can adjust the waiting period for page elements to load, ensuring more reliable results.
- **Automatic Browser Management**: Uses `webdriver_manager` to automatically handle browser drivers.
  
## Prerequisites
Make sure you have the following installed:
- Python 3.x
- `pip` (Python package installer)

You will need to install the following libraries:
- `selenium`
- `webdriver_manager`
- `smtplib` (for email notifications, if required)

You can install the required libraries using `pip`:

```bash
pip install selenium webdriver_manager
```

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Modify the Script**:
   Edit the script to match the structure of the academic calendar page you want to scrape. You'll need to adjust element selectors if you're targeting a specific website.

3. **Run the Script**:
   After setting everything up, you can run the script using:
   ```bash
   python get_academic_calendar.py
   ```

   The script will automatically fetch the academic dates and display them in the terminal.

## Configuration
The script is designed to run with headless Chrome by default. If you want to run it with a visible browser, you can modify the `Options` in the script to disable headless mode:

```python
options.headless = False
```

## License
This project is open-source and available under the Apache 2.0 License.

## Issues
If you encounter any issues, feel free to open an issue on this repository.

---

## Example Output
After running the script, you should see output similar to the following (example dates and events):

```
- Select one of the following options: 

[1] - Fall 2024

[2] - Winter 2025

[3] - Spring 2025

[4] - Summer 2024

- Option: 1

 - MAY 1: Application for admission open

 - JUNE 24: View schedule of classes for fall 2024

 - JULY 22: Registration opens based on Priority Registration group

 - JULY 22: Group 1-A registration opens

 - JULY 23: Group 1-B registration opens

 - JULY 24: Group 2 registration opens

 - JULY 25: Group 3 registration opens

 - JULY 29: Group 4 registration opens

 - JULY 30: Group 5 registration opens ... Etc.
 
```

For more advanced usage or features, please contact: bizarr.development@gmail.com
