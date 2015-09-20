# Core
from django.conf.urls import include, url

# Ours
from . import views

urlpatterns = [

    # Entries sorted according to rates
    url(r'^$', views.entries_home, name='entries_home'),

    # Entries sorted accordingly
    url(r'^popular/$', views.entries_popular, name='entries_popular'),
    url(r'^new/$', views.entries_new, name='entries_new'),
    url(r'^involved/$', views.entries_involved, name='entries_involved'),

    # Look Entries in detail
    url(r'^entry/(?P<pk>[0-9]+)/$', views.entry_detail, name='entry_detail'),
    
    # User registration and authentication process
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'entries/login.html',},  name='login'),

    # Submit new entry
    url(r'^new_entry/', views.new_entry, name='new_entry'),

    # For voting process
    url(r'^entry/(?P<pk>[0-9]+)/vote_up$', views.entry_vote_up, name='entry_vote_up'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_up2$', views.entry_vote_up2, name='entry_vote_up2'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_up3$', views.entry_vote_up3, name='entry_vote_up3'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_down$', views.entry_vote_down, name='entry_vote_down'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_down2$', views.entry_vote_down2, name='entry_vote_down2'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_down3$', views.entry_vote_down3, name='entry_vote_down3'),
]