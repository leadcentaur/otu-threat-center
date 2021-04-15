from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .forms import UserUpdateForm, ProfileUpdateForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test
from users.models import Profile
from django.core.mail import send_mail
from django.core.exceptions import PermissionDenied


def legal_check(user):
    if user.legal.terms_accepted:
        return True
    raise PermissionDenied


@login_required
@require_http_methods(["GET", "POST"])
@user_passes_test(legal_check)
def profile(request):
    if request.method == "POST":

        # here we are loading both the UserUpdate form and the profileUpdate form into one,
        # this is done as we need to be able to update both models simultaneously

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            print(request.POST)

            messages.success(request, f'Your profile has been updated.')
            return redirect('profile')
        else:
            messages.error(request, f'Failed to update your profile.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/user_profile.html', context)


class ProfileDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Profile
    template_name = "users/user_profile_viewer.html"
    context_object_name = 'other_user_profile'

    def test_func(self):
        if self.request.user.legal.terms_accepted:
            return True
        return False


@require_http_methods(["GET"])
def login(request):
    return render(request, 'users/login.html')


@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('/')
