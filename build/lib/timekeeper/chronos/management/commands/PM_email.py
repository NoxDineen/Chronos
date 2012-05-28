from django.core.management.base import BaseCommand, CommandError
from timekeeper.chronos.models import Role, Person, Assignment
from django.core import mail
import datetime
import os

class Command(BaseCommand):
    args = '<WTF GOES HERE?>'
    help = 'Sends follow up survey to support gueststars and notifies rockstars of tomorrow'
    
    def handle(self, *args, **kwargs):

        connection = mail.get_connection()
        
        current = datetime.datetime.now()
        tomorrow = current + datetime.timedelta(days=1)
        
        gueststarsToday = Assignment.objects.filter(person__is_support=False, date__year=current.year, date__month=current.month, date__day=current.day)
        rockstarsTomorrow = Assignment.objects.filter(person__is_support=True, date__year=tomorrow.year, date__month=tomorrow.month, date__day=tomorrow.day)


        for gueststar in gueststarsToday:
            module_dir = os.path.dirname(__file__)
            gueststarFollowup = os.path.join(module_dir, 'email/gueststarFollowup.txt')
            gueststarFollowupEmail = open(gueststarFollowup, 'r').read()
            email = mail.EmailMessage('Give us feedback about your day on support', gueststarFollowupEmail, 'Sandy Lai <sandy@freshbooks.com>', [gueststar.person.email], connection=connection)
            email.send()

            self.stdout.write('Successfully emailed %s at: %s \n' % (gueststar, gueststar.person.email))


        for rockstar in rockstarsTomorrow:
            rockstarTomorrowEmail = "Have a great day rocking it on support tomorrow. Your role is %s." % rockstar.role
            email = mail.EmailMessage("You're on support tomorrow!", rockstarTomorrowEmail, 'Chronos <chronos@freshbooks.com>', [rockstar.person.email], connection=connection)
            email.send()

            self.stdout.write('Successfully emailed %s at: %s \n' % (rockstar, rockstar.person.email))