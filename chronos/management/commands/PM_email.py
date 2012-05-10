from django.core.management.base import BaseCommand, CommandError
from chronos.models import Role, Person, Assignment
from django.core.mail import send_mail
import datetime

class Command(BaseCommand):
    args = '<WTF GOES HERE?>'
    help = 'Sends follow up survey to support gueststars and notifies rockstars of tomorrow'
    
    def handle(self, *args, **kwargs):
        
        current = datetime.datetime(year, month, day)
        tomorrow = current + datetime.timedelta(days=1)
        
        gueststarsToday = Assignment.objects.filter(person.role !='is_support', date__year==current.year, date__month==current.month, date__day==current.day)

        rockstarsTomorrow = Assignment.objects.filter(person.role =='is_support', date__year==tomorrow.year, date__month==tomorrow.month date__day==tomorrow.day) 

        for gueststar in gueststarsToday:
            try send_email("Follow up for your support day", file.open(SOMEFILE.TXT), "sandy@freshbooks.com", gueststar.person.email, fail_silently=False)
            except Assignment.DoesNotExist:
                raise CommandError('Assignment does not exist')

        for rockstar in rockstarsTomorrow:
            try send_mail("You're on support tomorrow!", "Your role is " + rockstar.role.name, 'schedgy@freshbooks.com', rockstar.person.email, fail_silently=False)
            except Assignment.DoesNotExist:
                raise CommandError('Assignment does not exist')


# rockstar today/tomorrow gueststar update
# gueststars nextWeek
# gueststars tomorrow

# gueststars followUp (day of support) -- > 4:30pm
# rockstars tomorrow --> 4:30pm