from django.urls import path, include
from .views import Indexing, RegisterClassesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Register_Datas', RegisterClassesViewSet, basename='Register_Datas')

urlpatterns = [
    path('Urls/', include(router.urls)),
    path('', Indexing),
]