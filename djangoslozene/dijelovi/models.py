from django.db import models
import datetime
from django.forms.fields import FileField
from django.utils import timezone
from django import forms

class User(models.Model):
	name = models.CharField(max_length=20)
	# address = models.CharField(max_length=20)
	# mail = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name


# supplier
#         name - char
#         address - 
#         telephone - num
#         mail - char
#         list of available parts - 
#         buyer comments
class Supplier(models.Model):
	name = models.CharField(max_length=20)
	# address = models.CharField(max_length=20)
	# telephone = models.CharField(max_length=20)
	# mail = models.CharField(max_length=20)


	def __unicode__(self):
		return self.name

class PartCategory(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name


class Part(models.Model):
    name = models.CharField(max_length=10)
    year = models.IntegerField(max_length=4)
    supplier = models.ForeignKey(Supplier)
    part_category = models.ForeignKey(PartCategory)
    part_num = models.CharField(max_length=10)
    date_added = models.DateTimeField('date added')
    # Scomments = models.ForeignKey(PartComments)
    # category = models.ForeignKey(PartCategory)

    def __unicode__(self):
	    return self.name
    
    def year_created(self):
    	return self.year
    def was_added_recently(self):
    	return self.date_added >= timezone.now() - datetime.timedelta(days=1)
    was_added_recently.admin_order_field = 'date_added'
    was_added_recently.boolean = True
    was_added_recently.short_description = 'Published recently?'

class PartComments(models.Model):
	text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	user = models.ForeignKey(User)
	part = models.ForeignKey(Part)

	def __unicode__(self):
		return self.text	
	# def last_published(self):
	# 	return self.pub_date

class UploadFileForm(forms.Form):
	file = forms.FileField(label='Choose Excel table to upload:')