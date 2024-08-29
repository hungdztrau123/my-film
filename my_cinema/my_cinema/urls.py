"""my_cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static
from auth_manager.views import  UserLoginView, UserRegisterView
from auth_manager.views import LogoutAPIView
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import RedirectView
from django.views.static import serve
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from cinema_manager.views import base
from cinema_manager.views import register
from cinema_manager.views import login
from cinema_manager.views import home
from cinema_manager.views import homepage
from cinema_manager.views import area
from cinema_manager.views import promotion
from cinema_manager.views import film
from cinema_manager.views import room
from cinema_manager.views import bookfilm
from cinema_manager.views import promotionlist
from cinema_manager.views import contact
from cinema_manager.views import booking

from cinema_manager.views import adminmanager
from cinema_manager.views import combomanage
from cinema_manager.views import comboinsert
from cinema_manager.views import comboupdate

from cinema_manager.views import filmmanage
from cinema_manager.views import filminsert
from cinema_manager.views import filmupdate

from cinema_manager.views import schedulemanage
from cinema_manager.views import scheduleinsert
from cinema_manager.views import scheduleupdate

from cinema_manager.views import areamanage
from cinema_manager.views import areainsert
from cinema_manager.views import areaupdate

from cinema_manager.views import placemanage
from cinema_manager.views import placeinsert
from cinema_manager.views import placeupdate

from cinema_manager.views import dayshowmanage
from cinema_manager.views import dayshowinsert
from cinema_manager.views import dayshowupdate

from cinema_manager.views import roommanage
from cinema_manager.views import roominsert
from cinema_manager.views import roomupdate

from cinema_manager.views import seatmanage
from cinema_manager.views import seatinsert
from cinema_manager.views import seatupdate

from cinema_manager.views import imagemanage
from cinema_manager.views import imageinsert
from cinema_manager.views import imageupdate

from cinema_manager.views import videomanage
from cinema_manager.views import videoinsert
from cinema_manager.views import videoupdate


# from cinema_manager.views import map_view



from auth_manager.views import UserViewSet, UserProfileViewSet

from cinema_manager.views import FilmViewSet
from cinema_manager.views import PromotionViewSet
from cinema_manager.views import BulkEditObjectsView
from cinema_manager.views import AreaViewSet
from cinema_manager.views import PlaceViewSet
from cinema_manager.views import DayShowViewSet
from cinema_manager.views import ScheduleViewSet
from cinema_manager.views import RoomViewSet
from cinema_manager.views import SeatViewSet
from cinema_manager.views import ImageViewSet
from cinema_manager.views import VideoViewSet
from cinema_manager.views import ServiceViewSet
from cinema_manager.views import ContactViewSet
from cinema_manager.views import CategoryViewSet
from cinema_manager.views import CategoryFilmViewSet
from cinema_manager.views import TicketViewSet
from cinema_manager.views import BookingViewSet
from cinema_manager.views import BookingDetailViewSet
from cinema_manager.views import CommentViewSet
from cinema_manager.views import ComboViewSet


api_router = DefaultRouter()

api_router.register(r"users", UserViewSet)
api_router.register(r"user_profiles", UserProfileViewSet)
api_router.register(r"promotions", PromotionViewSet)
api_router.register(r"areas", AreaViewSet)
api_router.register(r"places", PlaceViewSet)
api_router.register(r"dayshows", DayShowViewSet)
api_router.register(r"films", FilmViewSet)
api_router.register(r"schedules", ScheduleViewSet)
api_router.register(r"rooms", RoomViewSet)
api_router.register(r"seats", SeatViewSet)
api_router.register(r"images", ImageViewSet)
api_router.register(r"videos", VideoViewSet)
api_router.register(r"services", ServiceViewSet)
api_router.register(r"contacts", ContactViewSet)
api_router.register(r"categories", CategoryViewSet)
api_router.register(r"categoryfilms", CategoryFilmViewSet)
api_router.register(r"tickets", TicketViewSet)
api_router.register(r"bookings", BookingViewSet)
api_router.register(r"bookingdetails", BookingDetailViewSet)
api_router.register(r"comments", CommentViewSet)
api_router.register(r"combos", ComboViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base, name = "base"),
    path('register/', register, name = "register"),
    path('login/', login, name = "login"),
    
    path('home/', home, name = "home"),
    path('homepage/', homepage, name = "homepage"),
    path('area/', area, name = "area"),
    path('promotion/<int:id>/', promotion, name = "promotion"),
    path('film/<int:id>/', film, name = "film"),
    path('bookfilm/<int:id>/', bookfilm, name = "bookfilm"),
    path('room/<int:id>/', room, name = "room"),
    path('promotionlist/', promotionlist, name = "promotionlist"),
    path('contact/', contact, name = "contact"),
    path('booking/<int:id>/', booking, name = "booking"),
    
    
    path('adminmanager/', adminmanager, name = "adminmanager"),
    path('combomanage/', combomanage, name = "combomanage"),
    path('comboinsert/', comboinsert, name = "comboinsert"),
    path('comboupdate/', comboupdate, name = "comboupdate"),
    
    path('filmmanage/', filmmanage, name = "filmmanage"),
    path('filminsert/', filminsert, name = "filminsert"),
    path('filmupdate/', filmupdate, name = "filmupdate"),
    
    path('schedulemanage/', schedulemanage, name = "schedulemanage"),
    path('scheduleinsert/', scheduleinsert, name = "scheduleinsert"),
    path('scheduleupdate/', scheduleupdate, name = "scheduleupdate"),
    
    path('areamanage/', areamanage, name = "areamanage"),
    path('areainsert/', areainsert, name = "areainsert"),
    path('areaupdate/', areaupdate, name = "areaupdate"),
    
    path('placemanage/', placemanage, name = "placemanage"),
    path('placeinsert/', placeinsert, name = "placeinsert"),
    path('placeupdate/', placeupdate, name = "placeupdate"),
    
    path('dayshowmanage/', dayshowmanage, name = "dayshowmanage"),
    path('dayshowinsert/', dayshowinsert, name = "dayshowinsert"),
    path('dayshowupdate/', dayshowupdate, name = "dayshowupdate"),
    
    path('roommanage/', roommanage, name = "roommanage"),
    path('roominsert/', roominsert, name = "roominsert"),
    path('roomupdate/', roomupdate, name = "roomupdate"),
    
    path('seatmanage/', seatmanage, name = "seatmanage"),
    path('seatinsert/', seatinsert, name = "seatinsert"),
    path('seatupdate/', seatupdate, name = "seatupdate"),
    
    path('imagemanage/', imagemanage, name = "imagemanage"),
    path('imageinsert/', imageinsert, name = "imageinsert"),
    path('imageupdate/', imageupdate, name = "imageupdate"),
    
    path('videomanage/', videomanage, name = "videomanage"),
    path('videoinsert/', videoinsert, name = "videoinsert"),
    path('videoupdate/', videoupdate, name = "videoupdate"),
    
    

    
    re_path(
        r"^api/",
        include(
            [
              
                re_path('^login/', UserLoginView.as_view(), name='login'),
                re_path('^register/', UserRegisterView.as_view(), name='register'),
                re_path('^logout/', LogoutAPIView.as_view(), name='logout'),
                re_path('^bulk_edit_objects/', BulkEditObjectsView.as_view(), name='bulk_edit_objects'),
                
                
                *api_router.urls,
            ],
        ),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
