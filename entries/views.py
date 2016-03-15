# Core
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

# Combine query sets
from itertools import chain

# Authentication process
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Get time
from django.utils import timezone

# Ours'
from .forms import UserForm, UserProfileForm, EntryForm, UpdateEntryForm, UpdateUserForm, CommentForm, EditCommentForm, SubcommentForm, EditSubcommentForm, TwosubcommentForm, EditTwosubcommentForm, UpdateUserProfileForm
from .models import Entry, Comment, Subcomment, Twosubcomment, UserProfile
from django.contrib.auth.models import User

# Pagginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Entries sorted according to rates
def entries_home(request):
    context = {}
    user = request.user
    if user.is_active:
        all_entries_initial = Entry.objects.all().extra(order_by = ['-rate_total'])
        right_all_entries = all_entries_initial

        paginator = Paginator(all_entries_initial, 7) 
        page = request.GET.get('page')
        try:
            all_entries = paginator.page(page)
        except PageNotAnInteger:
            all_entries = paginator.page(1)
        except EmptyPage:
            all_entries = paginator.page(paginator.num_pages)  

        up_entries = user.up_entries.all()
        down_entries = user.down_entries.all()
        context = {'all_entries': all_entries, 
                   'user':user,
                   'up_entries': up_entries,
                   'down_entries': down_entries,
                   'right_all_entries': right_all_entries,}
    return render(request, 'entries/entries_home.html', context)

# Entries sorted according to views
def entries_popular(request):
    context = {}
    user = request.user
    if user.is_active:
        all_entries_initial = Entry.objects.all().extra(order_by = ['-views'])
        right_all_entries = all_entries_initial

        paginator = Paginator(all_entries_initial, 7) 
        page = request.GET.get('page')
        try:
            all_entries = paginator.page(page)
        except PageNotAnInteger:
            all_entries = paginator.page(1)
        except EmptyPage:
            all_entries = paginator.page(paginator.num_pages)

        up_entries = user.up_entries.all()
        down_entries = user.down_entries.all()
        context = {'all_entries': all_entries, 
                   'user':user,
                   'up_entries': up_entries,
                   'down_entries': down_entries,
                   'right_all_entries': right_all_entries,}
    return render(request, 'entries/entries_home.html', context)

# Entries sorted according to created_date
def entries_new(request):
    context = {}
    user = request.user
    if user.is_active:
        all_entries_initial = Entry.objects.all().extra(order_by = ['-created_date'])
        right_all_entries = all_entries_initial

        paginator = Paginator(all_entries_initial, 7) 
        page = request.GET.get('page')
        try:
            all_entries = paginator.page(page)
        except PageNotAnInteger:
            all_entries = paginator.page(1)
        except EmptyPage:
            all_entries = paginator.page(paginator.num_pages)

        up_entries = user.up_entries.all()
        down_entries = user.down_entries.all()
        context = {'all_entries': all_entries, 
                   'user':user,
                   'up_entries': up_entries,
                   'down_entries': down_entries,
                   'right_all_entries': right_all_entries,}
    return render(request, 'entries/entries_home.html', context)

# Entries sorted according to user interaction
def entries_involved(request):
    context = {}
    user = request.user
    if user.is_active:
        up_entries = user.up_entries.all()
        down_entries = user.down_entries.all()
        all_entries_initial  = list(chain(up_entries, down_entries))
        right_all_entries = all_entries_initial

        paginator = Paginator(all_entries_initial, 7) 
        page = request.GET.get('page')
        try:
            all_entries = paginator.page(page)
        except PageNotAnInteger:
            all_entries = paginator.page(1)
        except EmptyPage:
            all_entries = paginator.page(paginator.num_pages)

        context = {'all_entries': all_entries, 
                   'user':user,
                   'up_entries': up_entries,
                   'down_entries': down_entries,
                   'right_all_entries': right_all_entries,}
    return render(request, 'entries/entries_home.html', context)
    
