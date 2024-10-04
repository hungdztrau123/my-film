from django_filters.rest_framework import Filter
from django_filters.rest_framework import FilterSet
from django.contrib.auth.models import User
from cinema_manager.models import UserProfile

CHAR_KWARGS = ["istartswith", "iendswith", "icontains", "iexact"]
ID_KWARGS = ["in", "exact"]
INT_KWARGS = ["exact", "gt", "gte", "lt", "lte", "isnull"]
DATE_KWARGS = ["year", "month", "day", "date__gt", "gt", "date__lt", "lt"]
BOOL_KWARGS = ["exact"]
class UserFilterSet(FilterSet):
    class Meta:
        model = User
        fields = {
            "id": ID_KWARGS,
            "email": CHAR_KWARGS,
            "username": CHAR_KWARGS,
            "is_staff": BOOL_KWARGS,
            "is_active": BOOL_KWARGS,
        }
        
        
class UserProfileFilterSet(FilterSet):
    class Meta:
        model = UserProfile
        fields = {
            "id": ID_KWARGS,
            "user":ID_KWARGS,
            "gender": CHAR_KWARGS,
            "phone": CHAR_KWARGS,
            "address": CHAR_KWARGS,
        }