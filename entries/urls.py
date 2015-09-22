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

    # Submit new subcomment
    url(r'^new_subcomment/(?P<pk>[0-9]+)/(?P<pks>[0-9]+)$', views.new_subcomment, name='new_subcomment'),

    # Submit new twosubcomment
    url(r'^new_twosubcomment/(?P<pk>[0-9]+)/(?P<pks>[0-9]+)/(?P<pkss>[0-9]+)$', views.new_twosubcomment, name='new_twosubcomment'),

    # Edit existing entry
    url(r'^update_entry/(?P<pk>[0-9]+)/$', views.update_entry, name='update_entry'),

    # Edit existing comment
    url(r'^edit_comment/(?P<pk>[0-9]+)/$', views.edit_comment, name='edit_comment'),

    # Edit existing Subcomment
    url(r'^edit_subcomment/(?P<pk>[0-9]+)/$', views.edit_subcomment, name='edit_subcomment'),

    # Edit existing Twosubcomment
    url(r'^edit_twosubcomment/(?P<pk>[0-9]+)/$', views.edit_twosubcomment, name='edit_twosubcomment'),

    # Edit existing user
    url(r'^update_user/$', views.update_user, name='update_user'),

    # For voting process of entries
    url(r'^entry/(?P<pk>[0-9]+)/vote_up$', views.entry_vote_up, name='entry_vote_up'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_up2$', views.entry_vote_up2, name='entry_vote_up2'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_up3$', views.entry_vote_up3, name='entry_vote_up3'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_down$', views.entry_vote_down, name='entry_vote_down'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_down2$', views.entry_vote_down2, name='entry_vote_down2'),
    url(r'^entry/(?P<pk>[0-9]+)/vote_down3$', views.entry_vote_down3, name='entry_vote_down3'),

    # For voting process of comment
    url(r'^comment/(?P<pk>[0-9]+)/vote_up$', views.comment_vote_up, name='comment_vote_up'),
    url(r'^comment/(?P<pk>[0-9]+)/vote_up2$', views.comment_vote_up2, name='comment_vote_up2'),
    url(r'^comment/(?P<pk>[0-9]+)/vote_up3$', views.comment_vote_up3, name='comment_vote_up3'),
    url(r'^comment/(?P<pk>[0-9]+)/vote_down$', views.comment_vote_down, name='comment_vote_down'),
    url(r'^comment/(?P<pk>[0-9]+)/vote_down2$', views.comment_vote_down2, name='comment_vote_down2'),
    url(r'^comment/(?P<pk>[0-9]+)/vote_down3$', views.comment_vote_down3, name='comment_vote_down3'),

    # For voting process of subcomments
    url(r'^subcomment/(?P<pk>[0-9]+)/vote_up$', views.subcomment_vote_up, name='subcomment_vote_up'),
    url(r'^subcomment/(?P<pk>[0-9]+)/vote_up2$', views.subcomment_vote_up2, name='subcomment_vote_up2'),
    url(r'^subcomment/(?P<pk>[0-9]+)/vote_up3$', views.subcomment_vote_up3, name='subcomment_vote_up3'),
    url(r'^subcomment/(?P<pk>[0-9]+)/vote_down$', views.subcomment_vote_down, name='subcomment_vote_down'),
    url(r'^subcomment/(?P<pk>[0-9]+)/vote_down2$', views.subcomment_vote_down2, name='subcomment_vote_down2'),
    url(r'^subcomment/(?P<pk>[0-9]+)/vote_down3$', views.subcomment_vote_down3, name='subcomment_vote_down3'),

    # For voting process of twosubcomments
    url(r'^twosubcomment/(?P<pk>[0-9]+)/vote_up$', views.twosubcomment_vote_up, name='twosubcomment_vote_up'),
    url(r'^twosubcomment/(?P<pk>[0-9]+)/vote_up2$', views.twosubcomment_vote_up2, name='twosubcomment_vote_up2'),
    url(r'^twosubcomment/(?P<pk>[0-9]+)/vote_up3$', views.twosubcomment_vote_up3, name='twosubcomment_vote_up3'),
    url(r'^twosubcomment/(?P<pk>[0-9]+)/vote_down$', views.twosubcomment_vote_down, name='twosubcomment_vote_down'),
    url(r'^twosubcomment/(?P<pk>[0-9]+)/vote_down2$', views.twosubcomment_vote_down2, name='twosubcomment_vote_down2'),
    url(r'^twosubcomment/(?P<pk>[0-9]+)/vote_down3$', views.twosubcomment_vote_down3, name='twosubcomment_vote_down3'),
]