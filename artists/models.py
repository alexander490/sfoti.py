from django.db import models

class Artist(models.Model):
	first_name = models.CharField(max_length=140)
	last_name = models.CharField(max_length=140, blank=True)
	biography = models.TextField(blank=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name
