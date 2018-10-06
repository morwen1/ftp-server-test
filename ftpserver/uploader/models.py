from django.db import models



class Uploader(models.Model):
	filename = models.CharField(max_length=100)
	docfile = models.FileField(upload_to = 'documets/%Y/%m/%d')

# Create your models here.