# Look Entries in detail
def entry_detail(request, pk):
    user = request.user
    entry = get_object_or_404(Entry, pk=pk)
    comments = Comment.objects.filter(entry=entry).extra(order_by = ['-rate_total'])        
    entry.views += 1
    entry.save()
    all_entries = Entry.objects.all().extra(order_by = ['-rate_total'])
    up_comments = user.up_comments.all()
    down_comments = user.down_comments.all()
    up_entries = user.up_entries.all()
    down_entries = user.down_entries.all()
    up_subcomments = user.up_subcomments.all()
    down_subcomments = user.down_subcomments.all()
    up_twosubcomments = user.up_twosubcomments.all()
    down_twosubcomments = user.down_twosubcomments.all()
    subcomment_form = SubcommentForm()
    twosubcomment_form = TwosubcommentForm()

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
               'down_entries': down_entries,
               'subcomment_form': subcomment_form,
               'up_subcomments': up_subcomments,
               'down_subcomments': down_subcomments,
               'up_twosubcomments': up_twosubcomments,
               'down_twosubcomments': down_twosubcomments,
               'twosubcomment_form': twosubcomment_form,}

    return render(request, 'entries/entry_detail.html', context)

# Create new subcomment
def new_subcomment(request, pk, pks):
    comment = get_object_or_404(Comment, pk=pks)
    entry = get_object_or_404(Entry, pk=pk)
    user = request.user

    if request.method == 'POST':
        form  = SubcommentForm(data=request.POST)
        if form.is_valid():
            subcomment = form.save(commit=False)
            subcomment.author = user
            subcomment.comment = comment
            subcomment.entry = entry
            subcomment.rate_up = 1
            subcomment.rate_total = 1
            subcomment.save()
            subcomment.up_voters.add(user)
            subcomment.save()
            return HttpResponseRedirect('/entry/' + pk)
    else:
        return HttpResponseRedirect('/entry/' + pk)

# Create new twosubcomment
def new_twosubcomment(request, pk, pks, pkss):
    subcomment = get_object_or_404(Subcomment, pk=pkss)
    comment = get_object_or_404(Comment, pk=pks)
    entry = get_object_or_404(Entry, pk=pk)
    user = request.user

    if request.method == 'POST':
        form  = TwosubcommentForm(data=request.POST)
        if form.is_valid():
            twosubcomment = form.save(commit=False)
            twosubcomment.author = user
            twosubcomment.subcomment = subcomment
            twosubcomment.comment = comment
            twosubcomment.entry = entry
            twosubcomment.rate_up = 1
            twosubcomment.rate_total = 1
            twosubcomment.save()
            twosubcomment.up_voters.add(user)
            twosubcomment.save()
            return HttpResponseRedirect('/entry/' + pk)
    else:
        return HttpResponseRedirect('/entry/' + pk)

# User registration and authentication process
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.avatar = request.FILES.get('avatar', None)
            # if profile.avatar == None:
            #     profile.avatar = 'img/avatar.png'
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
    return HttpResponseRedirect('/') # END OF User registration and authentication process 

# Submit new entry
# @login_required
def new_entry(request):
    user = request.user
    if request.method == 'POST':
        form  = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = user
            entry.rate_up = 1
            entry.rate_total = 1
            entry.thumbnail = request.FILES.get('thumbnail', None)
            # if entry.thumbnail == None:
            #    entry.thumbnail = 'img/thumbnail.png'
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
            form = UpdateEntryForm(request.POST, request.FILES, instance=entry)
            if form.is_valid():
                edited_entry = form.save(commit=False)
                edited_entry.edited = True
                edited_entry.updated_date = timezone.now()
                edited_entry.save()
                edited_entry.thumbnail = request.FILES.get('thumbnail', None)
                if edited_entry.thumbnail != None:
                    edited_entry.save()
                    # edited_entry.thumbnail = 'img/thumbnail.png'
                
                return HttpResponseRedirect('/entry/' + str(entry.pk))
        else:
            form = UpdateEntryForm(instance=entry)

        return render(request,'entries/update_entry.html', {'form': form, 'entry': entry})
    else:
        return HttpResponseRedirect('/')

# Update existing user
def update_user(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    user_profile = get_object_or_404(UserProfile, user=user)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=user)
        profile_form = UpdateUserProfileForm(request.POST, request.FILES, instance=user_profile)
        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save()
            profile.avatar = request.FILES.get('avatar', None)
            if profile.avatar != None:
                profile.save()
            return HttpResponseRedirect('/')
    else:
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateUserProfileForm(instance=user_profile)
    return render(request,'entries/update_user.html', {
                   'user_form': user_form, 
                   'profile_form': profile_form,
                   'user_profile': user_profile,})

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

