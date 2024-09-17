import os
from collections import OrderedDict

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models.functions import Lower
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from rest_framework import parsers, status
from django.views.generic import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.models import Token
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.renderers import JSONRenderer
from datetime import datetime, timedelta
from django.utils import timezone
import hashlib
from django.shortcuts import render
from my_cinema.views import StandardPagination
import folium

from cinema_manager.permissions import AdminPermission
from cinema_manager.permissions import UserPermission
from cinema_manager.permissions import AccessTokenPermission

from cinema_manager.models import Films
from cinema_manager.models import Promotion
from cinema_manager.models import Area
from cinema_manager.models import Place
from cinema_manager.models import DayShow
from cinema_manager.models import Schedules
from cinema_manager.models import Rooms
from cinema_manager.models import Seats
from cinema_manager.models import Image
from cinema_manager.models import Video
from cinema_manager.models import Service
from cinema_manager.models import Contact
from cinema_manager.models import Categories
from cinema_manager.models import CategoryFilm
from cinema_manager.models import Tickets
from cinema_manager.models import Bookings
from cinema_manager.models import BookingDetail
from cinema_manager.models import Comments
from cinema_manager.models import Combo
from cinema_manager.models import Actors
from cinema_manager.models import UserProfile
from cinema_manager.models import Pay
from cinema_manager.models import Bill
from cinema_manager.models import Logo
from cinema_manager.models import Background
from cinema_manager.models import ComboDetail



from cinema_manager.serializers import FilmSerializer
from cinema_manager.serializers import PromotionSerializer
from cinema_manager.serializers import BulkEditObjectsSerializer
from cinema_manager.serializers import AreaSerializer
from cinema_manager.serializers import PlaceSerializer
from cinema_manager.serializers import DayShowSerializer
from cinema_manager.serializers import ScheduleSerializer
from cinema_manager.serializers import RoomSerializer
from cinema_manager.serializers import SeatSerializer
from cinema_manager.serializers import ImageSerializer
from cinema_manager.serializers import VideoSerializer
from cinema_manager.serializers import ServiceSerializer
from cinema_manager.serializers import ContactSerializer
from cinema_manager.serializers import CategorySerializer
from cinema_manager.serializers import CategoryFilmSerializer
from cinema_manager.serializers import TicketSerializer
from cinema_manager.serializers import BookingSerializer
from cinema_manager.serializers import BookingDetailSerializer
from cinema_manager.serializers import CommentSerializer
from cinema_manager.serializers import ComboSerializer
from cinema_manager.serializers import ActorSerializer
from cinema_manager.serializers import UserProfileSerializer
from cinema_manager.serializers import PaySerializer
from cinema_manager.serializers import BillSerializer
from cinema_manager.serializers import LogoSerializer
from cinema_manager.serializers import BackgroundSerializer
from cinema_manager.serializers import ComboDetailSerializer





from cinema_manager.filters import FilmFilterSet
from cinema_manager.filters import PromotionFilterSet
from cinema_manager.filters import AreaFilterSet
from cinema_manager.filters import PlaceFilterSet
from cinema_manager.filters import DayShowFilterSet
from cinema_manager.filters import ScheduleFilterSet
from cinema_manager.filters import RoomFilterSet
from cinema_manager.filters import SeatFilterSet
from cinema_manager.filters import ImageFilterSet
from cinema_manager.filters import VideoFilterSet
from cinema_manager.filters import ServiceFilterSet
from cinema_manager.filters import ContactFilterSet
from cinema_manager.filters import CategoryFilterSet
from cinema_manager.filters import CategoryFilmFilterSet
from cinema_manager.filters import TicketFilterSet
from cinema_manager.filters import BookingFilterSet
from cinema_manager.filters import BookingDetailFilterSet
from cinema_manager.filters import CommentFilterSet
from cinema_manager.filters import ComboFilterSet
from cinema_manager.filters import ActorFilterSet
from cinema_manager.filters import UserProfileFilterSet
from cinema_manager.filters import PayFilterSet
from cinema_manager.filters import BillFilterSet
from cinema_manager.filters import LogoFilterSet
from cinema_manager.filters import BackgroundFilterSet
from cinema_manager.filters import ComboDetailFilterSet




from cinema_manager.models import ChoiceCountries, ChoiceStatus
from cinema_manager.models import ChoiceTypeSeat, ChoiceKindSeat
from cinema_manager.models import ChoiceVideoType
from cinema_manager.models import ChoiceTypeTicket
from cinema_manager.models import ChoiceStatusPay
from cinema_manager.models import ChoiceStatusSchedule




def adminmanager(request):
    context = {}
    return render(request, '../templates/adminmanager.html', context)

