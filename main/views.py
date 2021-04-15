from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Report, Target
from django.forms import modelformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from .forms import ReportSubmitForm
from django.contrib.auth.models import User
from main.models import Report
from collections import Counter
from users.models import Profile, Legal
from .forms import LegalForm, SetUserNameUponSignup
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


def legal_check(user):
    if user.legal.terms_accepted:
        return True
    raise PermissionDenied


# from .models import ReportImages
@require_http_methods(["GET", "POST"])
def overview(request):
    if request.method == "POST" and request.user.is_authenticated:
        l_form = LegalForm(request.POST, instance=request.user)
        n_form = SetUserNameUponSignup(request.POST, instance=request.user.profile)

        # check that the username the user has set is valid
        if n_form.is_valid() and l_form.is_valid():
            if 'Accept' in request.POST:
                print("Terms accepted.")

                send_mail(
                    'OTU ThreatCenter - SignUp confirmation',
                    f'Hi {request.user.first_name}, Thank you for registering for the OTU Threat Center. Happy hunting :)',
                    'tester30009@gmail.com',
                    [f'{request.user.email}'],
                    fail_silently=False,
                )

                request.user.legal.terms_accepted = True
                request.user.legal.save()
                n_form.save()
                l_form.save()

                messages.success(request, f'Thank you for registering. A verification email has been sent.')

            else:
                print("Terms declined.")
                request.user.legal.terms_accepted = False
                request.user.legal.save()

    n_form = SetUserNameUponSignup()
    l_form = LegalForm()
    # pass the system reports and the leader board to the page context
    context = {
        'l_form': l_form,
        'n_form': n_form
    }

    return render(request, 'main/overview.html', context)


@login_required
@require_http_methods(["GET"])
@user_passes_test(legal_check)
def reports_page(request):
    report_most_common = []

    # get all of the reports on the system
    system_reports = Report.objects.all()

    # get the reports for the current user
    user_reports = Report.objects.filter(author=request.user.profile)
    print(user_reports)

    # get the user data and its labels
    user_graph_data = Counter(x.get_classification_display() for x in user_reports).most_common()
    user_graph_labels = [i[0] for i in user_graph_data]

    # get the system data and labels
    system_graph_data = Counter([x.get_classification_display() for x in system_reports]).most_common()
    system_graph_labels = [i[0] for i in system_graph_data]
    print(system_graph_labels)

    context = {
        'reports': user_reports,
        'system_reports': system_reports,
        'system_graph_data': system_graph_data,
        'system_graph_labels': system_graph_labels,

        'user_graph_data': user_graph_data,
        'user_graph_labels': user_graph_labels
    }
    return render(request, 'main/reports_page.html', context)


class TargetCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Target
    context_object_name = 'target'
    fields = ['asset', 'hostname', 'iprange', 'ports', 'owner']

    def form_valid(self, form):
        form.instance.author = self.request.user.profile

        messages.success(self.request, f'A target has been added successfully')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # used to return the context
        context = super(TargetCreateView, self).get_context_data()
        context['targets'] = Target.objects.all()
        return context

    def test_func(self):
        if self.request.user.legal.terms_accepted:
            return True
        return False


class ReportDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Report
    template_name = "main/report_detail.html"
    context_object_name = 'reports'

    def test_func(self):
        if self.request.user.legal.terms_accepted:
            return True
        return False


class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Report
    success_url = '/'

    def test_func(self):
        report = self.get_object()
        if self.request.user.is_superuser:
            return True
        if self.request.user.profile == report.author and self.request.user.legal.terms_accepted:
            return True
        return False


class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Report
    fields = ['title', 'details', 'asset', 'classification', 'severity', 'points', 'status']
    template_name = "main/report_update_form.html"

    def form_valid(self, form):

        """
            below we check to see if the user updating the form is admin.
            this is done as to let admins update and delete reports. if the user updating the form
            is admin we return the instance of the form as to not modify the author, the rest of the logic
            is handled in report_update_form.html
        """


        if self.request.user.is_superuser:
            return super().form_valid(form)
        else:
            form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def test_func(self):
        # gets the post we are currently trying to update
        post = self.get_object()
        # this will make it so users can't edit other users posts
        if self.request.user.is_superuser:
            return True
        if self.request.user.profile == post.author and self.request.user.legal.terms_accepted:
            return True
        return False


class ReportCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Report
    template_name = "main/report_create_form.html"
    fields = ['title', 'details', 'asset', 'classification', 'severity']

    def form_valid(self, form):
        # check if the author of the form is the same of the user.
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.legal.terms_accepted:
            return True
        return False
