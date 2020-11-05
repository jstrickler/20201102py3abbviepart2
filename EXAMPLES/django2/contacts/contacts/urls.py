from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin', admin.site.urls),
    # path('dogs', include('contacts_core.urls', namespace="dogs_core")),
    # path('art', include('contacts_core.urls', namespace="art_core")),
    path('', include('contacts_core.urls', namespace="contacts")),
    # path('api/', include('contacts_core.api.urls', namespace='api')
    # path('apple', include('apple.urls', namespace="apple")),
    # path('banana/', include('banana.urls', namespace="banana")),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]

# include Django Debug toolbar if DEBUG is set
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns

# 3f2540e4b1bf996c396e04c5463a47e42900441a
