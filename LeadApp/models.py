from django.db import models

# Create your models here.
class LeadModel(models.Model):
    SOURCE_CHOICES=(
        ("Walks-in","Walks-in"),
        ("call","call"),
        ("referal","refreal"),
        ("Website","Website")
    )
    STATUS_CHOICES=(
        ("New","New"),
        ("Contacted","Contacted"),
        ("Converted","Converted"),
        ("Lose","Lose")
    )
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10,unique=True)
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=100)
    source=models.CharField(max_length=100,choices=SOURCE_CHOICES)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES)
    added_date=models.DateField(auto_now=True)
    notes=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"