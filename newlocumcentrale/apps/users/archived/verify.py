# import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# # Specify the relative path to the chromedriver executable
# chromedriver_path = os.path.join(os.getcwd(), 'bin', 'chromedriver')

# # Set the path to the chromedriver executable in the webdriver configuration
# driver = webdriver.Chrome(executable_path=chromedriver_path)


def verify_mdc_details(full_name, category, mdc_number):
    # Specify the relative path to the chromedriver executable
    # chromedriver_path = os.path.join(os.getcwd(), 'bin', 'chromedriver')

    # Set the path to the chromedriver executable in the webdriver configuration
    # driver = webdriver.Chrome()

    # timeout = 10  # Set the timeout value in seconds

    capabilities = DesiredCapabilities.CHROME.copy()
    # capabilities['timeouts'] = {'implicit': int(timeout * 1000),
    #                             'pageLoad': int(timeout * 1000),
    #                             'script': int(timeout * 1000)}

    driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=capabilities)
    # Specify the path to the ChromeDriver executable
    # driver_path = './bin/chromedriver'  # Replace with the actual path

    # Configure Chrome options for running in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Create a Service object with the driver path
    # service = Service()

    # # Start the service
    # service.start()

    # # Create the WebDriver using the service and Chrome options
    # driver = webdriver.Chrome(service=service, options=chrome_options)

    # # Set the maximum amount of time to wait for elements to appear on the page
    # wait = WebDriverWait(driver, 10)

    # Open the webpage
    driver.get("https://portal.mdcghana.org/#/login")

    try:
        # full_name = 'Theodore Amegashie'
        # category = "Doctor"
        # mdc_number = "MDC/RN/12950"
        error_msg = "Sorry, your details could not be verified from the MDC database."

        # Select the appropriate radio button based on the "register_as" value
        if category.lower() == "doctor":
            driver.find_element(By.CSS_SELECTOR, 'input[value="Doctor"]').click()
        else:
            driver.find_element(By.CSS_SELECTOR, 'input[value="PA"]').click()

        # Wait for the "MDC Registration No." field to appear
        mdc_registration_no_field = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="username"]'))
        )

        # Enter the value for the "MDC Registration No." field
        mdc_registration_no_field.send_keys(mdc_number)

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        try:
            # Wait for the h4 element to appear within the iframe
            h4_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "body > app-root > app-login > div > div > div > div > div.card-body > div > h4")
                )
            )

            # Extract and print the text
            text = h4_element.text.strip()

            # if full_name.lower() == text.lower() and set(full_name.lower().split()) == set(text.lower().split()):
            #     print(f"Verified as a {category}")
            # else:
            #     print("names don't match")

            full_name_parts = full_name.lower().split()
            text_parts = text.lower().split()

            matching_names = set(full_name_parts) & set(text_parts)

            if len(matching_names) >= 2:
                print(f"Verified as a {category}")
            else:
                print("Names don't match")

        except NoSuchElementException:
            # Custom error message when the h4 element is not found
            print(error_msg)

    except TimeoutException:
        # Custom error message when the form submission times out
        print(error_msg)

    # Switch back to the main content
    driver.switch_to.default_content()

    # Close the browser
    driver.quit()


if __name__ == "__main__":
    full_name = "Theodore Amegashie"
    category = "Doctor"
    mdc_number = "MDC/RN/12950"

    output = verify_mdc_details(full_name, category, mdc_number)
