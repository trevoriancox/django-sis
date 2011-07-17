#       settings.py
#       
#       Copyright 2010 Cristo Rey New York High School
#		Author David M Burke <dburke@cristoreyny.org>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

# Django settings for ecwsp project.
# This section is for editing

# Django ldap groups example configuration.
import os,sys

LDAP = False
if LDAP:
    LDAP_SERVER = 'crnyhs-dc.admin.cristoreyny.org'
    NT4_DOMAIN = 'ADMIN'
    LDAP_PORT = 389
    LDAP_URL = 'ldap://%s:%s' % (LDAP_SERVER, LDAP_PORT)
    SEARCH_DN = 'DC=admin,DC=cristoreyny,DC=org'
    SEARCH_FIELDS = ['mail','givenName','sn','sAMAccountName','memberOf', 'cn']
    BIND_USER = 'ldap'
    BIND_PASSWORD = ''

# Single Sign On
CAS = False
if CAS:
    CAS_SERVER_URL = "https://cas.cristoreyny.org:8443/cas/"
    AUTHENTICATION_BACKENDS = ('ldap_groups.accounts.backends.ActiveDirectoryGroupMembershipSSLBackend','django.contrib.auth.backends.ModelBackend','django_cas.backends.CASBackend',)
elif LDAP:
    AUTHENTICATION_BACKENDS = ('ldap_groups.accounts.backends.ActiveDirectoryGroupMembershipSSLBackend','django.contrib.auth.backends.ModelBackend',)
else:
    AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

# Google Apps Settings
GAPPS = False
if GAPPS:
    GAPPS_DOMAIN = ''
    GAPPS_USERNAME = ''
    GAPPS_PASSWORD = ''
    AUTHENTICATION_BACKENDS += ('ecwsp.google_auth.backends.GoogleAppsBackend',)

# admins get emailed if there is an error
ADMINS = (
    ('Admin', 'dburke@cristoreyny.org'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sword',
        'USER': 'sword',
        'PASSWORD': '1234',
    }
}

# This section should not normally be edited
MANAGERS = ADMINS

# SMTP server
EMAIL_HOST = 'daphne.cristoreyny.org'

# Max number of hours a student can work per day.
MAX_HOURS_DAY = 10

# Sync data to SugarCRM
SYNC_SUGAR = False

ASP = True

# Prefered file format, may be changed in user preferences.
# Default o
# o = Open Document
# m = Microsoft Binary
# x = Microsoft XML
PREFERED_FORMAT = 'o'
templateHead = os.path.dirname(os.path.abspath(''))
TEMPLATE_DIRS = os.path.join('/opt/sword/templates/')
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'
TIME_INPUT_FORMATS = ('%I:%M %p', '%I:%M%p', '%H:%M:%S', '%H:%M')
TIME_FORMAT = 'h:i A'

########################################################################
# These settings should not normally be edited. Editing them is not
# tested.
########################################################################

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
INTERNAL_IPS = ('127.0.0.1',)
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# base URL
# Example: "www.example.com"
production = False
if production:
    BASE_URL = "http://sis.cristoreyny.org"
else:
    BASE_URL = "http://127.0.0.1:8000"

MEDIA_URL = '/media/'
mediaHead = os.path.dirname(os.path.abspath(''))
MEDIA_ROOT = os.path.join(mediaHead, 'media/')

staticHead = os.path.dirname(os.path.abspath(''))
STATICFILES_DIRS = ((''),
    os.path.join(staticHead, 'static_files/'),
)

staticRootHead = os.path.dirname(os.path.abspath(''))
STATIC_ROOT = os.path.join(staticRootHead, 'static/')
#STATIC_ROOT = '/home/calli/sword/static/'
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4@=mqjpx*f$3m(1-wl6&02p#cx@*dz4_t26lu@@pmd^2%+)**y'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
   
)
if CAS:
    MIDDLEWARE_CLASSES += (
        'django_cas.middleware.CASMiddleware',
        'django.middleware.doc.XViewMiddleware',
    )

