from django.db import models
from django.utils import timezone


class CustomUser(models.Model):
	user_id = models.AutoField(primary_key=True) 
	name = models.CharField(max_length=200)
	nick_name = models.CharField(max_length=200, blank=True)
	email = models.EmailField(max_length=254)
	is_admin = models.BooleanField(default=False)

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
	        default=timezone.now)
	published_date = models.DateTimeField(
	        blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title
class Comment(models.Model):
	post_id = models.ForeignKey(Post, related_name='post_id',on_delete=models.CASCADE)
	author = models.ForeignKey(CustomUser, related_name='author', on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(
	        default=timezone.now)

class Message(models.Model):
	sender = models.ForeignKey(CustomUser, related_name='sender',on_delete=models.CASCADE) 
	receiver = models.ForeignKey(CustomUser, related_name='receiver',on_delete=models.CASCADE)
	text = models.TextField(blank=True)
	created_date = models.DateTimeField(
	        default=timezone.now)

	
	 
