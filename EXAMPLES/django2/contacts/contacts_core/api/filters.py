from django_filters import rest_framework as filters
from contacts_core.models import City, Contact


class ContactFilterSet(filters.FilterSet):
     firstname = filters.CharFilter(field_name="first_name", lookup_expr='icontains')
     lastname = filters.CharFilter(field_name="last_name", lookup_expr='icontains')
     mindob = filters.NumberFilter(field_name="dob", lookup_expr='gte')
     maxdob = filters.NumberFilter(field_name="dob", lookup_expr='lte')
     postcode = filters.CharFilter(field_name="postcode", lookup_expr='icontains')
     city = filters.CharFilter(field_name='city', lookup_expr='name__icontains')
     country = filters.CharFilter(field_name='city', lookup_expr='country__icontains')


     class Meta:
         model = Contact
         fields = ["firstname", "lastname", "mindob", "maxdob", "postcode", "city", "country"]


class CityFilterSet(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    stateorprovince = filters.CharFilter(field_name="admindiv", lookup_expr='icontains')
    country = filters.CharFilter(field_name="country", lookup_expr='icontains')

    class Meta:
        model = City
        fields = ["name", "stateorprovince", "country"]
