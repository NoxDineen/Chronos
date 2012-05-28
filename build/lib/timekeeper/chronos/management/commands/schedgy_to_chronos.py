from django.core.management.base import BaseCommand, CommandError
from timekeeper.chronos.models import Person, Assignment, Role
from schedgy.models import Users, Assignments as SchedgyAssignment, Days
from django.core import mail
import datetime
import os

class Command(BaseCommand):
    args = '<None needed>'
    help = 'Migrates assignments and users from old crufty Schedgy to lovely Chronos'
    
    def handle(self, *args, **kwargs):
       # delete existing data
       Assignment.objects.all().delete()
       Person.objects.all().delete()
       Role.objects.get_or_create(name='Support')

       # create users in Chronos
       for user in Users.objects.using('schedgy').all():
           p = Person()
           p.first_name = user.first_name
           p.last_name = user.last_name
           p.email = user.email
           p.save()

       # create assignments in Chronos
       for assignment in SchedgyAssignment.objects.using('schedgy').all():
           a = Assignment()
           a.date = assignment.day.date
           user_email = assignment.user.email
           a.person = Person.objects.get(email=user_email)
           a.save()

           # .stdout.write('Woo!') 
