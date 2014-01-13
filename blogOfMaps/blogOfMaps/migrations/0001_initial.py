# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Users'
        db.create_table(u'blogOfMaps_users', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('user_pic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogOfMaps.MediaObject'])),
        ))
        db.send_create_signal(u'blogOfMaps', ['Users'])

        # Adding model 'Story'
        db.create_table(u'blogOfMaps_story', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='storyes', to=orm['blogOfMaps.Users'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(related_name='storyes', to=orm['blogOfMaps.Country'])),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('version_last', self.gf('django.db.models.fields.related.ForeignKey')(related_name='story', to=orm['blogOfMaps.StoryVersion'])),
        ))
        db.send_create_signal(u'blogOfMaps', ['Story'])

        # Adding model 'StoryVersion'
        db.create_table(u'blogOfMaps_storyversion', (
            (u'story_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['blogOfMaps.Story'], unique=True, primary_key=True)),
            ('edited_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'blogOfMaps', ['StoryVersion'])

        # Adding model 'Country'
        db.create_table(u'blogOfMaps_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('eng_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('story_count', self.gf('django.db.models.fields.IntegerField')()),
            ('point', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogOfMaps.Point'])),
        ))
        db.send_create_signal(u'blogOfMaps', ['Country'])

        # Adding model 'Point'
        db.create_table(u'blogOfMaps_point', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogOfMaps.Users'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'blogOfMaps', ['Point'])

        # Adding model 'MediaObject'
        db.create_table(u'blogOfMaps_mediaobject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('file_ext', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('file_hash', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(related_name='media', to=orm['blogOfMaps.Story'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='media', to=orm['blogOfMaps.Users'])),
        ))
        db.send_create_signal(u'blogOfMaps', ['MediaObject'])

        # Adding model 'Comments'
        db.create_table(u'blogOfMaps_comments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comment', to=orm['blogOfMaps.Story'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comment', to=orm['blogOfMaps.Users'])),
        ))
        db.send_create_signal(u'blogOfMaps', ['Comments'])


    def backwards(self, orm):
        # Deleting model 'Users'
        db.delete_table(u'blogOfMaps_users')

        # Deleting model 'Story'
        db.delete_table(u'blogOfMaps_story')

        # Deleting model 'StoryVersion'
        db.delete_table(u'blogOfMaps_storyversion')

        # Deleting model 'Country'
        db.delete_table(u'blogOfMaps_country')

        # Deleting model 'Point'
        db.delete_table(u'blogOfMaps_point')

        # Deleting model 'MediaObject'
        db.delete_table(u'blogOfMaps_mediaobject')

        # Deleting model 'Comments'
        db.delete_table(u'blogOfMaps_comments')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'blogOfMaps.comments': {
            'Meta': {'object_name': 'Comments'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comment'", 'to': u"orm['blogOfMaps.Users']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comment'", 'to': u"orm['blogOfMaps.Story']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'blogOfMaps.country': {
            'Meta': {'object_name': 'Country'},
            'eng_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'point': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blogOfMaps.Point']"}),
            'story_count': ('django.db.models.fields.IntegerField', [], {})
        },
        u'blogOfMaps.mediaobject': {
            'Meta': {'object_name': 'MediaObject'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media'", 'to': u"orm['blogOfMaps.Users']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'file_ext': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'file_hash': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media'", 'to': u"orm['blogOfMaps.Story']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blogOfMaps.point': {
            'Meta': {'object_name': 'Point'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blogOfMaps.Users']"}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {})
        },
        u'blogOfMaps.story': {
            'Meta': {'object_name': 'Story'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'storyes'", 'to': u"orm['blogOfMaps.Users']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'storyes'", 'to': u"orm['blogOfMaps.Country']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'version_last': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'story'", 'to': u"orm['blogOfMaps.StoryVersion']"})
        },
        u'blogOfMaps.storyversion': {
            'Meta': {'object_name': 'StoryVersion', '_ormbases': [u'blogOfMaps.Story']},
            'edited_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'story_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['blogOfMaps.Story']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'blogOfMaps.users': {
            'Meta': {'object_name': 'Users', '_ormbases': [u'auth.User']},
            'user_pic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blogOfMaps.MediaObject']"}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blogOfMaps']