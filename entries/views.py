# Core
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Combine query sets
from itertools import chain

# Authentication process
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Get time now
from django.utils import timezone

# Ours
from .forms import UserForm, UserProfileForm, EntryForm, UpdateEntryForm, UpdateUserForm, CommentForm, EditCommentForm
from .models import Entry, Comment

# Entries sorted according to rates
def entries_home(request):
    context = {}
    user = request.user
    if user.is_active:
        all_entries = Entry.objects.all().extra(order_by = ['-rate_total'])
        up_entries = user.up_entries.all()
        down_entries = user.down_entries.all()
        context = {'all_entries': all_entries, 
                   'user':user,
                   'up_entries': up_entries,
                   'down_entries': down_entries, }
    return render(request, 'entries/entries_home.html', context)

# Entries sorted according to views
def entries_popular(request):
    context = {}
    user = request.user
    if user.is_active:
        all_entries = Entry.objects.all().extra(order_by = ['-views'])
        up_entries = user.up_entries.all()
        down_entries = user.down_entries.all()
        context = {'all_entries': all_entries, 
                   'user':user,
                   'up_entries': up_entries,
                   'down_entries': down_entries,}
    return render(request, 'entries/entries_home.html', context)

# Entries sorted according to created date
def entries_new(request):
    context = {}
    user = request.user
    if user.is_active:
        all_entries = Entry.objects.all().extra(order_by = ['-created_date'])
        up_entries = user.up_entries.all()
        down_entries = user.down_entries.all()
        context = {'all_entries': all_entries, 
                   'user':user,
                   'up_entries': up_entries,
                   'down_entries': down_entries,}
    return render(request, 'entries/entries_home.html', context)

# Entries sorted according to user interaction
def entries_involved(request):
    context = {}
    user = request.user
    if user.is_active:
        up_entries = user.up_entries.all()
        down_entries = user.down_entries.all()
        all_entries  = list(chain(up_entries, down_entries))
        context = {'all_entries': all_entries, 
                   'user':user,
                   'up_entries': up_entries,
                   'down_entries': down_entries,}
    return render(request, 'entries/entries_home.html', context)
    
# Look Entries in detail
def entry_detail(request, pk):
    user = request.user
    entry = get_object_or_404(Entry, pk=pk)
    comments = Comment.objects.filter(entry=entry).extra(order_by = ['-rate_total'])
    
    # for comment in comments:
        
    entry.views += 1
    entry.save()
    all_entries = Entry.objects.all().extra(order_by = ['-rate_total'])
    up_comments = user.up_comments.all()
    down_comments = user.down_comments.all()
    up_entries = user.up_entries.all()
    down_entries = user.down_entries.all()

    if request.method == 'POST':
        form  = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = user
            comment.entry = entry
            comment.rate_up = 1
            comment.rate_total = 1
            comment.save()
            comment.up_voters.add(user)
            comment.save()
            return HttpResponseRedirect('/entry/' + pk)
    else:
        form = CommentForm()

    context = {'entry': entry, 
               'all_entries': all_entries,
               'comments': comments,
               'form': form,
               'up_comments': up_comments,
               'down_comments': down_comments,
               'up_entries': up_entries,
               'down_entries': down_entries,}

    return render(request, 'entries/entry_detail.html', context)

# User registration and authentication process
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

# Submit new entry
@login_required
def new_entry(request):
    user = request.user
    if request.method == 'POST':
        form  = EntryForm(data=request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = user
            entry.rate_up = 1
            entry.rate_total = 1
            entry.save()
            entry.up_voters.add(user)
            entry.save()
            return HttpResponseRedirect('/')
    else:
        form  = EntryForm()
    return render(request,'entries/new_entry.html', {'form': form})

# Update existing entry
def update_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if entry.author == request.user:
        if request.method == 'POST':
            form = UpdateEntryForm(request.POST, instance=entry)
            if form.is_valid():
                edited_entry = form.save(commit=False)
                edited_entry.edited = True
                edited_entry.updated_date = timezone.now()
                edited_entry.save()
                return HttpResponseRedirect('/entry/' + str(entry.pk))
        else:
            form = UpdateEntryForm(instance=entry)

        return render(request,'entries/update_entry.html', {'form': form, 'entry': entry})
    else:
        return HttpResponseRedirect('/')

# Update existing user
def update_user(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request,'entries/update_user.html', {'form': form})

# Update existing comment
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    entry = comment.entry
    entry_pk = entry.pk
    if comment.author == request.user:
        if request.method == 'POST':
            form = EditCommentForm(request.POST, instance=comment)
            if form.is_valid():
                edited_comment = form.save(commit=False)
                edited_comment.edited = True
                edited_comment.updated_date = timezone.now()
                edited_comment.save()
                return HttpResponseRedirect('/entry/' + str(entry_pk))
        else:
            form = EditCommentForm(instance=comment)

        return render(request,'entries/edit_comment.html', {'form': form, 'comment': comment})
    else:
        return HttpResponseRedirect('/')

# For voting process of ENTRIES
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

# For voting process of COMMENTS
def comment_vote_up(request, pk):
    user = request.user
    comment = get_object_or_404(Comment, pk=pk)
    comment.rate_up += 1
    comment.rate_total = comment.rate_up + comment.rate_down
    user.down_comments.remove(comment)
    user.up_comments.add(comment)
    comment.save()
    user.save()
    return HttpResponse(status=204)

def comment_vote_up2(request, pk):
    user = request.user
    comment = get_object_or_404(Comment, pk=pk)
    comment.rate_up -= 1
    comment.rate_total = comment.rate_up + comment.rate_down
    user.up_comments.remove(comment)
    comment.save()
    user.save()
    return HttpResponse(status=204)

def comment_vote_up3(request, pk):
    user = request.user
    comment = get_object_or_404(Comment, pk=pk)
    comment.rate_up += 2
    comment.rate_total = comment.rate_up + comment.rate_down
    user.down_comments.remove(comment)
    user.up_comments.add(comment)
    user.save()
    comment.save()
    return HttpResponse(status=204)

def comment_vote_down(request, pk):
    user = request.user
    comment = get_object_or_404(Comment, pk=pk)
    comment.rate_down -= 1
    comment.rate_total = comment.rate_up + comment.rate_down
    user.up_comments.remove(comment)
    user.down_comments.add(comment)
    user.save()
    comment.save()
    return HttpResponse(status=204)

def comment_vote_down2(request, pk):
    user = request.user
    comment = get_object_or_404(Comment, pk=pk)
    comment.rate_down += 1
    comment.rate_total = comment.rate_up + comment.rate_down
    user.up_comments.remove(comment)
    user.down_comments.remove(comment)
    user.save()
    comment.save()
    return HttpResponse(status=204)

def comment_vote_down3(request, pk):
    user = request.user
    comment = get_object_or_404(Comment, pk=pk)
    comment.rate_up -= 2
    comment.rate_total = comment.rate_up + comment.rate_down
    user.up_comments.remove(comment)
    user.down_comments.add(comment)
    user.save()
    comment.save()
    return HttpResponse(status=204)
