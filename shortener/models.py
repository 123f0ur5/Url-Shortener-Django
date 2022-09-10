from django.db import models
import datetime

# Create your models here.
class Url(models.Model):
	identifier 		= models.CharField(max_length=5, unique=True)
	original_link	= models.TextField()
	creation_date	= models.DateField(default=datetime.date.today)