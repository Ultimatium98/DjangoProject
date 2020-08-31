from django.shortcuts import render, redirect
from .forms import RegisterForm, UserProfileForm
from blog.views import get_ip_address


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.ip = get_ip_address(request)
            profile.user = user
            profile.save()
            return redirect("/")
        else:
            print(profile_form.errors)
    else:
        form = RegisterForm()
        profile_form = UserProfileForm(initial={'ip': get_ip_address(request)})
    return render(request, "registration/register.html", {'form': form, 'profile_form': profile_form})
