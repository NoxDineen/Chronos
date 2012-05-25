from django.core.management.base import BaseCommand, CommandError
from timekeeper.chronos.models import Person, Assignment, Role
from django.core.mail import send_mail
import datetime

class Command(BaseCommand):
    args = '<WTF GOES HERE?>'
    help = 'Notifies gueststars of upcoming support shifts'
    
    def handle(self, *args, **kwargs):
        
        current = datetime.datetime.now()
        tomorrow = current + datetime.timedelta(days=1)
        nextWeek = current + datetime.timedelta(days=7)
        
        rockstarsToday = Assignment.objects.filter(person__is_support=True, date__year=current.year, date__month=current.month, date__day=current.day)

        for rockstar in rockstarsToday:
            send_mail("You're on support today!", "If you see this things are working", "test@localobject.com", ["nox@freshbooks.com"], fail_silently=False)

            self.stdout.write('Successfully emailed "%s"\n' % rockstar)