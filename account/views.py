from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
from account.forms import UserRegistrationForm
from account.models import Profile


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


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
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})
