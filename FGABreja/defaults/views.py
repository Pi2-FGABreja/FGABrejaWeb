from django.views.generic import View
from django.utils.translation import ugettext as _
from django.contrib import messages


class FGABrejaView(View):

    def add_message_errors(self, form, request):
        for error in form.errors:
            messages.error(request, _(error))
