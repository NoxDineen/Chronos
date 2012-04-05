from chronos.models import *
from datetime import *
import calendar
import time
from django.shortcuts import get_object_or_404, render_to_response, render
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse

month_names = "January February March April May June July August September October November December"
month_names = month_names.split()
now = datetime.now()

def index(request):
	year = now.year
	month = now.month

	return render(request, 'chronos/month.html', {'year' : year , 'month' : month})

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
		if form.is_valid:
			new_assignment = Assignment()
			new_assignment.person = form.cleaned_data['person']
			new_assignment.date = datetime.strptime('form.cleaned_data['date']', '%Y %m %d')
# AJAX GOODNESS GOES HERE
		else:
			form = AssignmentForm()

	# if request.method =='POST':
	# 	form = CommentForm(request.POST)
	# 	if form.is_valid():
	# 		new_comment = Comment()
	# 		new_comment.comment = form.cleaned_data['comment']
	# 		new_comment.name = form.cleaned_data['name']
	# 		new_comment.email = form.cleaned_data['email']
	# 		new_comment.photo_id = myphoto.id
	# 		new_comment.save()
	# 		if request.is_ajax():
	# 			data = simplejson.dump(
	# 				{'comment': new_comment.comment,
	# 				'created': new_comment.created,
	# 				'email': new_comment.email,
	# 				'name': new_comment.name }, 
	# 				cls=DjangoJSONEncoder
	# 				)
	# 			return HttpResponse(data, mimetype='application/json')
	# 		else:
	# 			return HttpResponseRedirect('/photo/%d' % myphoto.id)
	# else:
	# 	form = CommentForm()
			
	return render(request, 'chronos/month.html', dict(year=year, month=month, day=day, month_days=lst, mname=month_names[month-1], support_team=support_team, not_support_team=not_support_team))