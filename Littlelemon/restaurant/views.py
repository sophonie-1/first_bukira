from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,UpdateAPIView,RetrieveUpdateDestroyAPIView
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.viewsets import ModelViewSet


class BookingViewSet(ModelViewSet):
    serializer_class =BookingSerializer
    queryset = Booking.objects.all()




class MenuSerializerView(ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset =Menu.objects.all()
    
class MenuSingleView(RetrieveUpdateDestroyAPIView):
    serializer_class= MenuSerializer
    queryset = Menu.objects.all()
    lookup_field = "pk"
