#!/usr/bin/python3

# This scraper is designed to return the Job Description and the Job Title of an indeed post
# However their cloudfare security solution blocked this attempt 
# Instead of tossing this script, I want to use it showcase my development and why I will be attempting
# to use Indeeds API next.


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
# #waiting for button to be clickable
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def scrape_indeed_job_description():
#     #Setup Chrome options
#     chrome_options = Options()
#     chrome_options.add_argument("--headless") # Esnure GUI is off
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")

#     # Set path to chromedriver as per your configuration
#     webdriver_service = Service(ChromeDriverManager().install())

#       #Choose Chrom Browser
#     driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

#     #wait
#     wait = WebDriverWait(driver,20)

  
#     driver.get("https://www.indeed.com")

#     # getting to the search bar and typing ajob and location
#     search_job = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="sugInpt"]')))
#     search_job.send_keys(Keys.CONTROL + "a")
#     search_job.send_keys("Cybersecurity")

#     search_location = wait.until(EC.presence_of_element_located((By.XPATH,' //*[@id="where"]')))
#     search_location.send_keys(Keys.CONTROL + "a") # This clears the location field, as it's pre-filled
#     search_location.send_keys("Bellevue, WA")

#     #clicking the "Find Jobs" button to start the search
#     search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="whatWhereFormId"]/div[3]/button')))
#     search_button.click()

#     # waiting for page to load, grab job and extract data

#     # delay to wait for JS to load jobs
#     #time.sleep(10)

#     # grab the page source
#     html = driver.page_source

#     # create a beautifulSoup object and specify parser
#     soup = BeautifulSoup(html,'html.parser')

#     #find job card

#     job_cards = soup.find_all('div', {'class':'cardOutline tapItem'})

#     #iterate over each job and grab title and description

#     for job_card in job_cards:
#         title_tag = job_card.find('h2',{'class':'jobTitle'})
#         if title_tag:
#             title = title_tag.find('span').get('title')
#             print(f"Job title:  {title}")

#         desc_tag = job_card.find('div',{"class":'job-snippet'})
#         if desc_tag:
#             description = desc_tag.get_text(strip=True)
#             print(f"Description: {description}\n")

#     # close the browser
#     driver.quit()

#     # Tells python to run the function we just declared

# scrape_indeed_job_description()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_indeed_job_description():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set path to chromedriver as per your configuration
    webdriver_service = Service(ChromeDriverManager().install())

    # Choose Chrome Browser
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    driver.get("https://www.indeed.com")

    # Explicit wait
    time.sleep(10)

    # Print the page source
    print(driver.page_source)

    # Define the wait object
    wait = WebDriverWait(driver, 20)

    # Getting to the search bar and typing a job and location
    search_job = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sugInpt"]')))
    search_job.send_keys(Keys.CONTROL + "a")
    search_job.send_keys("Cybersecurity")

    search_location = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="where"]')))
    search_location.send_keys(Keys.CONTROL + "a") # This clears the location field, as it's pre-filled
    search_location.send_keys("Bellevue, WA")

    # Clicking the "Find Jobs" button to start the search
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="whatWhereFormId"]/div[3]/button')))
    search_button.click()

    # ... rest of your code

scrape_indeed_job_description()
