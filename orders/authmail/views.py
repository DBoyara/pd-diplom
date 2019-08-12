from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from .forms import UserSignupForm


def signup_views(request):

    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return HttpResponseRedirect(reverse('base'))
    else:
        user_form = UserSignupForm()
    return render(request, 'authmail/signup.html', {'user_form': user_form})
