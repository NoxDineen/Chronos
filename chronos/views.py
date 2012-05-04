from chronos.models import *
from chronos.forms import AssignmentForm
import datetime
import calendar
import time
from django.shortcuts import get_object_or_404, render_to_response, render
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect

month_names = "January February March April May June July August September October November December"
month_names = month_names.split()

def month(request, year=None, month=None):
	if year is None or month is None:
		now = datetime.datetime.now()
		year = now.year
		month = now.month
	else:
		year, month = int(year), int(month)

	support_team = Person.objects.filter(is_support=True)
	not_support_team = Person.objects.filter(is_support=False)
	roles = Role.objects.all()

	cal = calendar.Calendar() 
	month_days = cal.itermonthdays(year, month)
	nyear, nmonth, nday = time.localtime()[:3]
	lst = [[]]
	week = 0

	for day in month_days:
		assignments = today = False #are there assignments for this day? today?
		if day:
			assignments = Assignment.objects.filter(date__year=year, date__month=month, date__day=day)
			if year == nyear and month == nmonth and day == nday:
				today = True

		lst[week].append((day, assignments, today))
		if len(lst[week]) == 7:
			lst.append([])
			week+=1

	if request.method == 'POST':
		import pdb; pdb.set_trace()
		form = AssignmentForm(request.POST)
		if form.is_valid():
			form.save()

			if request.is_ajax():
				data = simplejson.dump(
					{'date': new_assignment.date,
					'person': new_assignment.person,
					'role': new_assignment.role}, 
					cls=DjangoJSONEncoder
					)
				return HttpResponse(data, mimetype='application/json')
			else:
				return HttpResponseRedirect('/%d/%d' % (year, month))
	else:
		form = AssignmentForm()

	current = datetime.datetime(year, month, 1)
	next_month = current + datetime.timedelta(days=31)
	prev_month = current - datetime.timedelta(days=1)
			
	return render(request, 'chronos/month.html', dict(year=year, month=month, day=day, month_days=lst, mname=month_names[month-1], roles=roles, support_team=support_team, not_support_team=not_support_team, form=form, prev_month=prev_month, next_month=next_month))


def delete_assignment(request, assignment_id):
	assignment = Assignment.objects.get(id=assignment_id)
	assignment.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def assign_role(request, assignment_id, role_id):
	assignment = Assignment.objects.get(id=assignment_id)
	assignment.role = role_id
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
