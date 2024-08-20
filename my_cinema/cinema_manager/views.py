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
    
    # def perform_create(self, serializer):
    #     serializer.save(create_by=self.request.user,user=self.request.user)
    # def perform_update(self, serializer):
    #     serializer.save(editor=self.request.user)
    
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

class FilmViewSet(ModelViewSet):
    model = Films
    queryset = Films.objects.all()
    serializer_class = FilmSerializer
    pagination_class = StandardPagination
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = FilmFilterSet
    ordering_fields = ("id","name","producer","duration","description", "country","imdb","age","view")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
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

class CommentViewSet(ModelViewSet):
    model = Comments
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    pagination_class = StandardPagination
    permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = CommentFilterSet
    ordering_fields = ("id","user", "film", "rate", )
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]

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

class ContactViewSet(ModelViewSet):
    model = Contact
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = StandardPagination
    permission_classes = (IsAuthenticated,)
    # permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = ContactFilterSet
    ordering_fields = ("id","name","phone","email","service","area","place")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    # def perform_create(self, serializer):
    #     serializer.save(create_by=self.request.user)
    # def perform_update(self, serializer):
    #     serializer.save(editor=self.request.user)

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
    ordering_fields = ("id","film","room","start_time","end_time")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
   
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
    ordering_fields = ("id","name")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]


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

