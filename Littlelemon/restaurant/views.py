from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,UpdateAPIView,RetrieveUpdateDestroyAPIView
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BookingViewSet(ModelViewSet):
    serializer_class =BookingSerializer
    queryset = Booking.objects.all()
    permission_classes =[IsAuthenticated]
    authentication_classes = [TokenAuthentication]




class MenuSerializerView(ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset =Menu.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes =[IsAuthenticated]
    
class MenuSingleView(RetrieveUpdateDestroyAPIView):
    permission_classes =[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class= MenuSerializer
    queryset = Menu.objects.all()
    lookup_field = "pk"
# this view for test static file
def index(request):
    return render(request,'index.html',{})