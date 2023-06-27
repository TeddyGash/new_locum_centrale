# import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# from config.settings.base import BASE_DIR


def verify_mdc_details(full_name, category, mdc_number):
    # Specify the path to the ChromeDriver executable
    # driver_path = os.path.join(BASE_DIR, "bin", "chromedriver")

    # Configure Chrome options for running in headless mode
    # chrome_options = Options()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    # Create the WebDriver using Chrome options
    # driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    # Set the maximum amount of time to wait for elements to appear on the page
    wait = WebDriverWait(driver, 10)

    # Open the webpage
    driver.get("https://portal.mdcghana.org/#/login")

    try:
        error_msg = "Sorry, your details could not be verified from the MDC database."

        # Select the appropriate radio button based on the "register_as" value
        if category.lower() == "doctor":
            driver.find_element(By.CSS_SELECTOR, 'input[value="Doctor"]').click()
        else:
            driver.find_element(By.CSS_SELECTOR, 'input[value="PA"]').click()

        # Wait for the "MDC Registration No." field to appear
        mdc_registration_no_field = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="username"]'))
        )

        # Enter the value for the "MDC Registration No." field
        mdc_registration_no_field.send_keys(mdc_number)

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        try:
            # Wait for the h4 element to appear within the iframe
            h4_element = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "body > app-root > app-login > div > div > div > div > div.card-body > div > h4")
                )
            )

            # Extract and print the text
            text = h4_element.text.strip()

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

    # Close the browser
    driver.quit()


if __name__ == "__main__":
    full_name = "Theodore Amegashie"
    category = "Doctor"
    mdc_number = "MDC/RN/12950"

    verify_mdc_details(full_name, category, mdc_number)
