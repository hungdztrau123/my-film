import datetime
import logging
import os
import re
from collections import OrderedDict
from pathlib import Path
from typing import Final
from typing import Optional

from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from enum import Enum

# Create your models here.

class ChoiceCountries(Enum):
    america = 'America'
    vietnam = 'VietNam'
    england = 'England'

class ChoiceTypeTicket(Enum):
    regural = 'Regural'
    vip = 'Vip'
    
class ChoiceTypeSeat(Enum):
    regural = 'Regural'
    vip = 'Vip'

class ChoiceGender(Enum):
    male = 'Male'
    female = 'Female'

class ChoiceStatus(Enum):
    now = 'Now'
    comming = 'Coming'

class Base(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(default=timezone.now, db_index=True)
    create_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='%(class)s_created')
    editor = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='%(class)s_editor')
    class  Meta:
        abstract = True
        

class UserProfile(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100,choices=[(tag.value, tag.name) for tag in ChoiceGender], default=ChoiceGender.male.value )
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    

class Area(Base):
    name = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self): 
        return self.name

class Place(Base):
    name = models.CharField(max_length=255, null=True, blank=True)
    area = models.ForeignKey(Area, null=True, on_delete=models.CASCADE)
    image = models.FileField(upload_to='files/',null=True,blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self): 
        return self.name
    
class DayShow(Base):
    place = models.ManyToManyField(Place,null=True, blank=True)
    day = models.DateTimeField(null=True,blank=True)
    

class Rooms(Base):
    place = models.ForeignKey(Place, null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)

class Seats(Base):
    room = models.ForeignKey(Rooms, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True, choices=[(tag.value, tag.name) for tag in ChoiceTypeSeat], default=ChoiceTypeSeat.regural.value)
    status = models.BooleanField(default=True)

class Films(Base):
    place = models.ManyToManyField(Place,null=True, blank=True)
    dayshow = models.ManyToManyField(DayShow,null=True, blank=True)
    age = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    poster = models.FileField(upload_to='files/',null=True,blank=True)
    banner = models.FileField(upload_to='files/',null=True,blank=True)
    imdb = models.CharField(max_length=100, null=True, blank=True)
    producer = models.CharField(max_length=255, null=True,blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)
    release = models.DateTimeField(null=True, blank=True)
    view = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=100, choices=[(tag.value, tag.name) for tag in ChoiceCountries], default=ChoiceCountries.america.value )
    status = models.CharField(max_length=100, null=True, choices=[(tag.value, tag.name) for tag in ChoiceStatus], default=ChoiceStatus.now.value )

class Image(Base):
    film = models.ForeignKey(Films, null=True, on_delete=models.CASCADE)
    image = models.FileField(upload_to='files/',null=True)

class Video(Base):
    film = models.ForeignKey(Films, null=True, on_delete=models.CASCADE)
    video = models.FileField(upload_to='files/',null=True,blank=True)
    video_type = models.CharField(max_length=20, null=True, blank=True)
    
class Comments(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Films, null=True, on_delete=models.CASCADE)
    rate = models.CharField(max_length=100, null=True, blank=True)
    content = models.CharField(max_length=500, null=True, blank=True)

class Categories(Base):
    name = models.CharField(max_length=255, null=True, blank=True)

class CategoryFilm(Base):
    category = models.ForeignKey(Categories, null=True, on_delete=models.CASCADE)
    film = models.ForeignKey(Films, null=True, on_delete=models.CASCADE)


    
class Schedules(Base):
    place = models.ForeignKey(Place, null=True,on_delete=models.SET_NULL)
    dayshow = models.ForeignKey(DayShow, null=True, on_delete=models.CASCADE)
    film = models.ForeignKey(Films, null=True, blank=True, on_delete=models.SET_NULL)
    room = models.ForeignKey(Rooms, null=True, on_delete=models.CASCADE) 
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(null=True,blank=True)
    

class Tickets(Base):
    price = models.CharField(max_length=255, null=True, blank=True)
    schedule = models.ForeignKey(Schedules, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=[(tag.value, tag.name) for tag in ChoiceTypeTicket], default=ChoiceTypeTicket.regural.value)

class Actors(Base):
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to='files/',null=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    film = models.ForeignKey(Films,null=True, on_delete=models.CASCADE)

class Bookings(Base):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class BookingDetail(Base):
    booking = models.ForeignKey(Bookings,null=True, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Tickets, null=True, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seats, null=True, on_delete=models.SET_NULL)
    
class Promotion(Base):
    name = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    image = models.FileField(upload_to='files/',null=True)
    description = models.CharField(max_length=500, null=True, blank=True)

class Service(Base): 
    name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to='files/',null=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self): 
        return self.name

class Contact(Base):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    area = models.ForeignKey(Area, null=True, on_delete=models.SET_NULL)
    place = models.ForeignKey(Place,null=True, on_delete=models.SET_NULL)
    
    
class Pay(Base):
    pass
    
    