def combomanage(request):
    context = {}
    return render(request, '../templates/combomanage.html', context)

def comboinsert(request):
    context = {}
    return render(request, '../templates/comboinsert.html', context)

def comboupdate(request):
    context = {}
    return render(request, '../templates/comboupdate.html', context)


def filmmanage(request):
    context = {}
    return render(request, '../templates/filmmanage.html', context)

def filminsert(request):
    countries = [c.value for c in ChoiceCountries]
    statuses = [s.value for s in ChoiceStatus]
    context = {
        'countries': countries,
        'statuses': statuses,
    }
    return render(request, '../templates/filminsert.html', context)

def filmupdate(request):
    countries = [c.value for c in ChoiceCountries]
    statuses = [s.value for s in ChoiceStatus]
    context = {
        'countries': countries,
        'statuses': statuses,
    }
    return render(request, '../templates/filmupdate.html', context)


def schedulemanage(request):
    context = {}
    return render(request, '../templates/schedulemanage.html', context)

def scheduleinsert(request):
    statuses = [s.value for s in ChoiceStatusSchedule]
    context = {
        
        'statuses': statuses,
    }
    return render(request, '../templates/scheduleinsert.html', context)

def scheduleupdate(request):
    statuses = [s.value for s in ChoiceStatusSchedule]
    context = {
        
        'statuses': statuses,
    }
    return render(request, '../templates/scheduleupdate.html', context)


def areamanage(request):
    context = {}
    return render(request, '../templates/areamanage.html', context)

def areainsert(request):
    context = {}
    return render(request, '../templates/areainsert.html', context)

def areaupdate(request):
    context = {}
    return render(request, '../templates/areaupdate.html', context)


def placemanage(request):
    context = {}
    return render(request, '../templates/placemanage.html', context)

def placeinsert(request):
    context = {}
    return render(request, '../templates/placeinsert.html', context)

def placeupdate(request):
    context = {}
    return render(request, '../templates/placeupdate.html', context)


def dayshowmanage(request):
    context = {}
    return render(request, '../templates/dayshowmanage.html', context)

def dayshowinsert(request):
    context = {}
    return render(request, '../templates/dayshowinsert.html', context)

def dayshowupdate(request):
    context = {}
    return render(request, '../templates/dayshowupdate.html', context)


def roommanage(request):
    context = {}
    return render(request, '../templates/roommanage.html', context)

def roominsert(request):
    context = {}
    return render(request, '../templates/roominsert.html', context)

def roomupdate(request):
    context = {}
    return render(request, '../templates/roomupdate.html', context)


def seatmanage(request):
    context = {}
    return render(request, '../templates/seatmanage.html', context)

def seatinsert(request):
    types = [t.value for t in ChoiceTypeSeat]
    kinds = [k.value for k in ChoiceKindSeat]
    context = {
        'types': types,
        'kinds': kinds,
    }
    return render(request, '../templates/seatinsert.html', context)

def seatupdate(request):
    types = [t.value for t in ChoiceTypeSeat]
    kinds = [k.value for k in ChoiceKindSeat]
    context = {
        'types': types,
        'kinds': kinds,
    }
    return render(request, '../templates/seatupdate.html', context)



def imagemanage(request):
    context = {}
    return render(request, '../templates/imagemanage.html', context)

def imageinsert(request):
    context = {}
    return render(request, '../templates/imageinsert.html', context)

def imageupdate(request):
    context = {}
    return render(request, '../templates/imageupdate.html', context)


def videomanage(request):
    context = {}
    return render(request, '../templates/videomanage.html', context)

def videoinsert(request):
    video_types = [v.value for v in ChoiceVideoType]
    context = {
        'video_types': video_types,
    }
    return render(request, '../templates/videoinsert.html', context)

def videoupdate(request):
    video_types = [v.value for v in ChoiceVideoType]
    context = {
        'video_types': video_types,
    }
    return render(request, '../templates/videoupdate.html', context)


def ticketmanage(request):
    context = {}
    return render(request, '../templates/ticketmanage.html', context)

def ticketinsert(request):
    types = [t.value for t in ChoiceTypeTicket]
    context = {
        'types': types,
    }
    return render(request, '../templates/ticketinsert.html', context)

def ticketupdate(request):
    types = [t.value for t in ChoiceTypeTicket]
    context = {
        'types': types,
    }
    return render(request, '../templates/ticketupdate.html', context)


def actormanage(request):
    context = {}
    return render(request, '../templates/actormanage.html', context)

def actorinsert(request):
    context = {}
    return render(request, '../templates/actorinsert.html', context)

def actorupdate(request):
    context = {}
    return render(request, '../templates/actorupdate.html', context)


