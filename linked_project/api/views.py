from rest_framework import generics, viewsets

from custom_urls.models import URLS, EmergencyName, EmergencyPhoneNumbers
from .serializers import URLSSerializer, EmergencyNameSerializer, EmergencyPhoneNumbersSerializer

class URLSAPIView(generics.ListAPIView):
    queryset = URLS.objects.all()
    serializer_class = URLSSerializer

class PostURLSSet(viewsets.ModelViewSet):
    queryset = URLS.objects.all()
    serializer_class = URLSSerializer

class EmergencyNameAPIView(generics.ListAPIView):
    queryset = EmergencyName.objects.all()
    serializer_class = EmergencyNameSerializer

class PostEmergencyNameSet(viewsets.ModelViewSet):
    queryset = EmergencyName.objects.all()
    serializer_class = EmergencyNameSerializer

class EmergencyPhoneNumbersAPIView(generics.ListAPIView):
    queryset = EmergencyPhoneNumbers.objects.all()
    serializer_class = EmergencyPhoneNumbersSerializer

class PostEmergencyPhoneNumbersSet(viewsets.ModelViewSet):
    queryset = EmergencyPhoneNumbers.objects.all()
    serializer_class = EmergencyPhoneNumbersSerializer