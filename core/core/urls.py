from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from server.views import ServerListViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('api/server/select', ServerListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/docs/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/schema/ui/", SpectacularSwaggerView.as_view()),
    path('', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
