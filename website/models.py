from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=100, blank=True)
    address_line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=25, blank=True)
    country = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100) 
    phone = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True)
    
    def __str__(self):
        return(f"{self.title} {self.first_name} {self.last_name} ")
    
    