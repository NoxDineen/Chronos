# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('chronos_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('is_support', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('chronos', ['Person'])

        # Adding model 'Assignment'
        db.create_table('chronos_assignment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chronos.Person'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chronos.Role'])),
        ))
        db.send_create_signal('chronos', ['Assignment'])

        # Adding unique constraint on 'Assignment', fields ['date', 'person']
        db.create_unique('chronos_assignment', ['date', 'person_id'])

        # Adding model 'Role'
        db.create_table('chronos_role', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('icon', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('icon_mini', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('chronos', ['Role'])


    def backwards(self, orm):
        # Removing unique constraint on 'Assignment', fields ['date', 'person']
        db.delete_unique('chronos_assignment', ['date', 'person_id'])

        # Deleting model 'Person'
        db.delete_table('chronos_person')

        # Deleting model 'Assignment'
        db.delete_table('chronos_assignment')

        # Deleting model 'Role'
        db.delete_table('chronos_role')


    models = {
        'chronos.assignment': {
            'Meta': {'unique_together': "(('date', 'person'),)", 'object_name': 'Assignment'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chronos.Person']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chronos.Role']"})
        },
        'chronos.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_support': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'chronos.role': {
            'Meta': {'object_name': 'Role'},
            'icon': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'icon_mini': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['chronos']