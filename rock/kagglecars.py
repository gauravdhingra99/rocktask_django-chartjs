from models import *
import csv
with open('/home/gaurav/Desktop/rockassign/rock/cars.csv',"rt", encoding='cp1252') as f:
         reader = csv.reader(f)
         for row in reader:
         	print(row[1].strip(),row[2].strip(),row[3].strip(),
                 row[4].strip(),row[5].strip(),row[6].strip(),row[7].strip())
         	_, created = Cars.objects.get_or_create(
         		mpg=row[0].strip(),
                cylinders=row[1].strip(),
                cubicinches=row[2].strip(),
                hp=row[3].strip(),
                weightlbs=row[4].strip(), 
                timeto60=row[5].strip(),
                year=row[6].strip(),
                brand=row[7].strip(),
                )

