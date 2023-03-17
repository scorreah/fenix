
# Django
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login
from django.views.decorators.cache import never_cache
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Forms
from user.forms import LoginForm

# Models
from user.models import User

# Create your views here.

class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    #dispatch verifica la peticion si es GET o POST
    def dispatch(self, request, *args, **kwargs):
        #Si el usuario esta autentificado se lleva al reverse_lazy
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        #si no me tiene que mandar al login y llamo a dispatch y pinto el metodo qeu corresponte
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)