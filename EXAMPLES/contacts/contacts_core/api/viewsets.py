from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from contacts_core.models import Contact, City
from contacts_core.api.serializers import ContactSerializer, CitySerializer
from contacts_core.api.filters import ContactFilter, CityFilter

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContactFilter


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CityFilter

