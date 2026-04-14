import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth


# Fetch all dealers from MongoDB microservice
def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"

    request_url = "http://localhost:3000" + endpoint + "?" + params
    print(f"GET from {request_url}")

    try:
        response = requests.get(request_url)
        status_code = response.status_code
        json_data = json.loads(response.text)
        return json_data
    except Exception as e:
        print(f"Network exception occurred: {e}")
        return None


# Analyze review sentiment using Watson NLU microservice
def analyze_review_sentiments(dealer_review):
    request_url = f"http://localhost:5050/analyze/{dealer_review}"
    try:
        response = requests.get(request_url)
        status_code = response.status_code
        json_data = json.loads(response.text)
        return json_data
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def get_dealers_from_cf(url, **kwargs):
    results = []
    json_result = get_request(url)
    if json_result:
        dealers = json_result["dealers"]
        for dealer_doc in dealers:
            dealer_obj = CarDealer(
                address=dealer_doc["address"],
                city=dealer_doc["city"],
                full_name=dealer_doc["full_name"],
                id=dealer_doc["id"],
                lat=dealer_doc["lat"],
                long=dealer_doc["long"],
                short_name=dealer_doc["short_name"],
                st=dealer_doc["st"],
                zip=dealer_doc["zip"]
            )
            results.append(dealer_obj)
    return results


def get_dealer_by_id_from_cf(url, dealer_id):
    results = []
    json_result = get_request(url, id=dealer_id)
    if json_result:
        dealers = json_result["dealers"]
        for dealer_doc in dealers:
            dealer_obj = CarDealer(
                address=dealer_doc["address"],
                city=dealer_doc["city"],
                full_name=dealer_doc["full_name"],
                id=dealer_doc["id"],
                lat=dealer_doc["lat"],
                long=dealer_doc["long"],
                short_name=dealer_doc["short_name"],
                st=dealer_doc["st"],
                zip=dealer_doc["zip"]
            )
            results.append(dealer_obj)
    return results


def get_dealers_by_state(url, state):
    results = []
    json_result = get_request(url, state=state)
    if json_result:
        dealers = json_result["dealers"]
        for dealer_doc in dealers:
            dealer_obj = CarDealer(
                address=dealer_doc["address"],
                city=dealer_doc["city"],
                full_name=dealer_doc["full_name"],
                id=dealer_doc["id"],
                lat=dealer_doc["lat"],
                long=dealer_doc["long"],
                short_name=dealer_doc["short_name"],
                st=dealer_doc["st"],
                zip=dealer_doc["zip"]
            )
            results.append(dealer_obj)
    return results


def get_dealer_reviews_from_cf(url, dealer_id):
    results = []
    json_result = get_request(url, id=dealer_id)
    if json_result:
        reviews = json_result["reviews"]
        for review_doc in reviews:
            review_obj = DealerReview(
                dealership=review_doc["dealership"],
                name=review_doc["name"],
                purchase=review_doc["purchase"],
                review=review_doc["review"],
                purchase_date=review_doc.get("purchase_date", ""),
                car_make=review_doc.get("car_make", ""),
                car_model=review_doc.get("car_model", ""),
                car_year=review_doc.get("car_year", ""),
                sentiment=review_doc.get("sentiment", ""),
                id=review_doc["id"]
            )
            sentiment_result = analyze_review_sentiments(review_doc["review"])
            if sentiment_result:
                review_obj.sentiment = sentiment_result.get("sentiment", "neutral")
            results.append(review_obj)
    return results
