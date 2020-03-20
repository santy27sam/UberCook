from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES = (
	("1","MALE"),
	("2","FEMALE"),
	("3","OTHERS"),
	)
class Profile(models.Model):
	user		= models.OneToOneField(User, on_delete=models.CASCADE)
	firstname 	= models.TextField()
	lastname 	= models.TextField()
	Designation = models.TextField()
	Age			= models.IntegerField()
	Sex			= models.CharField(max_length = 30, choices = GENDER_CHOICES, default = '1' )

	def __str__(self):
		return f'{self.user.username}'
