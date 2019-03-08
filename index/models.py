from django.db import models

# Create your models here.
class Tags(models.Model):
	tag1 = models.CharField(max_length = 66)
	tag2 = models.CharField(max_length = 66)