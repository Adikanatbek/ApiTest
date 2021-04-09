from django.shortcuts import render
from rest_framework import generics
from cars.serializers import *
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )



class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


