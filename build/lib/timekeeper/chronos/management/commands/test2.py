from django.core.management.base import BaseCommand, CommandError
from timekeeper.chronos.models import Person, Assignment, Role
from django.core import mail
import datetime

connection = mail.get_connection()

class Command(BaseCommand):
    args = '<No args needed>'
    help = 'Notifies rockstars of their role today'
    
    def handle(self, *args, **kwargs):
        
        current = datetime.datetime.now()
        
        rockstarsToday = Assignment.objects.filter(person__is_support=True, date__year=current.year, date__month=current.month, date__day=current.day)

        for rockstar in rockstarsToday:
            email_body = "You're on support today! Your role is %s. \n" % rockstar.role
            email = mail.EmailMessage('You are on support today!', email_body, 'Sandy Lai <sandy@freshbooks.com>', [rockstar.person.email], connection=connection)
            email.send()

            self.stdout.write('Successfully emailed %s at: %s \n' % (rockstar, rockstar.person.email))

# TODO: Figure out if I have to explicitly close the SMTP connection after the for loop -- feels like I should