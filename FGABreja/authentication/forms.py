from defaults.forms import FGABrejaForm
from django.contrib.auth.models import User
from django.core.validators import validate_email, ValidationError
from django.utils.translation import ugettext as _


class UserForm(FGABrejaForm):

    def is_valid(self):
        is_valid = False
        try:
            validate_email(self.data['email'])
            self.cleaned_data['email'] = self.data['email']
            self.cleaned_data['username'] = self.data['username']
            self.cleaned_data['first_name'] = self.data['first_name']
            self.cleaned_data['password'] = self.data['password']
            is_valid = True
        except ValidationError:
            self.errors.append(_("Enter a valid email address."))
        return is_valid

    def save(self):
        user = User()
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']
        user.ser_password(self.cleaned_data['password'])
        return user


class UpdateUserForm(FGABrejaForm):

    def is_valid(self):
        is_valid = False
        try:
            validate_email(self.data['email'])
            self.cleaned_data['email'] = self.data['email']
            is_valid = True
        except ValidationError:
            self.errors.append(_("Enter a valid email address."))

        self.cleaned_data['first_name'] = self.data['first_name']
        return is_valid

    def save(self):
        self.user.email = self.cleaned_data['email']
        self.user.first_name = self.cleaned_data['first_name']
        self.user.save()


class UpdatePasswordForm(FGABrejaForm):

    def is_valid(self):
        is_valid = False
        if self.data['password'] == self.data['confirm_password']:
            self.cleaned_data['password'] = self.data['password']
            is_valid = True
        else:
            self.errors.append(_('The fields "Password" and "Confirm password"'
                                 ' must be equals'))
        return is_valid

    def save(self):
        self.user.set_password(self.cleaned_data['password'])
        self.user.save()
