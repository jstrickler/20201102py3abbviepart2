from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from contacts_core.api.serializers import ContactSerializer, CitySerializer
from contacts_core.api.filters import CityFilterSet, ContactFilterSet
from contacts_core.models import Contact, City

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContactFilterSet


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CityFilterSet

