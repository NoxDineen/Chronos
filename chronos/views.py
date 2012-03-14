from chronos.models import *
from datetime import *
import calendar
import time
from django.shortcuts import get_object_or_404, render_to_response

month_names = "January February March April May June July August September October November December"
month_names = month_names.split()
now = datetime.now()

def month(request, year=None, month=None):
	if year:
		year = int(year)
	else:
		year = now.year

	if month:
		month = int(month)
	else:
		month = now.month

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

	return render_to_response('chronos/month.html', dict(year=year, month=month, day=day, month_days=lst, mname=month_names[month-1]))