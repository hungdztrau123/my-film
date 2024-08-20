
from rest_framework import serializers
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


from auth_manager.serializers import UserSerializer

from django.contrib.auth.models import User

class DayShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayShow
        fields = '__all__'

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class CategoryFilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryFilm
        fields = '__all__'
        
    def to_representation(self, instance): 
        data = super().to_representation(instance) 
        if instance.category: 
            data['category'] = CategorySerializer(instance.category).data 
        if instance.film: 
            data['film'] = FilmSerializer(instance.film).data 
        return data
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedules
        fields = '__all__'     
    
    def to_representation(self, instance): 
        data = super().to_representation(instance) 
        if instance.dayshow: 
            data['dayshow'] = DayShowSerializer(instance.dayshow).data 
        if instance.film: 
            data['film'] = FilmSerializer(instance.film).data 
        if instance.room: 
            data['room'] = RoomSerializer(instance.room).data 
        if instance.place: 
            data['place'] = PlaceSerializer(instance.place).data 
        return data   

class RoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rooms
        fields = '__all__' 
        
    def to_representation(self, instance): 
        data = super().to_representation(instance) 
        if instance.place: 
            data['place'] = PlaceSerializer(instance.place).data 
        return data       

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = '__all__'
        
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'   
    
    def to_representation(self, instance): 
        data = super().to_representation(instance) 
        if instance.schedule: 
            data['schedule'] = ScheduleSerializer(instance.schedule).data 
        return data 
    
     
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'  
        
    def to_representation(self, instance): 
        data = super().to_representation(instance) 
        if instance.user: 
            data['user'] = UserSerializer(instance.user).data 
    
        return data  

class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingDetail
        fields = '__all__'
    def to_representation(self, instance): 
        data = super().to_representation(instance) 
        if instance.ticket: 
            data['ticket'] = TicketSerializer(instance.ticket).data
        if instance.seat: 
            data['seat'] = SeatSerializer(instance.seat).data 
        return data 

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'
        
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
        

class BulkEditObjectsSerializer(serializers.Serializer):
    objects = serializers.ListField(
        required=True,
        allow_empty=False,
        label="Objects",
        write_only=True,
        child=serializers.IntegerField(),
    )
    
    is_active = serializers.BooleanField(
        required=False,
        allow_null=True,
        label="Is Active",
        write_only=True,
        default=True
    )

    object_type = serializers.ChoiceField(
        choices=[
            "films",
            "promotions",
            "users",
            "contacts",
            "seats",
            "bookingdetails",
            "bookings",
            
            
        ],
        label="Object Type",
        write_only=True,
    )

    operation = serializers.ChoiceField(
        choices=[
            "delete",
            "update",
        ],
        label="Operation",
        required=True,
        write_only=True,
    )


    def get_object_class(self, object_type):
        object_class = None
        if object_type == "films":
            object_class = Films
        elif object_type == "promotions":
            object_class = Promotion
        elif object_type == "contacts":
            object_class = Contact
        elif object_type == "seats":
            object_class = Seats
        elif object_type == "bookingdetails":
            object_class = BookingDetail
        elif object_type == "bookings":
            object_class = Bookings
        elif object_type == "users":
            object_class = User
        
        return object_class

    def _validate_objects(self, objects, object_type):
        if not isinstance(objects, list):
            raise serializers.ValidationError("objects must be a list")
        if not all(isinstance(i, int) for i in objects):
            raise serializers.ValidationError("objects must be a list of integers")
        object_class = self.get_object_class(object_type)
        count = object_class.objects.filter(id__in=objects).count()
        if not count == len(objects):
            raise serializers.ValidationError(
                "Some ids in objects don't exist or were specified twice.",
            )
        return objects
    def _validate_is_active(self, is_active):
        
        if is_active is not None and not isinstance(is_active, bool):
            raise serializers.ValidationError("The `is_active` field must be a boolean value.")
        return is_active
    
    def validate(self, attrs):
        object_type = attrs["object_type"]
        is_active = attrs["is_active"]
        objects = attrs["objects"]

        self._validate_objects(objects, object_type)
        self._validate_is_active(is_active)

        return attrs