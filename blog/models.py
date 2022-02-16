from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
# post table

class Post(models.Model):
	#table fields title maxlegth 100
	title=models.CharField(max_length=100)
	content=models.TextField()
#post created time
	#date_posted=models.DateTimeField(auto_now=True)
#only when the object is created
	#date_posted=models.DateTimeField(auto_now_add=True)
	date_posted=models.DateTimeField(default=timezone.now)
	#author is user in seperate table user ----> multiple post
	author=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title