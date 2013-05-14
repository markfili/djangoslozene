# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PartManufacturer'
        db.create_table(u'dijelovi_partmanufacturer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'dijelovi', ['PartManufacturer'])

        # Adding field 'Part.colour'
        db.add_column(u'dijelovi_part', 'colour',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Part.state'
        db.add_column(u'dijelovi_part', 'state',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=20),
                      keep_default=False)

        # Adding field 'Part.manufacturer'
        db.add_column(u'dijelovi_part', 'manufacturer',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dijelovi.PartManufacturer'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Part.price'
        db.add_column(u'dijelovi_part', 'price',
                      self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=20, decimal_places=2, blank=True),
                      keep_default=False)


        # Changing field 'Part.name'
        db.alter_column(u'dijelovi_part', 'name', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Part.part_num'
        db.alter_column(u'dijelovi_part', 'part_num', self.gf('django.db.models.fields.CharField')(max_length=20))

    def backwards(self, orm):
        # Deleting model 'PartManufacturer'
        db.delete_table(u'dijelovi_partmanufacturer')

        # Deleting field 'Part.colour'
        db.delete_column(u'dijelovi_part', 'colour')

        # Deleting field 'Part.state'
        db.delete_column(u'dijelovi_part', 'state')

        # Deleting field 'Part.manufacturer'
        db.delete_column(u'dijelovi_part', 'manufacturer_id')

        # Deleting field 'Part.price'
        db.delete_column(u'dijelovi_part', 'price')


        # Changing field 'Part.name'
        db.alter_column(u'dijelovi_part', 'name', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Part.part_num'
        db.alter_column(u'dijelovi_part', 'part_num', self.gf('django.db.models.fields.CharField')(max_length=10))

    models = {
        u'dijelovi.part': {
            'Meta': {'object_name': 'Part'},
            'colour': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dijelovi.PartManufacturer']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'part_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dijelovi.PartCategory']"}),
            'part_num': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '20'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dijelovi.Supplier']"}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        u'dijelovi.partcategory': {
            'Meta': {'object_name': 'PartCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'dijelovi.partcomments': {
            'Meta': {'object_name': 'PartComments'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dijelovi.Part']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dijelovi.User']"})
        },
        u'dijelovi.partmanufacturer': {
            'Meta': {'object_name': 'PartManufacturer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'dijelovi.supplier': {
            'Meta': {'object_name': 'Supplier'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'dijelovi.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['dijelovi']