# Update existing Subcomment
def edit_subcomment(request, pk):
    subcomment = get_object_or_404(Subcomment, pk=pk)
    entry = subcomment.entry
    entry_pk = entry.pk
    if subcomment.author == request.user:
        if request.method == 'POST':
            form = EditSubcommentForm(request.POST, instance=subcomment)
            if form.is_valid():
                edited_subcomment = form.save(commit=False)
                edited_subcomment.edited = True
                edited_subcomment.updated_date = timezone.now()
                edited_subcomment.save()
                return HttpResponseRedirect('/entry/' + str(entry_pk))
        else:
            form = EditSubcommentForm(instance=subcomment)

        return render(request,'entries/edit_subcomment.html', {'form': form, 'subcomment': subcomment})
    else:
        return HttpResponseRedirect('/')

# Delete Entry
def delete_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    entry.delete()
    return HttpResponseRedirect('/')

# Delete Comment
def delete_comment(request, pk, pks):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return HttpResponseRedirect('/entry/' + pks)

# Delete Subcomment
def delete_subcomment(request, pk, pks):
    subcomment = get_object_or_404(Subcomment, pk=pk)
    subcomment.delete()
    return HttpResponseRedirect('/entry/' + pks)

# Delete Twosubcomment
def delete_twosubcomment(request, pk, pks):
    twosubcomment = get_object_or_404(Twosubcomment, pk=pk)
    twosubcomment.delete()
    return HttpResponseRedirect('/entry/' + pks)

# Update existing Twosubcomment
def edit_twosubcomment(request, pk):
    twosubcomment = get_object_or_404(Twosubcomment, pk=pk)
    entry = twosubcomment.entry
    entry_pk = entry.pk
    if twosubcomment.author == request.user:
        if request.method == 'POST':
            form = EditTwosubcommentForm(request.POST, instance=twosubcomment)
            if form.is_valid():
                edited_twosubcomment = form.save(commit=False)
                edited_twosubcomment.edited = True
                edited_twosubcomment.updated_date = timezone.now()
                edited_twosubcomment.save()
                return HttpResponseRedirect('/entry/' + str(entry_pk))
        else:
            form = EditTwosubcommentForm(instance=twosubcomment)

        return render(request,'entries/edit_twosubcomment.html', {'form': form, 'twosubcomment': twosubcomment})
    else:
        return HttpResponseRedirect('/')

# AJAX search
def entry_search(request):
    if request.method == 'POST':
        text_search = request.POST['text_search']
        if text_search == '':
            text_search = '✗'
            # print(text_search)
    else:
        text_search = None
    founded_entries = Entry.objects.filter(title__icontains=text_search)
    return render(request, 'entries/ajax_search.html', {'founded_entries': founded_entries,})

# Voting process of entries
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
    return HttpResponse(status=204) # END OF voting process of entries

# Voting process of comments
def comment_vote_up(request, pk):
    # Do this to every vote function
    # if request.method == 'POST':
    #     user = request.user
    #     comment = get_object_or_404(Comment, pk=pk)
    #     comment.rate_up += 1
    #     comment.rate_total = comment.rate_up + comment.rate_down
    #     user.down_comments.remove(comment)
    #     user.up_comments.add(comment)
    #     comment.save()
    #     user.save()
    #     return HttpResponse(status=204)
    # else:
    #     return HttpResponse(status=204)
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
    return HttpResponse(status=204) # END OF voting process of comments

# Voting process of subcomments
def subcomment_vote_up(request, pk):
    user = request.user
    subcomment = get_object_or_404(Subcomment, pk=pk)
    subcomment.rate_up += 1
    subcomment.rate_total = subcomment.rate_up + subcomment.rate_down
    user.down_subcomments.remove(subcomment)
    user.up_subcomments.add(subcomment)
    subcomment.save()
    user.save()
    return HttpResponse(status=204)

def subcomment_vote_up2(request, pk):
    user = request.user
    subcomment = get_object_or_404(Subcomment, pk=pk)
    subcomment.rate_up -= 1
    subcomment.rate_total = subcomment.rate_up + subcomment.rate_down
    user.up_subcomments.remove(subcomment)
    subcomment.save()
    user.save()
    return HttpResponse(status=204)

