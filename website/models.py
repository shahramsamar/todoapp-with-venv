from django.db import models


# Create your models here.
class BasicInformationModel(models.Model):
    about = models.TextField()
    age = models.PositiveIntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    
    
    def __str__(self):
        return f"BasicInfo {self.id}"
    
    class Meta:
        ordering = ['id']

class  SkillModel(models.Model):
    title = models.CharField(max_length=255)   
    level = models.PositiveBigIntegerField(default=50)  
    
    
    def __str__(self):
        return self.title    
    
    
class PhotoModel(models.Model):
    title = models.CharField(max_length=255,null=True)   
    image = models.ImageField(upload_to='photos/')
    
    
    # def __str__(self):
    #     return self.image  