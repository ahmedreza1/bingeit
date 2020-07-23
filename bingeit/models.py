from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator
from django.core.exceptions import PermissionDenied

# Create your models here.

# The Shows Model.
class Show(models.Model):
	title = models.CharField(max_length = 500)
	description = models.TextField(null=False, blank=False)
	poster = models.ImageField(upload_to = "image\\", null=True)
	cast = models.TextField(null=False, blank=False)
	director = models.TextField(null=False, blank=False)
	show_type = models.CharField(max_length = 200)
	cr_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "%s" % self.title

# The Episode Model.
class Episode(models.Model):
	show = models.ForeignKey(Show, related_name='episodes', on_delete=CASCADE, null=True, blank=True)
	episode = models.CharField(max_length = 800)
	def __str__(self):
		return "%s" % self.episode

# The Tag Model.
class Tag(models.Model):
	show = models.ForeignKey(Show, related_name='tags', on_delete=CASCADE, null=True, blank=True)
	tag = models.CharField(max_length = 500)
	def __str__(self):
		return "%s" % self.tag