from django.core.management.base import BaseCommand, CommandError
from chronos.models import Person, Assignment, Role
from django.core import mail
import datetime

connection = mail.get_connection()

class Command(BaseCommand):
    args = '<No args needed>'
    help = 'Notifies gueststars of upcoming support shifts'
    
    def handle(self, *args, **kwargs):
        
        current = datetime.datetime.now()
        
        rockstarsToday = Assignment.objects.filter(person__is_support=True, date__year=current.year, date__month=current.month, date__day=current.day)

        for rockstar in rockstarsToday:
            email_body = "You're on support today! Your role is %s. \n" % rockstar.role
            email = mail.EmailMessage('You are on support today!', email_body, 'ryan@freshbooks.com', [rockstar.person.email], connection=connection)

            # send_mail("You're on support today!", "If you see this things are working", "test@localobject.com", ["nox@freshbooks.com"], fail_silently=False)

            self.stdout.write('Successfully emailed "%s"\n' % rockstar)
            self.stdout.write(rockstar.person.email)