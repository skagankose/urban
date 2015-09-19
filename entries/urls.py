from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.entries_home, name='entries_home'),
    url(r'^popular/$', views.entries_popular, name='entries_popular'),
    url(r'^new/$', views.entries_new, name='entries_new'),
    url(r'^involved/$', views.entries_involved, name='entries_involved'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^restricted/', views.restricted, name='restricted'),

    url(r'^entry/(?P<pk>[0-9]+)/$', views.entry_detail, name='entry_detail'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_up$', views.entry_vote_up, name='entry_vote_up'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_up2$', views.entry_vote_up2, name='entry_vote_up2'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_up3$', views.entry_vote_up3, name='entry_vote_up3'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_down$', views.entry_vote_down, name='entry_vote_down'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_down2$', views.entry_vote_down2, name='entry_vote_down2'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_down3$', views.entry_vote_down3, name='entry_vote_down3'),

]