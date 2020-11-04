from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from presidents_core.models import Presidents
from presidents_core.api.serializers import PresidentsSerializer

# Create your viewsets here.
#
# examples:
#

class CommonPageLimits:
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class PresidentsLimitPagination(CommonPageLimits, LimitOffsetPagination):
    pass

class PresidentsPagePagination(CommonPageLimits, PageNumberPagination):
    pass

class PresidentsViewSet(viewsets.ModelViewSet):
    queryset = Presidents.objects.all()
    serializer_class = PresidentsSerializer
    pagination_class = PresidentsLimitPagination

