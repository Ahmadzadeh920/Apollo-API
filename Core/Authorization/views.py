# views.py
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from django.http import JsonResponse
from .models import HeaderRequest
import time





def authenticate_and_fetch(request):
    # Set up the webdriver for Chrome or your preferred browser
    driver = webdriver.Chrome()

    try:
        # Open Apollo.io and perform authentication
        driver.get("https://app.apollo.io/login")

        # Find the username and password inputs, fill them, and submit the form
        driver.find_element(By.NAME, "email").send_keys("sophie@skyhighsalescontact.com")
        driver.find_element(By.NAME, "password").send_keys("Thankyouforyourassessment24")
        driver.find_element(By.NAME, "submit").click()  # Adjust the selector as needed

        # Set up Chrome options to enable the DevTools Protocol
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run headless if you don't need UI
        # Ignores any certificate errors if there is any 
        options.add_argument("--ignore-certificate-errors") 

        # Create a new instance of Chrome
        # Enable the DevTools Protocol
        #Create a new instance of Chrome
        capabilities = DesiredCapabilities.CHROME
        capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}

        driver = webdriver.Chrome(service=Service('path_to_chromedriver'), options=options, desired_capabilities=capabilities)


        # After successful login, wait for navigation to the desired page
        driver.get("https://app.apollo.io/people")

        # Wait for the page to load 
        time.sleep(10)
        # Gets all the logs from performance in Chrome 
        logs = driver.get_log("performance") 
        for entry in logs:
            if 'request' in entry['message']:  # Check if it's a request
                message = json.loads(entry['message'])
                if 'params' in message['message'] and 'request' in message['message']['params']:
                    request = message['message']['params']['request']
                    url = request.get('url', '')
                    
                    # Check for the specific URL
                    if "https://app.apollo.io/api/v1/mixed_people/search" in url:
                        headers = request.get('headers', {})
                        cookies = request.get('cookies', {})
                        post_data = request.get('postData', None)
        
       

        # Save the data
        header_request = HeaderRequest(url="https://app.apollo.io/api/v1/mixed_people/search")
        header_request.set_cookies(cookies)
        header_request.set_headers(headers)
        header_request.set_payload(post_data)

        # Save to the database
        header_request.save()
        

        return JsonResponse({"success": True, "data": data})
    finally:
        driver.quit() 