import requests
from django.core.cache import cache
from django.http import JsonResponse
from django.views import View

# from django.http import request


class VerifyMDCDetailsView(View):
    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        user_type = request.POST.get("user_type")
        mdc_number = request.POST.get("mdc_number")
        url = "https://manager.mdcghana.org/api/getDetailsByRegNum"

        headers = {
            "User-Agent": "PostmanRuntime/7.32.3",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Postman-Token": "d9cc4ce6-e9a6-4804-b14c-18675eee43ab",
            "Host": "manager.mdcghana.org",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        payload = {"username": mdc_number, "type": user_type}

        try:
            retrieved_data = self.make_request(url, payload, headers)
            status = retrieved_data["status"]

            if status == "0":
                return JsonResponse({"status": "Wrong MDC number"})

            elif status == "1":
                verification_result = self.verify_user(mdc_number, retrieved_data, first_name, last_name)
                return JsonResponse(verification_result)

        except requests.RequestException as e:
            return JsonResponse({"status": "Error occurred during the request: " + str(e)})

    def make_request(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    def verify_user(self, mdc_number, retrieved_data, first_name, last_name):
        retrieved_first_name = retrieved_data["user_data"]["first_name"]
        retrieved_last_name = retrieved_data["user_data"]["last_name"]
        specialty = retrieved_data["user_data"]["specialty"]
        register_type = retrieved_data["user_data"]["register_type"]
        year_of_provisional = retrieved_data["user_data"]["year_of_provisional"]
        phone = retrieved_data["user_data"]["phone"]
        category = retrieved_data["user_data"]["category"]

        if {first_name.lower(), last_name.lower()} == {retrieved_first_name.lower(), retrieved_last_name.lower()}:
            response_data = {
                "status": "verified",
                "verification_status": "True",
                "specialty": specialty,
                "register_type": register_type,
                "year_of_provisional": year_of_provisional,
                "phone": phone,
                "category": category,
            }

            # Store the response_data in cache
            cache.set(mdc_number, response_data)

            return response_data

        else:
            return {"status": "Names don't match"}
