from chronos.models import *
from chronos.forms import AssignmentForm
from datetime import *
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
now = datetime.now()

#TODO Remove redundancy from index & month views

def index(request):
	year = now.year
	month = now.month

	support_team = Person.objects.filter(is_support=True)
	not_support_team = Person.objects.filter(is_support=False)

	cal = calendar.Calendar() 
	month_days = cal.itermonthdays(year, month)
	nyear, nmonth, nday = time.localtime()[:3]
	lst = [[]]
	week = 0

	for day in month_days:
		assignments = current = False #are there assignments for this day? current day?
		if day:
			assignments = Assignment.objects.filter(date__year=year, date__month=month, date__day=day)
			if year == nyear and month == nmonth and day == nday:
				current = True

		lst[week].append((day, assignments, current))
		if len(lst[week]) == 7:
			lst.append([])
			week+=1

	if request.method == 'POST':
		form = AssignmentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/%d/%d' % (year, month))
	else:
		form = AssignmentForm()

	if month > 1 and month < 12:
		next_month = month + 1
		next_year = year
		prev_month = month - 1
		prev_year = year
	elif month == 1:
		next_month = month + 1
		next_year = year
		prev_month = 12
		prev_year = year - 1
	else: # month == 12
		next_month = 1 
		next_year = year + 1
		prev_month = month - 1 
		prev_year = year
			
	return render(request, 'chronos/month.html', dict(year=year, month=month, day=day, month_days=lst, mname=month_names[month-1], support_team=support_team, not_support_team=not_support_team, form=form, prev_month=prev_month, prev_year=prev_year, next_month=next_month, next_year=next_year))

def month(request, year, month):
	year, month = int(year), int(month)

	support_team = Person.objects.filter(is_support=True)
	not_support_team = Person.objects.filter(is_support=False)

	cal = calendar.Calendar() 
	month_days = cal.itermonthdays(year, month)
	nyear, nmonth, nday = time.localtime()[:3]
	lst = [[]]
	week = 0

	for day in month_days:
		assignments = current = False #are there assignments for this day? current day?
		if day:
			assignments = Assignment.objects.filter(date__year=year, date__month=month, date__day=day)
			if year == nyear and month == nmonth and day == nday:
				current = True

		lst[week].append((day, assignments, current))
		if len(lst[week]) == 7:
			lst.append([])
			week+=1

	if request.method == 'POST':
		form = AssignmentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/%d/%d' % (year, month))
	else:
		form = AssignmentForm()

	if month > 1 and month < 12:
		next_month = month + 1
		next_year = year
		prev_month = month - 1
		prev_year = year
	elif month == 1:
		next_month = month + 1
		next_year = year
		prev_month = 12
		prev_year = year - 1
	else: # month == 12
		next_month = 1 
		next_year = year + 1
		prev_month = month - 1 
		prev_year = year
			
	return render(request, 'chronos/month.html', dict(year=year, month=month, day=day, month_days=lst, mname=month_names[month-1], support_team=support_team, not_support_team=not_support_team, form=form, prev_month=prev_month, prev_year=prev_year, next_month=next_month, next_year=next_year))