from django.db import models

# Create your models here.
class Cars(models.Model):
	mpg=models.FloatField()
	cylinders=models.FloatField()
	cubicinches=models.FloatField()
	hp=models.FloatField()
	weightlbs=models.FloatField()
	timeto60=models.FloatField()
	year=models.CharField(max_length=100)
	brand=models.CharField(max_length=100)

	def __str__(self):
		return self.brand

