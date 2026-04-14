from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime
import logging
import json

from .models import CarMake, CarModel
from .restapis import (
    get_dealers_from_cf,
    get_dealer_by_id_from_cf,
    get_dealers_by_state,
    get_dealer_reviews_from_cf,
    get_request,
    analyze_review_sentiments
)

logger = logging.getLogger(__name__)

# --- Dealer endpoints ---
DEALERS_URL = "/fetchDealers"
DEALER_BY_ID_URL = "/fetchDealer"
REVIEWS_URL = "/fetchReviews"
POST_REVIEW_URL = "/postReview"


def get_dealerships(request, filter_state="All"):
    if filter_state == "All":
        endpoint = DEALERS_URL
        dealerships = get_dealers_from_cf(endpoint)
    else:
        endpoint = DEALERS_URL
        dealerships = get_dealers_by_state(endpoint, filter_state)
    return render(request, 'djangoapp/index.html', {"dealer_list": dealerships})


def get_dealer_details(request, dealer_id):
    context = {}
    reviews = get_dealer_reviews_from_cf(REVIEWS_URL, dealer_id)
    dealers = get_dealer_by_id_from_cf(DEALER_BY_ID_URL, dealer_id)
    context["reviews"] = reviews
    if dealers:
        context["dealer"] = dealers[0]
    return render(request, 'djangoapp/dealer_details.html', context)


@login_required
def add_review(request, dealer_id):
    context = {}
    dealers = get_dealer_by_id_from_cf(DEALER_BY_ID_URL, dealer_id)
    if dealers:
        context["dealer"] = dealers[0]

    if request.method == "GET":
        cars = CarModel.objects.filter(dealer_id=dealer_id)
        context["cars"] = cars
        return render(request, 'djangoapp/add_review.html', context)

    if request.method == "POST":
        form = request.POST
        review = {
            "time": datetime.utcnow().isoformat(),
            "name": request.user.first_name + " " + request.user.last_name,
            "dealership": dealer_id,
            "review": form["content"],
            "purchase": "purchase" in form,
            "purchase_date": form.get("purchasedate", ""),
            "car_make": form.get("car_make", ""),
            "car_model": form.get("car_model", ""),
            "car_year": form.get("car_year", ""),
        }
        new_review = {"review": review}
        response = get_request(POST_REVIEW_URL, json=new_review)
        return redirect("djangoapp:dealer_details", dealer_id=dealer_id)


# --- Auth views ---
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('psw')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
    return render(request, 'djangoapp/index.html', context)


def logout_request(request):
    logout(request)
    return redirect('djangoapp:index')


def get_cars(request):
    count = CarMake.objects.filter().count()
    if count == 0:
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = [
        {"CarMake": cm.car_make.name, "CarModel": cm.name, "car_type": cm.car_type, "ModelYear": str(cm.year)}
        for cm in car_models
    ]
    return JsonResponse({"CarModels": cars})


def initiate():
    car_make_data = [
        {"name": "Toyota", "description": "Japanese automotive manufacturer"},
        {"name": "Honda", "description": "Japanese multinational conglomerate"},
        {"name": "Ford", "description": "American multinational automaker"},
        {"name": "BMW", "description": "German luxury vehicle manufacturer"},
    ]
    car_make_instances = []
    for data in car_make_data:
        cm, _ = CarMake.objects.get_or_create(name=data["name"], defaults={"description": data["description"]})
        car_make_instances.append(cm)

    car_model_data = [
        {"name": "Camry", "car_make": car_make_instances[0], "car_type": "SEDAN", "year": "2022-01-01", "dealer_id": 1},
        {"name": "RAV4", "car_make": car_make_instances[0], "car_type": "SUV", "year": "2023-01-01", "dealer_id": 1},
        {"name": "Civic", "car_make": car_make_instances[1], "car_type": "SEDAN", "year": "2022-01-01", "dealer_id": 2},
        {"name": "CR-V", "car_make": car_make_instances[1], "car_type": "SUV", "year": "2023-01-01", "dealer_id": 2},
        {"name": "F-150", "car_make": car_make_instances[2], "car_type": "TRUCK", "year": "2022-01-01", "dealer_id": 3},
        {"name": "Mustang", "car_make": car_make_instances[2], "car_type": "COUPE", "year": "2023-01-01", "dealer_id": 3},
        {"name": "3 Series", "car_make": car_make_instances[3], "car_type": "SEDAN", "year": "2022-01-01", "dealer_id": 4},
        {"name": "X5", "car_make": car_make_instances[3], "car_type": "SUV", "year": "2023-01-01", "dealer_id": 4},
    ]
    for data in car_model_data:
        CarModel.objects.get_or_create(name=data["name"], car_make=data["car_make"],
            defaults={"car_type": data["car_type"], "year": data["year"], "dealer_id": data["dealer_id"]})


def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']

        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")

        if not user_exist:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                email=email
            )
            login(request, user)
            return redirect("djangoapp:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/registration.html', context)
