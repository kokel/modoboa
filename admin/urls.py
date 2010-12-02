from django.conf.urls.defaults import *

urlpatterns = patterns('modoboa.admin.views',
                       url(r'^$', 'domains', name="index"),
                       url(r'^domains/$', 'domains', name="domains"),
                       (r'^domains/new/', 'newdomain'),
                       (r'^domains/(?P<dom_id>\d+)/edit/$', 'editdomain'),
                       (r'^domains/(?P<dom_id>\d+)/delete/$', 'deldomain'),

                       (r'^domaliases/$', "domaliases"),
                       (r'^domaliases/new/', 'newdomalias'),
                       (r'^domaliases/edit/(?P<alias_id>\d+)/', 'editdomalias'),

                       (r'^domains/(?P<dom_id>\d+)/newmailbox/$', 'newmailbox'),
                       (r'^domains/(?P<dom_id>\d+)/editmailbox/(?P<mbox_id>\d+)/$', 'editmailbox'),
                       (r'^domains/(?P<dom_id>\d+)/deletemailbox/(?P<mbox_id>\d+)/$', 'delmailbox'),
                       (r'^domains/(?P<dom_id>\d+)/newalias/$', 'newalias'),
                       (r'^domains/(?P<dom_id>\d+)/editalias/(?P<alias_id>\d+)/$', 'editalias'),
                       (r'^domains/(?P<dom_id>\d+)/$', 'mailboxes'),
                       (r'^domains/(?P<dom_id>\d+)/raw/$', 'mailboxes_raw'),
                       url(r'^domains/(?P<dom_id>\d+)/aliases/$', "aliases", name="full-aliases"),
                       url(r'^domains/(?P<dom_id>\d+)/aliases/(?P<mbox_id>\d+)/$', "aliases", name="mbox-aliases"),
                       (r'^domains/(?P<dom_id>\d+)/delalias/(?P<alias_id>\d+)/$', 'delalias'),

                       (r'^settings/$', 'viewparameters'),
                       (r'^settings/parameters/$', 'viewparameters'),
                       (r'^settings/parameters/save/$', 'saveparameters'),
                       (r'^settings/extensions/$', 'viewextensions'),
                       (r'^settings/extensions/save/$', 'saveextensions'),

                       (r'^permissions/$', 'permissions'),
                       (r'^permissions/add/$', 'add_permission'),
                       (r'^permissions/delete/$', 'delete_permissions'),
                       )
