from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class CarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cars
		fields = "__all__"

