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

import my_cinema.views

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
from cinema_manager.views import bookcombo
from cinema_manager.views import listticket
from cinema_manager.views import ticketissued
from cinema_manager.views import infouser




from cinema_manager.views import promotionlist
from cinema_manager.views import contact
from cinema_manager.views import booking

from cinema_manager.views import adminmanager

from cinema_manager.views import statisticalmanage

from cinema_manager.views import usermanage

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

from cinema_manager.views import commentmanage
from cinema_manager.views import commentupdate

from cinema_manager.views import ticketmanage
from cinema_manager.views import ticketinsert
from cinema_manager.views import ticketupdate

from cinema_manager.views import actormanage
from cinema_manager.views import actorinsert
from cinema_manager.views import actorupdate

from cinema_manager.views import categorymanage
from cinema_manager.views import categoryinsert
from cinema_manager.views import categoryupdate

from cinema_manager.views import categoryfilmmanage
from cinema_manager.views import categoryfilminsert
from cinema_manager.views import categoryfilmupdate

from cinema_manager.views import bookingmanage
from cinema_manager.views import bookinginsert
from cinema_manager.views import bookingupdate

from cinema_manager.views import promotionmanage
from cinema_manager.views import promotioninsert
from cinema_manager.views import promotionupdate

from cinema_manager.views import servicemanage
from cinema_manager.views import serviceinsert
from cinema_manager.views import serviceupdate

from cinema_manager.views import contactmanage
from cinema_manager.views import contactinsert
from cinema_manager.views import contactupdate

from cinema_manager.views import logomanage
from cinema_manager.views import logoinsert
from cinema_manager.views import logoupdate

from cinema_manager.views import backgroundmanage
from cinema_manager.views import backgroundinsert
from cinema_manager.views import backgroundupdate


from cinema_manager.views import paymanage

from cinema_manager.views import billmanage


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
from cinema_manager.views import ActorViewSet
from cinema_manager.views import UserProfileViewSet
from cinema_manager.views import PayViewSet
from cinema_manager.views import BillViewSet
from cinema_manager.views import LogoViewSet
from cinema_manager.views import BackgroundViewSet
from cinema_manager.views import ComboDetailViewSet
from cinema_manager.views import UserQueryViewSet








api_router = DefaultRouter()

api_router.register(r"logos", LogoViewSet)
api_router.register(r"backgrounds", BackgroundViewSet)
api_router.register(r"userprofiles", UserProfileViewSet)
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
api_router.register(r"combodetails", ComboDetailViewSet)
api_router.register(r"comments", CommentViewSet)
api_router.register(r"combos", ComboViewSet)
api_router.register(r"actors", ActorViewSet)
api_router.register(r"pays", PayViewSet)
api_router.register(r"bills", BillViewSet)
api_router.register(r"queries", UserQueryViewSet)



urlpatterns = [
    
    
    path('', my_cinema.views.index, name='index'),
    path('payment/', my_cinema.views.payment, name='payment'),
    path('payment_ipn/', my_cinema.views.payment_ipn, name='payment_ipn'),
    path('payment_return/', my_cinema.views.payment_return, name='payment_return'),
    path('query/', my_cinema.views.query, name='query'),
    path('refund/', my_cinema.views.refund, name='refund'),
    
        
    
    
    
    
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
    path('bookcombo/<int:id>/', bookcombo, name = "bookcombo"),
    path('listticket/<int:id>/', listticket, name = "listticket"),
    
    
    path('room/<int:id>/', room, name = "room"),
    path('promotionlist/', promotionlist, name = "promotionlist"),
    path('contact/', contact, name = "contact"),
    path('booking/<int:id>/', booking, name = "booking"),

    path('ticketissued/<int:id>/', ticketissued, name = "ticketissued"),
    path('infouser/<int:id>/', infouser, name = "infouser"),
    
    
    
    
    
    path('adminmanager/', adminmanager, name = "adminmanager"),
    
    path('statisticalmanage/', statisticalmanage, name = "statisticalmanage"),
    
    
    path('usermanage/', usermanage, name = "usermanage"),
   
    
    
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
    
    path('commentmanage/', commentmanage, name = "commentmanage"),
    path('commentupdate/', commentupdate, name = "commentupdate"),
    
    path('ticketmanage/', ticketmanage, name = "ticketmanage"),
    path('ticketinsert/', ticketinsert, name = "ticketinsert"),
    path('ticketupdate/', ticketupdate, name = "ticketupdate"),
    
    path('actormanage/', actormanage, name = "actormanage"),
    path('actorinsert/', actorinsert, name = "actorinsert"),
    path('actorupdate/', actorupdate, name = "actorupdate"),
    
    path('categorymanage/', categorymanage, name = "categorymanage"),
    path('categoryinsert/', categoryinsert, name = "categoryinsert"),
    path('categoryupdate/', categoryupdate, name = "categoryupdate"),
    
    path('categoryfilmmanage/', categoryfilmmanage, name = "categoryfilmmanage"),
    path('categoryfilminsert/', categoryfilminsert, name = "categoryfilminsert"),
    path('categoryfilmupdate/', categoryfilmupdate, name = "categoryfilmupdate"),

    path('bookingmanage/', bookingmanage, name = "bookingmanage"),
    path('bookinginsert/', bookinginsert, name = "bookinginsert"),
    path('bookingupdate/', bookingupdate, name = "bookingupdate"),
    
    path('promotionmanage/', promotionmanage, name = "promotionmanage"),
    path('promotioninsert/', promotioninsert, name = "promotioninsert"),
    path('promotionupdate/', promotionupdate, name = "promotionupdate"),
    
    path('servicemanage/', servicemanage, name = "servicemanage"),
    path('serviceinsert/', serviceinsert, name = "serviceinsert"),
    path('serviceupdate/', serviceupdate, name = "serviceupdate"),
    
    path('contactmanage/', contactmanage, name = "contactmanage"),
    path('contactinsert/', contactinsert, name = "contactinsert"),
    path('contactupdate/', contactupdate, name = "contactupdate"),
    
    path('logomanage/', logomanage, name = "logomanage"),
    path('logoinsert/', logoinsert, name = "logoinsert"),
    path('logoupdate/', logoupdate, name = "logoupdate"),
    
    path('backgroundmanage/', backgroundmanage, name = "backgroundmanage"),
    path('backgroundinsert/', backgroundinsert, name = "backgroundinsert"),
    path('backgroundupdate/', backgroundupdate, name = "backgroundupdate"),
    
    
    path('paymanage/', paymanage, name = "paymanage"),

    
    path('billmanage/', billmanage, name = "billmanage"),
  
    
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
