from django.views.generic import View

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')

class Get_car_data(APIView):
	def get(self,request):
		cars=Cars.objects.all()
		labels=[]
		mpg=[]
		i=0
		while(i<cars.count()):
			labels.append(cars[i].brand)
			i=i+1
		i=0
		while(i<cars.count()):
			mpg.append(cars[i].mpg)
			i=i+1

		# labels=list(set(labels))
		# year=list(set(year))
		print(mpg)
		# serializer = CarSerializer(cars, many=True)
		# data=serializer.data
		# print(data)

		data = {"labels": labels,
		 		 "data": mpg,}


		return Response(data)



