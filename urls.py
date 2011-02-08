import os

from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

BASEDIR = os.path.abspath(os.path.dirname(__file__))

urlpatterns = patterns('',
    (r'^admin/', admin.site.urls),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/media/'}),
    (r'^$', 'encurtador.views.index'),
    (r'^post_link/$', 'encurtador.views.post_link'),
)
