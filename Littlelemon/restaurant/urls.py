from django.urls import path,include
from .views import MenuSerializerView,MenuSingleView,BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables',BookingViewSet)



urlpatterns = [
    path('menu/',MenuSerializerView.as_view(),name='menu'),
    path('menu/<int:pk>/',MenuSingleView.as_view(),name='menu-detail'),
    path('restaurant/booking/',include(router.urls))
]
