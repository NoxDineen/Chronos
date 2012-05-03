from django.contrib import admin
from chronos.models import *

class PersonAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	list_display_links = ('first_name', 'last_name', 'email')
	list_filter = ('is_support',)
	search_fields = ('first_name',)

class AssignmentAdmin(admin.ModelAdmin):
	list_filter = ('person', 'role')
	date_hierarchy = 'date'

class RoleAdmin(admin.ModelAdmin):
	list_display = ('name', 'picture', 'icon')

	def picture(self, icon):
		return '<img src="%s" height="48"/>' % icon.filename.url
	picture.allow_tags = True


admin.site.register(Person, PersonAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Role, RoleAdmin)