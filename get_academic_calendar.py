from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import smtplib
import time
import os

def get_academic_dates():

	options = Options()
	options.add_argument("--headless")  # Headless mode
	options.add_argument("--no-sandbox")  # Avoid permission issues
	options.add_argument("--disable-dev-shm-usage")  # Prevent memory issues
	options.add_argument("--disable-gpu")  # Disable GPU acceleration
	options.add_argument("--disable-extensions")  # Disable extensions
	options.add_argument("--remote-debugging-port=9222")  # Debugging support

	driver = webdriver.Chrome(options=options)
	open_web(driver)
	print_results(driver)

def open_web(driver):
	try:
		driver.get("https://www.deanza.edu/calendar/")
	except Exception as e:
		print(f"\n[!] There was a problem accessing the website: {e}\n")

def get_calendar_object(driver):

	try:
		return driver.find_element(By.CLASS_NAME, 'list-tab-accordian')

	except Exception as e:
		print(f"\n[!] There was a problem getting the calendar title: {e}\n")

def get_available_calendars(calendar_object, driver):

	try:

		all_schedules_data_list = calendar_object.find_elements(By.TAG_NAME, "li") 
		print("\n- Select one of the following options: ")
		
		for num, schedule in enumerate(all_schedules_data_list, start=0):
			print(f"\n[{num + 1}] - {schedule.find_element(By.TAG_NAME, 'h3').text}")

		return all_schedules_data_list

	except Exception as e:
		print(f"\n[!] There was a problem getting the available calendars: {e}\n")

def get_dates_and_events(all_schedules_data_list):

	try:

		user_input = all_schedules_data_list[int(input("\n- Option: ")) - 1]
		user_input.click()

		calendar_square = user_input.find_element(By.CLASS_NAME, 'dl-horizontal')

		dates_list = calendar_square.find_elements(By.TAG_NAME, 'dt')
		dates_information_list = calendar_square.find_elements(By.TAG_NAME, 'dd')

		for i, date in enumerate(dates_list, start=0):

			print(f"\n - {date.text}: {dates_information_list[i].text}")

	except Exception as e:
		print(f"\n[!] There's a problem accessing the calendar data: {e}\n")


def print_results(driver):
	get_dates_and_events(get_available_calendars(get_calendar_object(driver), driver))

get_academic_dates()