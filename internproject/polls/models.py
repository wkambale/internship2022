from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

# class className(param1, param2):

class Question(models.Model):
	question_text = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date_published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=100)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
