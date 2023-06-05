from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import User
from .forms import UserForm
from .mixins import UserHasPermissionMixin


# Create your views here.
class IndexView(ListView):
    template_name = "users/index.html"
    model = User


class UserFormCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    succes_url = reverse_lazy("login")
    success_message = _("User successfully registred")
    


class UserUpdateView(UserHasPermissionMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "users/update.html"
    success_url = reverse_lazy("users_index")
    success_message = _("User successfully updated")


class UserDeleteView(UserHasPermissionMixin, DeleteView):
    model = User
    success_url = reverse_lazy("users_index")
    template_name = "users/delete.html"

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(
                self.request,
                _("Cannot delete a user because he is being used"),
            )
        else:
            messages.success(
                self.request,
                _("User successfully deleted"),
            )
        return HttpResponseRedirect(success_url)
