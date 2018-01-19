from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	datetime = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	content = models.TextField(max_length=10000)

	def __str__(self):
		return self.title

	def publish(self):
		self.published_date = timezone.now()
		self.save()