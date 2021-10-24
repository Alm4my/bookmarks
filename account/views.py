from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from django.views.decorators.http import require_POST

from account.forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from account.models import Profile
from actions.models import Action
from actions.utils import create_action
from common.decorators import ajax_required
from images.models import Contact


@login_required
def dashboard(request):
    # Display all actions by default
    actions = Action.objects.all()
    following_ids = request.user.following.values_list('id', flat=True)
    if following_ids:
        # if user is following others, retrieve only their actions
        actions = actions.filter(user_id__in=following_ids)
    actions = actions.select_related('user', 'user__profile')[:10]
    return render(request, 'account/dashboard.html', {'section': 'dashboard',
                                                      'actions': actions})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object without saving it
            new_user = user_form.save(commit=False)
            # set the new chosen password
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            # save the User object
            new_user.save()
            # create user profile
            Profile.objects.create(user=new_user)
            create_action(new_user, 'has created an account')
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    # messages.success(request, 'YEAH')
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form,
                                                 'profile_form': profile_form})


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html', {'section': 'people',
                                                      'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people',
                                                        'user': user})


@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
                create_action(request.user, 'has unfollowed', user)

        except User.DoesNotExist:
            return JsonResponse({'status': 'error'})
        else:
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})