def subcomment_vote_up3(request, pk):
    user = request.user
    subcomment = get_object_or_404(Subcomment, pk=pk)
    subcomment.rate_up += 2
    subcomment.rate_total = subcomment.rate_up + subcomment.rate_down
    user.down_subcomments.remove(subcomment)
    user.up_subcomments.add(subcomment)
    user.save()
    subcomment.save()
    return HttpResponse(status=204)

def subcomment_vote_down(request, pk):
    user = request.user
    subcomment = get_object_or_404(Subcomment, pk=pk)
    subcomment.rate_down -= 1
    subcomment.rate_total = subcomment.rate_up + subcomment.rate_down
    user.up_subcomments.remove(subcomment)
    user.down_subcomments.add(subcomment)
    user.save()
    subcomment.save()
    return HttpResponse(status=204)

def subcomment_vote_down2(request, pk):
    user = request.user
    subcomment = get_object_or_404(Subcomment, pk=pk)
    subcomment.rate_down += 1
    subcomment.rate_total = subcomment.rate_up + subcomment.rate_down
    user.up_subcomments.remove(subcomment)
    user.down_subcomments.remove(subcomment)
    user.save()
    subcomment.save()
    return HttpResponse(status=204)

def subcomment_vote_down3(request, pk):
    user = request.user
    subcomment = get_object_or_404(Subcomment, pk=pk)
    subcomment.rate_up -= 2
    subcomment.rate_total = subcomment.rate_up + subcomment.rate_down
    user.up_subcomments.remove(subcomment)
    user.down_subcomments.add(subcomment)
    user.save()
    subcomment.save()
    return HttpResponse(status=204) # END OF voting process of subcomments

#Voting process of twosubcomments
def twosubcomment_vote_up(request, pk):
    user = request.user
    twosubcomment = get_object_or_404(Twosubcomment, pk=pk)
    twosubcomment.rate_up += 1
    twosubcomment.rate_total = twosubcomment.rate_up + twosubcomment.rate_down
    user.down_twosubcomments.remove(twosubcomment)
    user.up_twosubcomments.add(twosubcomment)
    twosubcomment.save()
    user.save()
    return HttpResponse(status=204)

def twosubcomment_vote_up2(request, pk):
    user = request.user
    twosubcomment = get_object_or_404(Twosubcomment, pk=pk)
    twosubcomment.rate_up -= 1
    twosubcomment.rate_total = twosubcomment.rate_up + twosubcomment.rate_down
    user.up_twosubcomments.remove(twosubcomment)
    twosubcomment.save()
    user.save()
    return HttpResponse(status=204)

def twosubcomment_vote_up3(request, pk):
    user = request.user
    twosubcomment = get_object_or_404(Twosubcomment, pk=pk)
    twosubcomment.rate_up += 2
    twosubcomment.rate_total = twosubcomment.rate_up + twosubcomment.rate_down
    user.down_twosubcomments.remove(twosubcomment)
    user.up_twosubcomments.add(twosubcomment)
    user.save()
    twosubcomment.save()
    return HttpResponse(status=204)

def twosubcomment_vote_down(request, pk):
    user = request.user
    twosubcomment = get_object_or_404(Twosubcomment, pk=pk)
    twosubcomment.rate_down -= 1
    twosubcomment.rate_total = twosubcomment.rate_up + twosubcomment.rate_down
    user.up_twosubcomments.remove(twosubcomment)
    user.down_twosubcomments.add(twosubcomment)
    user.save()
    twosubcomment.save()
    return HttpResponse(status=204)

def twosubcomment_vote_down2(request, pk):
    user = request.user
    twosubcomment = get_object_or_404(Twosubcomment, pk=pk)
    twosubcomment.rate_down += 1
    twosubcomment.rate_total = twosubcomment.rate_up + twosubcomment.rate_down
    user.up_twosubcomments.remove(twosubcomment)
    user.down_twosubcomments.remove(twosubcomment)
    user.save()
    twosubcomment.save()
    return HttpResponse(status=204)

def twosubcomment_vote_down3(request, pk):
    user = request.user
    twosubcomment = get_object_or_404(Twosubcomment, pk=pk)
    twosubcomment.rate_up -= 2
    twosubcomment.rate_total = twosubcomment.rate_up + twosubcomment.rate_down
    user.up_twosubcomments.remove(twosubcomment)
    user.down_twosubcomments.add(twosubcomment)
    user.save()
    twosubcomment.save()
    return HttpResponse(status=204) # END OF voting process of twosubcomments