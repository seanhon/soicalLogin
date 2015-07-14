#from django.shortcuts import render
from beers.models import Beer
from beers.serializer import BeerSerializer
from rest_framework import generics, permissions

#List our beers and add beers
class BeerList(generics.ListCreateAPIView):
	#queryset = Beer.objects.all()
	#serializer_class = BeerSerializer

	serializer_class = BeerSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		user = self.request.user
		return Beer.objects.filter(owner=user)


	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

#Get a beer and remove a beer
class BeerDetail(generics.RetrieveDestroyAPIView):
	#queryset = Beer.objects.all()
	#serializer_class = BeerSerializer

	serializer_class = BeerSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		user = self.request.user
		return Beer.objects.filter(owner=user)


