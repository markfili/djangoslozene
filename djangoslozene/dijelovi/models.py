from django.db import models
import datetime
from django.forms.fields import FileField
from django.template.defaultfilters import default
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


class PartManufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Part(models.Model):
    COLOUR = (
        (u'R', u'Crvena'),
        (u'G', u'Zelena'),
        (u'B', u'Plava'))
    STATE_STAR = (
        (u'1', u'Jako lose'),
        (u'2', u'Lose'),
        (u'3', u'Dobro'),
        (u'4', u'Vrlo dobro'),
        (u'5', u'Odlicno'))
    name = models.CharField(max_length=20)
    year = models.IntegerField(max_length=4)
    supplier = models.ForeignKey(Supplier)
    part_category = models.ForeignKey(PartCategory)
    part_num = models.CharField(max_length=20)
    date_added = models.DateTimeField('date added')
    image = models.ImageField(upload_to='pictures/dijelovi', blank=True)
    colour = models.CharField(max_length=20, choices=COLOUR, default="Nedostupno", blank=True, null=True)
    state = models.CharField(max_length=20, choices=STATE_STAR, default=0)
    manufacturer = models.ForeignKey(PartManufacturer, blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0, blank=True, null=True)
    # comments = models.ForeignKey(PartComments)
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


class TestForm(forms.BaseModelForm):
    i = forms.CharField(max_length=100)

    def __unicode__(self):
        return self.text