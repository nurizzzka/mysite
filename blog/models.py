from django.db import models

# Create your models here.
# match with bd, stycrure
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class Students(models.Model):
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	patronymic = models.CharField(max_length=50)
	birthday = models.DateField()
	email = models.EmailField(max_length=70, blank=True)
	courses_quantity = models.PositiveIntegerField()
	student_description = models.TextField()
	students_money = models.DecimalField(max_digits=6, decimal_places=2)
	passport = models.CharField(max_length=50)
	identity_number = models.CharField(max_length=20)
	def __str__(self):
		return self.fname

