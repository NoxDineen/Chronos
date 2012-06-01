# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from schedgy.models import Users, Assignments as SchedgyAssignment, Days

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."
        orm.Assignment.objects.all().delete()
        orm.Person.objects.all().delete()
        default_role, created = orm.Role.objects.get_or_create(name='Support')

        # create users in Chronos
        for user in Users.objects.using('schedgy').all():
            p = orm.Person()
            p.first_name = user.first_name
            p.last_name = user.last_name
            p.email = user.email
            p.save()

        # create assignments in Chronos
        for assignment in SchedgyAssignment.objects.using('schedgy').all():
            a = orm.Assignment()
            a.date = assignment.day.date
            user_email = assignment.user.email
            a.person = orm.Person.objects.get(email=user_email)
            a.role = default_role
            a.save()

    def backwards(self, orm):
        "Write your backwards methods here."
        orm.Assignment.objects.all().delete()
        orm.Person.objects.all().delete()

    models = {
        'chronos.assignment': {
            'Meta': {'unique_together': "(('date', 'person'),)", 'object_name': 'Assignment'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chronos.Person']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [],
                {'default': 'False', 'to': "orm['chronos.Role']"})
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
    symmetrical = True
