# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AssignmentHasTags(models.Model):
    id = models.IntegerField(primary_key=True)
    assignment_id = models.IntegerField(null=True, blank=True)
    tag_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'assignment_has_tags'

class Assignments(models.Model):
    id = models.IntegerField(primary_key=True)
    # user_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey('schedgy.Users')
    # day_id = models.IntegerField(null=True, blank=True)
    day = models.ForeignKey('schedgy.Days')
    assignment_type = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'assignments'

class BdrbJobQueues(models.Model):
    id = models.IntegerField(primary_key=True)
    args = models.TextField(blank=True)
    worker_name = models.CharField(max_length=765, blank=True)
    worker_method = models.CharField(max_length=765, blank=True)
    job_key = models.CharField(max_length=765, blank=True)
    taken = models.IntegerField(null=True, blank=True)
    finished = models.IntegerField(null=True, blank=True)
    timeout = models.IntegerField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    archived_at = models.DateTimeField(null=True, blank=True)
    tag = models.CharField(max_length=765, blank=True)
    submitter_info = models.CharField(max_length=765, blank=True)
    runner_info = models.CharField(max_length=765, blank=True)
    worker_key = models.CharField(max_length=765, blank=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'bdrb_job_queues'

class Days(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    required_user_count = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'days'

class RequiredRoles(models.Model):
    id = models.IntegerField(primary_key=True)
    count = models.IntegerField(null=True, blank=True)
    role_type_id = models.IntegerField(null=True, blank=True)
    day_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'required_roles'

class RoleRestrictions(models.Model):
    id = models.IntegerField(primary_key=True)
    day_id = models.IntegerField(null=True, blank=True)
    role_type_id = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'role_restrictions'

class RoleTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'role_types'

class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    role_type_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'roles'

class SchemaMigrations(models.Model):
    version = models.CharField(max_length=765, unique=True)
    class Meta:
        db_table = u'schema_migrations'

class Tags(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'tags'

class UserRestrictions(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=765, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    day_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'user_restrictions'

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=765, blank=True)
    level = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=765, blank=True)
    first_name = models.CharField(max_length=765, blank=True)
    last_name = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'users'