def categorymanage(request):
    context = {}
    return render(request, '../templates/categorymanage.html', context)

def categoryinsert(request):
    context = {}
    return render(request, '../templates/categoryinsert.html', context)

def categoryupdate(request):
    context = {}
    return render(request, '../templates/categoryupdate.html', context)


def categoryfilmmanage(request):
    context = {}
    return render(request, '../templates/categoryfilmmanage.html', context)

def categoryfilminsert(request):
    context = {}
    return render(request, '../templates/categoryfilminsert.html', context)

def categoryfilmupdate(request):
    context = {}
    return render(request, '../templates/categoryfilmupdate.html', context)


def bookingmanage(request):
    context = {}
    return render(request, '../templates/bookingmanage.html', context)

def bookinginsert(request):
    context = {}
    return render(request, '../templates/bookinginsert.html', context)

def bookingupdate(request):
    context = {}
    return render(request, '../templates/bookingupdate.html', context)


def promotionmanage(request):
    context = {}
    return render(request, '../templates/promotionmanage.html', context)

def promotioninsert(request):
    context = {}
    return render(request, '../templates/promotioninsert.html', context)

def promotionupdate(request):
    context = {}
    return render(request, '../templates/promotionupdate.html', context)



def servicemanage(request):
    context = {}
    return render(request, '../templates/servicemanage.html', context)

def serviceinsert(request):
    context = {}
    return render(request, '../templates/serviceinsert.html', context)

def serviceupdate(request):
    context = {}
    return render(request, '../templates/serviceupdate.html', context)



def contactmanage(request):
    context = {}
    return render(request, '../templates/contactmanage.html', context)

def contactinsert(request):
    context = {}
    return render(request, '../templates/contactinsert.html', context)

def contactupdate(request):
    context = {}
    return render(request, '../templates/contactupdate.html', context)



def register(request):
    context = {}
    return render(request, '../templates/register.html', context)

def login(request):
    context = {}
    return render(request, '../templates/login.html', context)

def home(request):
    context = {}
    return render(request, '../templates/home.html', context)

def base(request):
    context = {}
    return render(request, '../templates/base.html', context)



def homepage(request):
    context = {}
    return render(request, '../templates/homepage.html', context)

def promotionlist(request):
    context = {}
    return render(request, '../templates/promotionlist.html', context)

def promotion(request, id):
    promotion_object = Promotion.objects.get(id=id)
    
    return render(request, '../templates/promotion.html', {'promotion': promotion_object})

def film(request, id):
    film_object = Films.objects.get(id=id)
    
    return render(request, '../templates/film.html', {'film': film_object})

def bookfilm(request, id):
    book_film_object = Films.objects.get(id=id)
    return render(request, '../templates/bookfilm.html', {'bookfilm': book_film_object})

def bookcombo(request, id):
    book_combo_object = Bookings.objects.get(id=id)
    return render(request, '../templates/bookcombo.html', {'bookcombo': book_combo_object})


def area(request):
    context = {}
    return render(request, '../templates/area.html', context)

def room(request,id):
    schedule_object = Schedules.objects.get(id=id)
    return render(request, '../templates/room.html', {'room': schedule_object})

def contact(request):
    context = {}
    return render(request, '../templates/contact.html', context)

def booking(request, id):
    booking_object = Bookings.objects.get(id=id)
    return render(request, '../templates/booking.html', {'booking': booking_object})

def bill(request, id):
    bill_object = Pay.objects.get(id=id)
    return render(request, '../templates/bill.html', {'bill': bill_object})

def listticket(request, id):
    listticket_object = User.objects.get(id=id)
    return render(request, '../templates/listticket.html', {'listticket': listticket_object})

class BackgroundViewSet(ModelViewSet):
    model = Background
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = BackgroundFilterSet
    ordering_fields = ("id","name")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)

class LogoViewSet(ModelViewSet):
    model = Logo
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = LogoFilterSet
    ordering_fields = ("id","name")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)

class PayViewSet(ModelViewSet):
    model = Pay
    queryset = Pay.objects.all()
    serializer_class = PaySerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = PayFilterSet
    ordering_fields = ("id","booking","status","schedule","total_amount" )
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)
        

class BillViewSet(ModelViewSet):
    model = Bill
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = BillFilterSet
    ordering_fields = ("id","pay","user","status")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user, user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)


class UserProfileViewSet(ModelViewSet):
    model = UserProfile
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = UserProfileFilterSet
    ordering_fields = ("id","user","gender","phone","address")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user,user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)



class BookingViewSet(ModelViewSet):
    model = Bookings
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = BookingFilterSet
    ordering_fields = ("id","user",)
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user,user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)
    
