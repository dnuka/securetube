from django.db import models

class Channels(models.Model):

	def __str__(self):
		return self.url

	url = models.URLField()


class Channel(models.Model):

	def __str__(self):
		return self.videos

	url = models.URLField()
	videos = set()
