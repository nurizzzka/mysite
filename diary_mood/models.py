from django.db import models
from datetime import datetime

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class DiaryMood(models.Model):
	status = models.CharField(max_length=500)
	exersice = models.BooleanField(default=False)
	scale = models.IntegerField(choices = PRODUCT_QUANTITY_CHOICES, default = PRODUCT_QUANTITY_CHOICES[0])
	date = models.DateField(blank=True, null=True)


	def dateOfPublish(self):
		self.data = datetime.now()
		self.save()

	def __str__(self):
		return self.status
