# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#import uuid
from django.db import models
#from polymorphic.models import PolymorphicModel


class PathTypeName(models.Model):
    path_name = models.CharField(max_length=256)

    class Meta:
        db_table = 'Path Name'
        ordering = ['path_name']


class Clusters(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'Clusters'
        ordering = ['name']


class Program(models.Model):
    name = models.CharField(max_length=256)
    cluster = models.ForeignKey('Clusters', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Program'
        ordering = ['name', 'cluster']


class ProgramSkills(models.Model):
    program = models.ForeignKey('Program', on_delete=models.CASCADE)
    skills = models.CharField(max_length=256, blank=False, null=True)

    class Meta:
        db_table = 'Program Skills'


class ProgramDuration(models.Model):
    duration = models.PositiveSmallIntegerField(blank=False, null=True)
    in_years_or_month = models.CharField(max_length=12, blank=False)

    class Meta:
        db_table = 'Program Duration'


class OverviewContent(models.Model):
    topcode = models.CharField(max_length=256, blank= False, null=True)
    learning_outcomes = models.CharField(max_length=256, blank=False, null=True)
    skills_learned = models.CharField(max_length=1000, blank=False, null=True)

    class Meta:
        db_table = 'Overview Content'


class CourseType(models.Model):
    title = models.CharField(max_length=256, blank=False, null=True)

    class Meta:
        db_table = 'Course Type'


class Courses(models.Model):
    title = models.CharField(max_length=256, blank=False, null=True)
    description = models.CharField(max_length=1000, blank=False, null=True)
    serial_number = models.PositiveSmallIntegerField(blank=True, null=True)
    course_type = models.ForeignKey('CourseType', on_delete=models.CASCADE)
    course_top_code = models.PositiveSmallIntegerField()
    units = models.PositiveSmallIntegerField()
    advisory = models.CharField(max_length=1000, blank=False, null=True)
    hours = models.TimeField()
    transferable = models.BooleanField()
    course_instruction_type = models.CharField(max_length=256, blank=False, null=True)
    credit_status = models.CharField(max_length=256, blank=False, null=True)
    gen_id = models.CharField(max_length=256, blank=False, null=True)
    course_milestone = models.ForeignKey('Milestone', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Courses'


class MilestoneType(models.Model):
    type = models.CharField(max_length=50, blank=False, null=True)

    class Meta:
        db_table = 'Milestone Type'


class MilestoneResource(models.Model):
    photo = models.FilePathField(blank=True)
    video = models.FilePathField(blank=True)
    gif_animation = models.FilePathField(blank=True)

    class Meta:
        db_table = 'Milestone Resource'


class Milestone(models.Model):
    message = models.CharField(max_length=256, blank=False, null=True)
    type = models.ForeignKey('MilestoneType', on_delete=models.CASCADE)
    course = models.ForeignKey('Courses', on_delete=models.CASCADE)
    url = models.URLField(blank=False)
    resource = models.ForeignKey('MilestoneResource', on_delete=models.CASCADE)
    attachment = models.FileField(blank=True)

    class Meta:
        db_table = 'Milestone'


class PathClusterProgram(models.Model):
    cluster = models.ForeignKey('Clusters', on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=False)
    program = models.ForeignKey('Program', on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    no_of_courses = models.IntegerField()
    min_gpa = models.SmallIntegerField()
    duration = models.IntegerField()
    overview = models.ForeignKey('OverviewContent', on_delete=models.CASCADE)
    courses = models.ForeignKey('Courses', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Cluster Program'









