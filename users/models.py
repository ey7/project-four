from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
	avatar = CloudinaryField('avatar')
	user = models.OneToOneField(User, on_delete=models.CASCADE,
		related_name='user_profile')