class BookingDetailViewSet(ModelViewSet):
    model = BookingDetail
    queryset = BookingDetail.objects.all()
    serializer_class = BookingDetailSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = BookingDetailFilterSet
    ordering_fields = ("id","booking","ticket","seat",)
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)

class SeatViewSet(ModelViewSet):
    model = Seats
    queryset = Seats.objects.all()
    serializer_class = SeatSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = SeatFilterSet
    ordering_fields = ("id","name","room","type","kind")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)
    

class TicketViewSet(ModelViewSet):
    model = Tickets
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = TicketFilterSet
    ordering_fields = ("id","price","schedule","type",)
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)

    
class RoomViewSet(ModelViewSet):
    model = Rooms
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = RoomFilterSet
    ordering_fields = ("id","name",)
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)


class DayShowViewSet(ModelViewSet):
    model = DayShow
    queryset = DayShow.objects.all()
    serializer_class = DayShowSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = DayShowFilterSet
    ordering_fields = ("id","place","day",)
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)

class FilmViewSet(ModelViewSet):
    model = Films
    queryset = Films.objects.all()
    serializer_class = FilmSerializer
    pagination_class = StandardPagination
    # permission_classes = [AccessTokenPermission]
    
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = FilmFilterSet
    ordering_fields = ("id","name","producer","duration","description", "country","imdb","age","view","created_at")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)
    
class ImageViewSet(ModelViewSet):
    model = Image
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = ImageFilterSet
    ordering_fields = ("id","film",)
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)
    
class VideoViewSet(ModelViewSet):
    model = Video
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = VideoFilterSet
    ordering_fields = ("id","film","video_type",)
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)
    
class CategoryViewSet(ModelViewSet):
    model = Categories
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = CategoryFilterSet
    ordering_fields = ("id","name",)
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)

class CategoryFilmViewSet(ModelViewSet):
    model = CategoryFilm
    queryset = CategoryFilm.objects.all()
    serializer_class = CategoryFilmSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = CategoryFilmFilterSet
    ordering_fields = ("id","category","film",)
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)
        
        
class ActorViewSet(ModelViewSet):
    model = Actors
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = ActorFilterSet
    ordering_fields = ("id","name","description","film",)
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)

class CommentViewSet(ModelViewSet):
    model = Comments
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    pagination_class = StandardPagination
    # permission_classes = [AccessTokenPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = CommentFilterSet
    ordering_fields = ("id","user", "film", "rate","created_at")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user, user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)

class ComboViewSet(ModelViewSet):
    model = Combo
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = ComboFilterSet
    ordering_fields = ("id","name", "price")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)
        
class ComboDetailViewSet(ModelViewSet):
    model = ComboDetail
    queryset = ComboDetail.objects.all()
    serializer_class = ComboDetailSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = ComboDetailFilterSet
    ordering_fields = ("id","booking", "combo")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)
        

class ServiceViewSet(ModelViewSet):
    model = Service
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = ServiceFilterSet
    ordering_fields = ("id","name","title","description")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)

class ContactViewSet(ModelViewSet):
    model = Contact
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = StandardPagination
    # permission_classes = (IsAuthenticated,)
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = ContactFilterSet
    ordering_fields = ("id","name","phone","email","service","area","place")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)

class ScheduleViewSet(ModelViewSet):
    model = Schedules
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = ScheduleFilterSet
    ordering_fields = ("id","film","room","start_time","end_time", "status",)
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)
   
class PromotionViewSet(ModelViewSet):
    model = Promotion
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = PromotionFilterSet
    ordering_fields = ("id","name", "created_at")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)


class AreaViewSet(ModelViewSet):
    model = Area
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = AreaFilterSet
    ordering_fields = ("id","name",)
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)


class PlaceViewSet(ModelViewSet):
    model = Place
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = PlaceFilterSet
    ordering_fields = ("id","name","address")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)


class BulkEditObjectsView(APIView):
    permission_classes = [AdminPermission]
    serializer_class = BulkEditObjectsSerializer
    parser_classes = [parsers.JSONParser]
    
    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        object_type = serializer.validated_data.get("object_type")
        object_ids = serializer.validated_data.get("objects")
        object_class = serializer.get_object_class(object_type)
        operation = serializer.validated_data.get("operation")

        objs = object_class.objects.filter(pk__in=object_ids)
        
        
        if operation == "update" and object_type == "users":
            for user_id in object_ids:
                user = User.objects.get(id=user_id)
                user.is_active = serializer.validated_data.get("is_active", user.is_active)
                user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
                       
        elif operation == "delete":
            objs.delete()

        return Response({"result": "OK"}, status=status.HTTP_200_OK)

