# # import os

# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException, TimeoutException

# # from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager

# # from config.settings.base import BASE_DIR


# def verify_mdc_details(full_name, category, mdc_number):
#     # Specify the path to the ChromeDriver executable
#     # driver_path = os.path.join(BASE_DIR, "bin", "chromedriver")

#     # Configure Chrome options for running in headless mode
#     # chrome_options = Options()
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("--headless")

#     # Create the WebDriver using Chrome options
#     # driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

#     # Set the maximum amount of time to wait for elements to appear on the page
#     wait = WebDriverWait(driver, 10)

#     # Open the webpage
#     driver.get("https://portal.mdcghana.org/#/login")

#     try:
#         error_msg = "Sorry, your details could not be verified from the MDC database."

#         # Select the appropriate radio button based on the "register_as" value
#         if category.lower() == "doctor":
#             driver.find_element(By.CSS_SELECTOR, 'input[value="Doctor"]').click()
#         else:
#             driver.find_element(By.CSS_SELECTOR, 'input[value="PA"]').click()

#         # Wait for the "MDC Registration No." field to appear
#         mdc_registration_no_field = wait.until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="username"]'))
#         )

#         # Enter the value for the "MDC Registration No." field
#         mdc_registration_no_field.send_keys(mdc_number)

#         # Submit the form
#         driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

#         try:
#             # Wait for the h4 element to appear within the iframe
#             h4_element = wait.until(
#                 EC.visibility_of_element_located(
#                     (By.CSS_SELECTOR, "body > app-root >
# app-login > div > div > div > div > div.card-body > div > h4")
#                 )
#             )

#             # Extract and print the text
#             text = h4_element.text.strip()

#             full_name_parts = full_name.lower().split()
#             text_parts = text.lower().split()

#             matching_names = set(full_name_parts) & set(text_parts)

#             if len(matching_names) >= 2:
#                 print(f"Verified as a {category}")
#             else:
#                 print("Names don't match")

#         except NoSuchElementException:
#             # Custom error message when the h4 element is not found
#             print(error_msg)

#     except TimeoutException:
#         # Custom error message when the form submission times out
#         print(error_msg)

#     # Close the browser
#     driver.quit()


# if __name__ == "__main__":
#     full_name = "Theodore Amegashie"
#     category = "Doctor"
#     mdc_number = "MDC/RN/12950"

#     verify_mdc_details(full_name, category, mdc_number)

# #     from django.views import View

# # import json

# # import requests
# # from django.http import JsonResponse


# class VerifyMDCDetailsView(View):
#     def post(self, request):
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         user_type = request.POST.get("user_type")
#         mdc_number = request.POST.get("mdc_number")
#         url = "https://manager.mdcghana.org/api/getDetailsByRegNum"

#         headers = {
#             "User-Agent": "PostmanRuntime/7.32.3",
#             "Accept": "*/*",
#             "Cache-Control": "no-cache",
#             "Postman-Token": "d9cc4ce6-e9a6-4804-b14c-18675eee43ab",
#             "Host": "manager.mdcghana.org",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Connection": "keep-alive",
#         }

#         payload = {"username": mdc_number, "type": user_type}

#         try:
#             retrieved_data = self.make_request(url, payload, headers)
#             status = retrieved_data["status"]

#             if status == "0":
#                 # Retry with the other user type
#                 payload["type"] = self.try_alternate_user_type(user_type)
#                 retrieved_data = self.make_request(url, payload, headers)
#                 status = retrieved_data["status"]

#                 if status == "0":
#                     return JsonResponse(json.dumps({"message": "Your details could not be verified"}), safe=False)

#             if status == "1":
#                 verification_result = self.verify_user(retrieved_data, first_name, last_name, user_type)
#                 return JsonResponse(verification_result, safe=False)

#         except requests.RequestException as e:
#             return JsonResponse(json.dumps({"message": "Error occurred during the request: " + str(e)}), safe=False)

#     def make_request(self, url, payload, headers):
#         response = requests.post(url, data=payload, headers=headers)
#         response.raise_for_status()
#         return response.json()

#     def try_alternate_user_type(self, user_type):
#         if user_type == "Doctor":
#             return "PA"
#         else:
#             return "Doctor"

#     def verify_user(self, retrieved_data, first_name, last_name, user_type):
#         retrieved_first_name = retrieved_data["user_data"]["first_name"]
#         retrieved_last_name = retrieved_data["user_data"]["last_name"]
#         specialty = retrieved_data["user_data"]["specialty"]
#         register_type = retrieved_data["user_data"]["register_type"]
#         year_of_provisional = retrieved_data["user_data"]["year_of_provisional"]
#         phone = retrieved_data["user_data"]["phone"]
#         category = retrieved_data["user_data"]["category"]

#         if {first_name, last_name} == {retrieved_first_name, retrieved_last_name}:
#             response_data = {
#                 "status": f"Verified as a {user_type}",
#                 "specialty": specialty,
#                 "register_type": register_type,
#                 "year_of_provisional": year_of_provisional,
#                 "phone": phone,
#                 "category": category,
#             }
#             response_json = json.dumps(response_data)
#             return response_json
#         else:
#             return JsonResponse(json.dumps({"message": "Your details could not be verified"}), safe=False)
