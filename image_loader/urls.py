from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'image_loader'

router = DefaultRouter()
router.register('image', viewset=views.ImageViewSet, basename='image')


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('image_load/', views.ImageLoadView.as_view(), name='image_load'),
    path('create_image/', views.ImageCreateView.as_view()),
    path('api/', include(router.urls)),
]