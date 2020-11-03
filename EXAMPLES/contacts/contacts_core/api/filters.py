from django_filters import rest_framework as filters
from contacts_core.models import Contact, City

class ContactFilter(filters.FilterSet):
    firstname = filters.CharFilter(field_name="first_name", lookup_expr='icontains')
    lastname = filters.CharFilter(field_name="last_name", lookup_expr='icontains')
    address = filters.CharFilter(field_name="street_address", lookup_expr='icontains')
    city = filters.CharFilter(field_name="city", lookup_expr="name__icontains")
    country = filters.CharFilter(field_name="city", lookup_expr="country__icontains")

    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "address", "city", "country"]

class CityFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    state_or_province = filters.CharFilter(field_name="admindiv", lookup_expr='icontains')
    country = filters.CharFilter(field_name="country", lookup_expr='icontains')

    class Meta:
        model = City
        fields = ["name", "state_or_province", "country"]
