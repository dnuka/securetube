from django.db import models

class Channels(models.Model):
	url = models.URLField()


class Channel(models.Model):
	url = models.URLField()
	videos = set()
