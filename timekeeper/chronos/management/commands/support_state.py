from django.core.management.base import BaseCommand, CommandError
from chronos.models import Role, Person, Assignment
import datetime
import re

class Command(BaseCommand):
    args = '<none needed>'
    help = 'Sends follow up survey to support gueststars and notifies rockstars of tomorrow'
    
    def handle(self, *args, **kwargs):

        current = datetime.datetime.now()
        supportToday = Assignment.objects.filter(date__year=current.year, date__month=current.month, date__day=current.day)
        name = re.compile(r"[\w]+")

        for supportStar in supportToday:
            #support_name = name.match(supportStar.person.email)
            #support_name = str(support_name)
            #self.stdout.write('%s \n' % support_name)
            self.stdout.write('%s \n' % supportStar.person.email)
