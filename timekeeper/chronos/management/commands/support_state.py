from django.core.management.base import BaseCommand, CommandError
from chronos.models import Role, Person, Assignment
import datetime

class Command(BaseCommand):
    args = '<none needed>'
    help = 'Sends follow up survey to support gueststars and notifies rockstars of tomorrow'
    
    def handle(self, *args, **kwargs):

        current = datetime.datetime.now()
        supportToday = Assignment.objects.filter(date__year=current.year, date__month=current.month, date__day=current.day)

        for supportStar in supportToday:
            support_name = supportStar.person.email.split('@')
            self.stdout.write('%s \n' % support_name[0])
