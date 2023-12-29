from django.db import models

# Create your models here.
class Recipe(models.Model):
    id=models.AutoField(primary_key=True)
    Recipe_name=models.CharField(max_length=20)
    Recipe_discription=models.TextField()
    Recipe_image=models.ImageField(upload_to="public")
