from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from alumni.models import User
from django.core.urlresolvers import reverse_lazy


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class HomeView(TemplateView):
    template_name = 'home.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User

    fields = [
        'picture',
        'open_picture',
        'open_login_id',
        'email',
        'open_email',
        'work',
        'open_work',
        'work_position',
        'open_work_position',
        'work_phone',
        'open_work_phone',
    ]
    success_url = reverse_lazy('my_page')
    template_name = 'registration/user_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super(UserUpdateView, self).form_valid(form)
