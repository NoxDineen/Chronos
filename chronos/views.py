from chronos.models import *
from chronos.forms import AssignmentForm, PersonForm
import datetime
import calendar
import time
from django.shortcuts import get_object_or_404, render_to_response, render
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import simplejson
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required

month_names = "January February March April May June July August September October November December"
month_names = month_names.split()

def month(request, year=None, month=None):
	if year is None or month is None:
		now = datetime.datetime.now()
		year = now.year
		month = now.month
	else:
		year, month = int(year), int(month)

	if request.method == 'POST':
		form = AssignmentForm(request.POST)
		if form.is_valid():
			new_assignment = Assignment()
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

	current = datetime.datetime(year, month, 1)
	next_month = current + datetime.timedelta(days=31)
	prev_month = current - datetime.timedelta(days=1)
			
	return render(request, 'chronos/month.html', dict(year=year, month=month, day=day, month_days=lst, mname=month_names[month-1], roles=roles, support_team=support_team, not_support_team=not_support_team, form=form, prev_month=prev_month, next_month=next_month))

@staff_member_required
def create_assignment(request):
	assignment = Assignment(request.POST)
	assignment.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@staff_member_required
def delete_assignment(request, assignment_id):
	assignment = Assignment.objects.get(id=assignment_id)
	assignment.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@staff_member_required
def assign_role(request, assignment_id, role_id):
	assignment = Assignment.objects.get(id=assignment_id)
	assignment.role_id = role_id
	assignment.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@staff_member_required
def create_user(request):
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect('/create-user/')
	else:
		form = PersonForm()

	return render(request, 'chronos/create-user.html', { 'form' : form})
