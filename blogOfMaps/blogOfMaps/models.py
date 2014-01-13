from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Users(User):
    user_pic = models.ForeignKey('MediaObject')


class Story(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    title = models.CharField(max_length=255, default=None, blank=True, null=True)
    text = models.TextField()
    author = models.ForeignKey(Users, related_name='storyes')
    country = models.ForeignKey('Country', related_name='storyes')
    public = models.BooleanField(default=False)
    version_last = models.ForeignKey('StoryVersion', related_name='story')

    def __unicode__(self):
        return self.title


class StoryVersion(Story):
    edited_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)


class Country(models.Model):
    name = models.CharField(max_length=255, default=None, blank=True, null=True)
    eng_name = models.CharField(max_length=255)
    story_count = models.IntegerField()
    point = models.ForeignKey('Point')

    def __unicode__(self):
        return self.name


class Point(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    comment = models.TextField()
    author = models.ForeignKey(Users)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)


class MediaObject(models.Model):
    file_name = models.CharField(max_length=255)
    file_ext = models.CharField(max_length=4)
    file_hash = models.CharField(max_length=255, editable=False, blank=True, null=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    deleted = models.BooleanField(default=False)
    story = models.ForeignKey(Story, related_name='media')
    author = models.ForeignKey(Users, related_name='media')

    def __unicode__(self):
        return self.file_name


class Comments(models.Model):
    story = models.ForeignKey(Story, related_name='comment')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    author = models.ForeignKey(Users, related_name='comment')