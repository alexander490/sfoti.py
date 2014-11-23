from django.db import models

class Artist(models.Model):
	first_name = models.CharField(max_length=140)
	last_name = models.CharField(max_length=140, blank=True)
	biography = models.TextField(blank=True)
	