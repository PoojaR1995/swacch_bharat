# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your models here.
from django.db import models# for creating database

import uuid

#Create your models here.

# this form is used for sign_up
class UserModel(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=120)
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=40)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

#for session token  which is used for genrating token for the identification
class SessionToken(models.Model):
	user = models.ForeignKey(UserModel)
	session_token = models.CharField(max_length=255)
	last_request_on = models.DateTimeField(auto_now=True)
	created_on = models.DateTimeField(auto_now_add=True)
	is_valid = models.BooleanField(default=True)

	def create_token(self):
		self.session_token = uuid.uuid4()

#for posting photos
class PostModel(models.Model):
	user = models.ForeignKey(UserModel)
	image = models.FileField(upload_to='user_images')
	image_url = models.CharField(max_length=255)
	caption = models.CharField(max_length=240)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	has_liked = False

# if user wants to like hie or her own post
	@property
	def like_count(self):
		return len(LikeModel.objects.filter(post=self))
# if any other comments on the users post then this funtion helps for the odering of the comment
	@property
	def comments(self):
		return CommentModel.objects.filter(post=self).order_by('-created_on')

#for the like purpose
class LikeModel(models.Model):
	user = models.ForeignKey(UserModel)
	post = models.ForeignKey(PostModel)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
# one click on the 'like' button likes if we click again on like this shows the unlike action

#for the comments on the post
class CommentModel(models.Model):
	user = models.ForeignKey(UserModel)
	post = models.ForeignKey(PostModel)
	comment_text = models.CharField(max_length=555)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

#for the categorization of the images in feed
class CategoryModel(models.Model):
   user = models.ForeignKey(UserModel)
   post = models.ForeignKey(PostModel)
   category_text = models.CharField(max_length=255)


   @property
   def category(self):
      return CategoryModel.objects.filter(post=self)