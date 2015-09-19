from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from entries.models import Entry
from django.http import HttpResponse, HttpResponseRedirect
from itertools import chain
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

## to do
## -create entry
## -add photos to entries and videos
## -crispy forms
## -redux registration
## -login locations
## -sent email
## -look edit profile and entry
## comments

def entries_home(request):
    context = {}
    user = request.user
    if user.is_active:
        time_now = timezone.now()
        all_entries = Entry.objects.all()
        all_entries = all_entries.extra(order_by = ['-rate_total'])
        up_entries = user.up_entries.all()
        down_entries = user.down_entries.all()
        context = {'time_now': time_now, 
                   'all_entries': all_entries, 
                   'user':user,
                   'up_entries': up_entries,
                   'down_entries': down_entries, }
    return render(request, 'entries/entries_home.html', context)

def entries_popular(request):
    context = {}
    user = request.user
    if user.is_active:
        time_now = timezone.now()
        all_entries = Entry.objects.all()
        all_entries = all_entries.extra(order_by = ['-views'])
        up_entries = user.up_entries.all()
        down_entries = user.down_entries.all()
        context = {'time_now': time_now, 
                   'all_entries': all_entries, 
                   'user':user,
                   'up_entries': up_entries,
                   'down_entries': down_entries, }
    return render(request, 'entries/entries_home.html', context)

def entries_new(request):
    time_now = timezone.now()
    all_entries = Entry.objects.all()
    all_entries = all_entries.extra(order_by = ['-created_date'])
    user = request.user
    up_entries = user.up_entries.all()
    down_entries = user.down_entries.all()
    context = {'time_now': time_now, 
               'all_entries': all_entries, 
               'user':user,
               'up_entries': up_entries,
               'down_entries': down_entries, }
    return render(request, 'entries/entries_home.html', context)

def entries_involved(request):
    time_now = timezone.now()
    user = request.user
    all_entries  = list(chain(user.up_entries.all(), user.down_entries.all()))
    up_entries = user.up_entries.all()
    down_entries = user.down_entries.all()
    context = {'time_now': time_now, 
               'all_entries': all_entries, 
               'user':user,
               'up_entries': up_entries,
               'down_entries': down_entries, }
    return render(request, 'entries/entries_home.html', context)
    
def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    entry.views += 1
    entry.save()
    all_entries = Entry.objects.all()
    all_entries = all_entries.extra(order_by = ['-rate_total'])
    context = {'entry': entry, 'all_entries': all_entries}
    return render(request, 'entries/entry_detail.html', context)

def entry_vote_up(request, pk):
    user = request.user
    entry = get_object_or_404(Entry, pk=pk)
    entry.rate_up += 1
    entry.rate_total = entry.rate_up + entry.rate_down
    user.down_entries.remove(entry)
    user.up_entries.add(entry)
    entry.save()
    user.save()
    return HttpResponse(status=204)

def entry_vote_up2(request, pk):
    user = request.user
    entry = get_object_or_404(Entry, pk=pk)
    entry.rate_up -= 1
    entry.rate_total = entry.rate_up + entry.rate_down
    user.up_entries.remove(entry)
    entry.save()
    user.save()
    return HttpResponse(status=204)

def entry_vote_up3(request, pk):
    user = request.user
    entry = get_object_or_404(Entry, pk=pk)
    entry.rate_up += 2
    entry.rate_total = entry.rate_up + entry.rate_down
    user.down_entries.remove(entry)
    user.up_entries.add(entry)
    user.save()
    entry.save()
    return HttpResponse(status=204)

def entry_vote_down(request, pk):
    user = request.user
    entry = get_object_or_404(Entry, pk=pk)
    entry.rate_down -= 1
    entry.rate_total = entry.rate_up + entry.rate_down
    user.up_entries.remove(entry)
    user.down_entries.add(entry)
    user.save()
    entry.save()
    return HttpResponse(status=204)

def entry_vote_down2(request, pk):
    user = request.user
    entry = get_object_or_404(Entry, pk=pk)
    entry.rate_down += 1
    entry.rate_total = entry.rate_up + entry.rate_down
    user.up_entries.remove(entry)
    user.down_entries.remove(entry)
    user.save()
    entry.save()
    return HttpResponse(status=204)

def entry_vote_down3(request, pk):
    user = request.user
    entry = get_object_or_404(Entry, pk=pk)
    entry.rate_up -= 2
    entry.rate_total = entry.rate_up + entry.rate_down
    user.up_entries.remove(entry)
    user.down_entries.add(entry)
    user.save()
    entry.save()
    return HttpResponse(status=204)

## Login Logout, look again
def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'entries/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'entries/login.html', {})

def user_logout(request):

    logout(request)
    return HttpResponseRedirect('/')

## Restricted page example
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")