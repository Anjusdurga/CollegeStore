
from django.db import models
from django.urls import reverse


# Create your models here.
class Departments(models.Model):
    name=models.CharField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'


    def __str__(self):
        return '{}'.format(self.name)

class Courses(models.Model):
    name=models.CharField(max_length=250,unique=True)
    # slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)

    department=models.ForeignKey(Departments,related_name="course",on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'course'



    def __str__(self):
        return '{}'.format(self.name)

class Purposes(models.Model):
    name=models.CharField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)

class Materials(models.Model):
    name=models.CharField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)

class Order(models.Model):

    name=models.CharField(max_length=250,null=True)
    # slug=models.SlugField(max_length=250,unique=True)

    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=250,null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)

    email = models.TextField(max_length=100)
    address = models.TextField(max_length=250)
    department= models.CharField(max_length=250,null=True)
    course = models.CharField(max_length=250,null=True)
    purpose =models.CharField(max_length=250,null=True, blank=True)
    materials = models.CharField(max_length=250,null=True, blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'order'
    def __str__(self):
        return '{}'.format(self.name)


