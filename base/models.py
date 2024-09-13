from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# from shop.views import index
# from django.db import models

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=200)
    cateegory=models.CharField(max_length=200)
    description=models.TextField()

    
    def __str__(self):
        return self.title

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    # status=models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'user'


class News(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    geeks_field = models.URLField(max_length = 200, 
        db_index=True, 
        unique=True, 
        blank=True)
    def __str__(self):
        return self.title
    
class FilesUpload(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)  
    file=models.FileField()
    
    # def __str__(self):
    #  return self.user
    
class Sts(models.Model):
    STATUS = (
			('in Stage 1', 'in Stage 1'),
            ('in Stage 2', 'in Stage 2'),
            ('in Stage 3', 'in Stage 3'),
			('Accepted', 'Accepted'),
			('Rejected', 'Rejected'),
			)
    user_id = models.OneToOneField(
        User, on_delete=models.CASCADE)
    
    status = models.CharField(max_length=200, null=True, choices=STATUS,default="in Stage 0")
    desc=models.TextField(default="Your Application is being Reviewed")
    # def __str__(self):
    #  return self.user_id    

class TueForm(models.Model):
    CHOICES = (
			('Yes', 'Yes'),
            ('No','No'),
			)
    SEX=(
        ('Male','Male'),
        ('Female','Female'),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    fname=models.CharField(max_length=30,null=True,default="user")
    dob=models.DateField( null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    phone=models.CharField(max_length=10, null=True, blank=True)
    gender=models.CharField(max_length=7, null=True, choices=SEX,default="none")
    sport=models.CharField(max_length=10, null=True, blank=True)
    id_type=models.CharField(max_length=10, null=True, blank=True)
    id_no=models.CharField(max_length=10, null=True, blank=True)
    name_on_id=models.CharField(max_length=10, null=True, blank=True)
    addType=models.CharField(max_length=10, null=True, blank=True)
    nationality=models.CharField(max_length=10, null=True, blank=True)
    state=models.CharField(max_length=10, null=True, blank=True)
    district=models.CharField(max_length=10, null=True, blank=True)
    city=models.CharField(max_length=10, null=True, blank=True)
    postal_code=models.CharField(max_length=10, null=True, blank=True)
    
    select1=models.CharField(max_length=4, null=True, blank=True)
    text1=models.CharField(max_length=10, null=True, blank=True)
    text2=models.CharField(max_length=10, null=True, blank=True)
    text3=models.CharField(max_length=10, null=True, blank=True)
    select2=models.CharField(max_length=4, null=True, blank=True)
    text4=models.CharField(max_length=10, null=True, blank=True)
    select3=models.CharField(max_length=4, null=True, blank=True)
    text5=models.CharField(max_length=10, null=True, blank=True)
    select4=models.CharField(max_length=4, null=True, blank=True)
    select5=models.CharField(max_length=4, null=True, blank=True)
    select6=models.CharField(max_length=4, null=True, blank=True)
    select7=models.CharField(max_length=4, null=True, blank=True)
    select8=models.CharField(max_length=4, null=True, blank=True)

    text5=models.CharField(max_length=10, null=True, blank=True)
    upload1=models.FileField( null=True, blank=True)
    text6=models.CharField(max_length=10, null=True, blank=True)
    text7=models.CharField(max_length=10, null=True, blank=True)
    text8=models.CharField(max_length=10, null=True, blank=True)
    text9=models.CharField(max_length=10, null=True, blank=True)
    text10=models.CharField(max_length=10, null=True, blank=True)
    text11=models.CharField(max_length=10, null=True, blank=True)
    text12=models.CharField(max_length=10, null=True, blank=True)
    
    physicianName=models.CharField(max_length=10, null=True, blank=True)
    text13=models.CharField(max_length=10, null=True, blank=True)
    text14=models.CharField(max_length=10, null=True, blank=True)
    text15=models.CharField(max_length=10, null=True, blank=True)
    text16=models.CharField(max_length=10, null=True, blank=True)
    text17=models.CharField(max_length=10, null=True, blank=True)
    text18=models.CharField(max_length=10, null=True, blank=True)
    text19=models.CharField(max_length=10, null=True, blank=True)
    text20=models.CharField(max_length=10, null=True, blank=True)
    text21=models.CharField(max_length=10, null=True, blank=True)
    text22=models.CharField(max_length=10, null=True, blank=True)
    upload2=models.FileField( null=True, blank=True)

    upload3=models.FileField( null=True, blank=True)
    date3=models.CharField(max_length=10, null=True, blank=True)
