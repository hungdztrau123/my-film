from django_filters.rest_framework import Filter
from django_filters.rest_framework import FilterSet

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



CHAR_KWARGS = ["istartswith", "iendswith", "icontains", "iexact", "in"]
ID_KWARGS = ["in", "exact"]
INT_KWARGS = ["exact", "gt", "gte", "lt", "lte", "isnull"]
DATE_KWARGS = ["year", "month", "day", "date__gt", "gt", "date__lt", "lt"]
BOOL_KWARGS = ["exact"]


class DayShowFilterSet(FilterSet):
    class Meta:
        model = DayShow
        fields = {
            "id": ID_KWARGS,
            "place": ID_KWARGS,
            "day": DATE_KWARGS,
        }

class FilmFilterSet(FilterSet):
    class Meta:
        model = Films
        fields = {
            "id": ID_KWARGS,
            "name": CHAR_KWARGS,
            "imdb": CHAR_KWARGS,
            "age": CHAR_KWARGS,
            "view": CHAR_KWARGS,
            "producer": CHAR_KWARGS,
            "duration": CHAR_KWARGS,
            "release": DATE_KWARGS,
            "description": CHAR_KWARGS,
            "country": CHAR_KWARGS,
            "dayshow": ID_KWARGS,
            "place": ID_KWARGS,
            "status": CHAR_KWARGS,
            
        }

class ImageFilterSet(FilterSet):
    class Meta:
        model = Image
        fields = {
            "id": ID_KWARGS,
            "film": ID_KWARGS,
        }    
class VideoFilterSet(FilterSet):
    class Meta:
        model = Video
        fields = {
            "id": ID_KWARGS,
            "film": ID_KWARGS,
            "video_type": CHAR_KWARGS,
        }       
        
class CategoryFilterSet(FilterSet):
    class Meta:
        model = Categories
        fields = {
            "id": ID_KWARGS,
            "name": CHAR_KWARGS,
        }   

class CategoryFilmFilterSet(FilterSet):
    class Meta:
        model = CategoryFilm
        fields = {
            "id": ID_KWARGS,
            "category": ID_KWARGS,
            "film": ID_KWARGS,
        }      

class CommentFilterSet(FilterSet):
    class Meta:
        model = Comments
        fields = {
            "id": ID_KWARGS,
            "user": ID_KWARGS,
            "film": ID_KWARGS,
            "rate": CHAR_KWARGS,
        }    
        
class ComboFilterSet(FilterSet):
    class Meta:
        model = Combo
        fields = {
            "id": ID_KWARGS,
            "name": CHAR_KWARGS,
            "price": CHAR_KWARGS,
        }   


class ServiceFilterSet(FilterSet):
    class Meta:
        model = Service
        fields = {
            "id": ID_KWARGS,
            "name": CHAR_KWARGS,
            "title": CHAR_KWARGS,
            "description": CHAR_KWARGS,
        }     
        
class ContactFilterSet(FilterSet):
    class Meta:
        model = Contact
        fields = {
            "id": ID_KWARGS,
            "name": CHAR_KWARGS,
            "phone": CHAR_KWARGS,
            "email": CHAR_KWARGS,
            "service": ID_KWARGS,
            "area": ID_KWARGS,
            "place": ID_KWARGS,
        }     

class ScheduleFilterSet(FilterSet):
    class Meta:
        model = Schedules
        fields = {
            "id": ID_KWARGS,
            "film": ID_KWARGS,
            "dayshow": ID_KWARGS,
            "place": ID_KWARGS,
            "room": ID_KWARGS,
            "start_time": DATE_KWARGS,
            "end_time": DATE_KWARGS,
        }
        
class RoomFilterSet(FilterSet):
    class Meta:
        model = Rooms
        fields = {
            "id": ID_KWARGS,
            "name": CHAR_KWARGS,
            "place": ID_KWARGS,
        }
        
class SeatFilterSet(FilterSet):
    class Meta:
        model = Seats
        fields = {
            "id": ID_KWARGS,
            "room": ID_KWARGS,
            "name": CHAR_KWARGS,
            "type": CHAR_KWARGS,
            "kind": CHAR_KWARGS,
            "status": BOOL_KWARGS,
        }

class TicketFilterSet(FilterSet):
    class Meta:
        model = Tickets
        fields = {
            "id": ID_KWARGS,
            "price": CHAR_KWARGS,
            "schedule": ID_KWARGS,
            "type": CHAR_KWARGS,
        }
        
class BookingFilterSet(FilterSet):
    class Meta:
        model = Bookings
        fields = {
            "id": ID_KWARGS,
            "user": ID_KWARGS,
        }
     
class BookingDetailFilterSet(FilterSet):
    class Meta:
        model = BookingDetail
        fields = {
            "id": ID_KWARGS,
            "booking": ID_KWARGS,
            "ticket": ID_KWARGS,
            "seat": ID_KWARGS,
            
        }
   
class PromotionFilterSet(FilterSet):
    class Meta:
        model = Promotion
        fields = {
            "id": ID_KWARGS,
            "name": CHAR_KWARGS,
        }

class AreaFilterSet(FilterSet):
    class Meta:
        model = Area
        fields = {
            "id": ID_KWARGS,
            "name": CHAR_KWARGS,
        }
     
class PlaceFilterSet(FilterSet):
    class Meta:
        model = Place
        fields = {
            "id": ID_KWARGS,
            "name": CHAR_KWARGS,
            "area": ID_KWARGS,
        }