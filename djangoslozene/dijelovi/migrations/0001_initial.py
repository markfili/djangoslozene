# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'dijelovi_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'dijelovi', ['User'])

        # Adding model 'Supplier'
        db.create_table(u'dijelovi_supplier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'dijelovi', ['Supplier'])

        # Adding model 'PartCategory'
        db.create_table(u'dijelovi_partcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'dijelovi', ['PartCategory'])

        # Adding model 'Part'
        db.create_table(u'dijelovi_part', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('year', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dijelovi.Supplier'])),
            ('part_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dijelovi.PartCategory'])),
            ('part_num', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'dijelovi', ['Part'])

        # Adding model 'PartComments'
        db.create_table(u'dijelovi_partcomments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dijelovi.User'])),
            ('part', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dijelovi.Part'])),
        ))
        db.send_create_signal(u'dijelovi', ['PartComments'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'dijelovi_user')

        # Deleting model 'Supplier'
        db.delete_table(u'dijelovi_supplier')

        # Deleting model 'PartCategory'
        db.delete_table(u'dijelovi_partcategory')

        # Deleting model 'Part'
        db.delete_table(u'dijelovi_part')

        # Deleting model 'PartComments'
        db.delete_table(u'dijelovi_partcomments')


    models = {
        u'dijelovi.part': {
            'Meta': {'object_name': 'Part'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'part_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dijelovi.PartCategory']"}),
            'part_num': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
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