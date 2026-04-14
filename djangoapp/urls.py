from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('', views.get_dealerships, name='index'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.registration_request, name='register'),
    path('get_cars/', views.get_cars, name='get_cars'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('dealer/<int:dealer_id>/review/', views.add_review, name='add_review'),
    path('dealer/state/<str:filter_state>/', views.get_dealerships, name='dealers_by_state'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