ROOT_URLCONF = 'ecwsp.urls'

INSTALLED_APPS = (
    'ajax_select',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.admindocs',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'grappelli.dashboard',
    'grappelli',
    #'ckeditor',
    'django.contrib.admin',
    'ecwsp.volunteer_track',
    'ecwsp.sis',
    'ecwsp.schedule',
    'ecwsp.work_study',
    'ecwsp.administration',
    'ecwsp.admissions',
    'ecwsp.engrade_sync',
    'ecwsp.alumni',
    #'ecwsp.omr',
    'reversion',
    'ldap_groups',
    'django.contrib.webdesign',
    'django_extensions',
    #'debug_toolbar',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',

    # required by django-admin-tools
    'django.core.context_processors.request',
    
    'ecwsp.sis.context_processors.global_stuff',
)

AJAX_LOOKUP_CHANNELS = {
    # the simplest case, pass a DICT with the model and field to search against :
    'student' : ('ecwsp.sis.lookups', 'StudentLookup'),
    'all_student' : ('ecwsp.sis.lookups', 'AllStudentLookup'),
    'dstudent' : ('ecwsp.sis.lookups', 'StudentLookupSmall'),
    'studentworker' : ('ecwsp.work_study.lookups', 'StudentLookup'),
    'faculty' : ('ecwsp.sis.lookups', 'FacultyLookup'),
    'emergency_contact' : ('ecwsp.sis.lookups', 'EmergencyContactLookup'),
    'discstudent' : ('ecwsp.sis.lookups', 'StudentWithDisciplineLookup'),
    'discipline_view_student': ('ecwsp.sis.lookups', 'DisciplineViewStudentLookup'),
    'attendance_view_student': ('ecwsp.sis.lookups', 'AttendanceStudentLookup'),
    'attendance_quick_view_student': ('ecwsp.sis.lookups', 'AttendanceAddStudentLookup'),
    'volunteer': ('ecwsp.volunteer_track.lookups', 'VolunteerLookup'),
    'site': ('ecwsp.volunteer_track.lookups', 'SiteLookup'),
    'benchmark': ('ecwsp.omr.lookups', 'BenchmarkLookup'),
    'theme': ('ecwsp.omr.lookups', 'ThemeLookup'),
}

DEBUG = True
TEMPLATE_DEBUG = DEBUG

AUTH_PROFILE_MODULE = 'sis.UserPreference'

ADMIN_TOOLS_MENU = 'ecwsp.menu.CustomMenu'
GRAPPELLI_INDEX_DASHBOARD = 'ecwsp.dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = '<img src="/static/images/logo.png"/ style="height: 30px; margin-left: -10px; margin-top: -8px; margin-bottom: -11px;">'

CKEDITOR_MEDIA_PREFIX = "/static/ckeditor/"
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT + "uploads"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [ 'Bold', 'Italic', 'Underline',
              '-', 'Image', 'Link', 'Unlink',
              '-', 'Format',
              '-', 'Maximize',
              '-', 'Table',
              '-', 'BulletedList', 'NumberedList',
              '-', 'PasteText','PasteFromWord',
            ]
        ],
        'height': 100,
        'width': 550,
        'disableNativeSpellChecker': False,
        'removePlugins': 'scayt,menubutton,contextmenu,elementspath',
        'resize_enabled': False,
    },
}

# http://ww7.engrade.com/api/key.php
ENGRADE_APITKEY = ''
# Admin user login
ENGRADE_LOGIN = ''
# Engrade password
ENGRADE_PASSWORD = ''
# School UID (admin must be connected to school)
ENGRADE_SCHOOLID = ''

# this will load additional settings from the file settings_local.py
# this is useful when managing multiple sites with different configurations
from settings_local import *