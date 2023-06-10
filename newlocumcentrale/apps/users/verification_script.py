import time

import requests
from bs4 import BeautifulSoup


def verify_mdc_details(category, mdc_number, full_name):
    error_msg = "Sorry, your details could not be verified from the MDC database."

    # Make a request to the target website
    response = requests.get("https://portal.mdcghana.org/#/login")

    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the appropriate radio button based on the "register_as" value
        if category.lower() == "doctor":
            radio_button_value = "Doctor"
        else:
            radio_button_value = "PA"

        radio_button = soup.find("input", {"value": radio_button_value})
        if radio_button:
            # Click the radio button by modifying its "checked" attribute
            radio_button["checked"] = "checked"

            # Find the "MDC Registration No." field
            mdc_registration_no_field = soup.find("input", {"name": "username"})

            if mdc_registration_no_field:
                # Set the value for the "MDC Registration No." field
                mdc_registration_no_field["value"] = mdc_number

                # Submit the form by finding the submit button and simulating a click
                submit_button = soup.find("button", {"type": "submit"})
                if submit_button:
                    # Make a request to the form submission URL
                    response = requests.post("https://portal.mdcghana.org/#/login", data=soup.form)

                    if response.status_code == 200:
                        # Delay for 5 seconds to allow the page to load
                        time.sleep(5)

                        # Create a new BeautifulSoup object to parse the response
                        soup = BeautifulSoup(response.content, "html.parser")

                        # Find the h4 element within the response HTML
                        h4_element = soup.find("h4")
                        if h4_element:
                            # Extract and return the text
                            text = h4_element.text.strip()

                            full_name_parts = full_name.lower().split()
                            text_parts = text.lower().split()

                            matching_names = set(full_name_parts) & set(text_parts)

                            if len(matching_names) >= 2:
                                return f"Verified as a {category}"
                            else:
                                return "Names don't match"

                        else:
                            # Custom error message when the h4 element is not found
                            return error_msg

    # Custom error message when the request or any required elements are not found
    return error_msg
