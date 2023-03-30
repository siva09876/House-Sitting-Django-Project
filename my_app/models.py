from django.contrib.auth.models import AbstractUser
from django.db import models



class MyUser(AbstractUser):
    email= models.EmailField(unique=True,primary_key=True,max_length=225)
    first_name=models.CharField(null=True,max_length=100)
    last_name=models.CharField(null=True,max_length=100)
    staff_address=models.CharField(null=True,max_length=100)
    staff_phone_number=models.IntegerField(null=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    def __str__(self) -> str:
        return self.username
    
class Resgistration(models.Model):
    STATUS=(
        ('Alloted','Alloted'),
        ('Not Alloted','Not Alloted')
    )
    username=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    #registration1
    fullname=models.CharField(max_length=100,null=True)
    age=models.CharField(max_length=10,null=True)
    house_type=models.CharField(max_length=20,null=True)
    gender=models.CharField(max_length=20,null=True)
    phone_number=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    house_sitter_gender=models.CharField(max_length=10,null=True)

    # registration2

    starting_date=models.CharField(max_length=10,null=True)
    ending_date=models.CharField(max_length=10,null=True)
    age_for_sitter=models.CharField(max_length=10,null=True)
    country_visit=models.CharField(max_length=100,null=True)
    staying_in_house=models.CharField(max_length=100,null=True)
    to_appoint=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=300,null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    pincode=models.CharField(max_length=6,null=True)
    instructions=models.CharField(max_length=1000,null=True)
    sitter_allotment=models.CharField(max_length=100,null=True,choices=STATUS,default="Not Alloted")


    def __str__(self):
        return self.fullname
    
    def get_absolute_url(self):
        return "/registration2/%i/"%self.id


    

