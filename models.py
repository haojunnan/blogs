from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogPost(models.Model):
	title = models.TextField()	
	date_add = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.title
class MainContents(models.Model):
	blog = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
	text = models.CharField(max_length=50)
	date_add = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	class Meta:
		verbose_name_plural = 'contents'
	def __str__(self):
		return self.text

