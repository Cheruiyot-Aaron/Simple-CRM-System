from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=80)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")

class add_book(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	book_name = models.CharField(max_length=50, default="Unknown")
	last_name =  models.CharField(max_length=50, default="Unknown")
	email =  models.CharField(max_length=80, default="Unknown")
	phone = models.CharField(max_length=15, default="Unknown")
	address =  models.CharField(max_length=100, default="Unknown")
	city =  models.CharField(max_length=50, default="Unknown")
	state =  models.CharField(max_length=50, default="Unknown")
	zipcode =  models.CharField(max_length=20, default="Unknown")

	def __str__(self):
		return(f"{self.book_name} {self.last_name}")