from django.core.management.base import BaseCommand, CommandError
from chronos.models import Role, Person, Assignment
from django.core.mail import send_mail
import datetime

class Command(BaseCommand):
    args = '<WTF GOES HERE?>'
    help = 'Notifies gueststars of upcoming support shifts'
    
    def handle(self, *args, **kwargs):
        
        current = datetime.datetime(year, month, day)
        tomorrow = current + datetime.timedelta(days=1)
        nextWeek = current + datetime.timedelta(days=7)
        
        gueststarsToday = Assignment.objects.filter(person.role !='is_support', date__year==current.year, date__month==current.month, date__day==current.day)

        gueststarsTomorrow = Assignment.objects.filter(person.role !='is_support', date__year==tomorrow.year, date__month==tomorrow.month, date__day==tomorrow.day)
        
        gueststarsNextWeek = Assignment.objects.filter(person.role != 'is_support', date__year==nextWeek.year, date__month==nextWeek.month, date__day==nextWeek.day)

        for gueststar in gueststarsToday:
            try send_email("You're on support today!", file.open(SOMEFILE.TXT), "sandy@freshbooks.com", gueststar.person.email, fail_silently=False)
            except Assignment.DoesNotExist:
                raise CommandError('Assignment does not exist')

        for gueststar in gueststarsTomorrow:
            try send_email("You're on support tomorrow!", file.open(SOMEFILE.TXT), "sandy@freshbooks.com", gueststar.person.email, fail_silently=False)
            except Assignment.DoesNotExist:
                raise CommandError('Assignment does not exist')

        for gueststar in gueststarsNextWeek:
            try send_email("You're on support next week, this is the last day to reschedule!", file.open(SOMEOTHERFILE.TXT), "sandy@freshbooks.com", gueststar.person.email, fail_silently=False)
            except Assignment.DoesNotExist:
                raise CommandError('Assignment does not exist')