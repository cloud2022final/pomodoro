from django.db import models

# Create your models here.

class RoomData(models.Model):
	roomname = models.CharField(max_length=20, help_text='Enter room\'s name', unique=True)
	minutes = models.IntegerField()
	seconds = models.IntegerField()
	pause = models.BooleanField(default=True)
	message =  models.TextField(help_text='Chat room\'s messages')

	class Meta:
		ordering = ['roomname']

	def __str__(self):
		return self.roomname