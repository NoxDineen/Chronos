from django.core.management.base import BaseCommand, CommandError
from timekeeper.chronos.models import Role, Person, Assignment
from django.core import mail
import datetime
import os

class Command(BaseCommand):
    args = '<None needed>'
    help = 'Notifies gueststars of upcoming support shifts'
    
    def handle(self, *args, **kwargs):

        connection = mail.get_connection()
        
        current = datetime.datetime.now()
        tomorrow = current + datetime.timedelta(days=1)
        nextWeek = current + datetime.timedelta(days=7)
        
        gueststarsToday = Assignment.objects.filter(person__is_support=False, date__year=current.year, date__month=current.month, date__day=current.day)
        gueststarsTomorrow = Assignment.objects.filter(person__is_support=False, date__year=tomorrow.year, date__month=tomorrow.month, date__day=tomorrow.day)
        gueststarsNextWeek = Assignment.objects.filter(person__is_support=False, date__year=nextWeek.year, date__month=nextWeek.month, date__day=nextWeek.day)

        for gueststar in gueststarsToday:
            module_dir = os.path.dirname(__file__)
            gueststarToday = os.path.join(module_dir, 'email/gueststarToday.txt')
            gueststarTodayEmail = open(gueststarToday, 'r').read()
            email = mail.EmailMessage("You're a gueststar on support today!", gueststarTodayEmail, 'Sandy Lai <sandy@freshbooks.com>', [gueststar.person.email], connection=connection)
            email.send()

            self.stdout.write('Successfully emailed %s about their gueststar shift today at: %s \n' % (gueststar, gueststar.person.email))

        for gueststar in gueststarsTomorrow:
            module_dir = os.path.dirname(__file__)
            gueststarTomorrow = os.path.join(module_dir, 'email/gueststarTomorrow.txt')
            gueststarTomorrowEmail = open(gueststarTomorrow, 'r').read()
            email = mail.EmailMessage("Tomorrow's the day! Get ready to rock support.", gueststarTomorrowEmail, 'Sandy Lai <sandy@freshbooks.com>', [gueststar.person.email], connection=connection)
            email.send()

            self.stdout.write('Successfully emailed %s about their gueststar shift tomorrow at: %s \n' % (gueststar, gueststar.person.email))

        for gueststar in gueststarsNextWeek:
            module_dir = os.path.dirname(__file__)
            gueststarNextWeek = os.path.join(module_dir, 'email/gueststarNextWeek.txt')
            gueststarNextWeekEmail = open(gueststarNextWeek, 'r').read()
            email = mail.EmailMessage("You're on support next week", gueststarNextWeekEmail, 'Sandy Lai <sandy@freshbooks.com>', [gueststar.person.email], connection=connection)
            email.send()

            self.stdout.write('Successfully emailed %s about their gueststar shift next week at: %s \n' % (gueststar, gueststar.person.email))