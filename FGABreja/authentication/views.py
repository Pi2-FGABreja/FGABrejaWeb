from .forms import UserForm, UpdateUserForm, UpdatePasswordForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from defaults.views import FGABrejaView
from django.utils.translation import ugettext as _


class LoginView(FGABrejaView):
    http_method_names = [u'get', u'post']

    def get(self, request):
        if request.user.is_authenticated():
            response = redirect('/')
        else:
            response = render_to_response(
                'login.html', context_instance=RequestContext(request))
        return response

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, _("You are logged in"))
                return redirect('/')
            else:
                messages.error(request, _("Inactive user."))
        else:
            messages.error(request, _("Invalid username/password."))

        return render_to_response('login.html',
                                  context=RequestContext(request))


class LogoutView(FGABrejaView):
    http_method_names = [u'get']

    def get(self, request):
        logout(request)
        messages.info(request, _("See you later!"))
        return redirect("/")


class ForgotPasswordView(FGABrejaView):
    http_method_names = [u'get', u'post']

    def get(self, request):
        return render_to_response('login.html')

    def post(self, request):
        return render_to_response('login.html')


class UpdatePasswordView(FGABrejaView):
    http_method_names = [u'get', u'post']

    def post(self, request):
        form = UpdatePasswordForm(request)
        if form.is_valid():
            form.save()
            response = redirect(reverse('login'))
            messages.success(request,
                             _("Password successfully updated. Please login "
                               "again."))
        else:
            response = redirect(reverse('user_profile'))
            self.add_message_errors(form, request)

        return response


class UserProfileView(FGABrejaView):
    http_method_names = [u'get', u'post']

    def get(self, request):
        return render_to_response('profile.html',
                                  context=RequestContext(request))

    def post(self, request):
        form = UpdateUserForm(request)
        if form.is_valid():
            form.save()
            messages.success(request,
                             _("Profile information successfully updated."))
        else:
            self.add_message_errors(form, request)

        return redirect(reverse('user_profile'))

    def add_message_errors(self, form, request):
        for error in form.errors:
            messages.error(request, _(error))


class DeactivateUserView(FGABrejaView):
    http_method_names = [u'post']

    def post(self, request):
        request.user.deactivation_reason = request.POST.get('reason')
        request.user.is_active = False
        request.user.save()

        messages.success(request,
                         _("User successfully deactivated. See you later!"))
        logout(request)
        return redirect("/")


class RegisterUserView(FGABrejaView):
    http_method_names = [u'get', u'post']

    def get(self, request):
        return render_to_response('register.html',
                                  context=RequestContext(request))

    def post(self, request):
        form = UserForm(request)
        if form.is_valid():
            user = form.save()
            user.save()

            response = redirect(reverse('login'))
            messages.success(
                request,
                _("User {} successfully created!".format(user.username)))
        else:
            self.add_message_errors(form, request)
            response = redirect(reverse('register_user'))
        return response

    def add_message_errors(self, form, request):
        for error in form.errors:
            messages.error(request, _(error))
