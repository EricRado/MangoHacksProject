from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DeleteView, CreateView, RedirectView
from .forms import EditUserProfileForm, UserCreateForm, LoginForm
from .models import User
from django.contrib import messages


#########################################################################################################
##                                   USER FUNCTIONS                                                   ##
########################################################################################################

@csrf_protect
def login_view(request):
    next = request.POST.get('next', '/')
    form = LoginForm

    if request.method == 'POST':

        username = request.POST['nickname']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # if we have a user object, credentials correct
        if user:
            # check to see if account is active
            if user.is_active:
                # if account is active login the user and send the user back to homepage
                login(request, user)
                current_user = request.user
            # account is not active
            else:
                messages.error(request, 'Your account has been disabled.')

        # no user with matching credentials
        else:
            # bad login credentials were provided
            messages.error(request, 'Sorry the credentials you input, were incorrect.')

        return HttpResponseRedirect(next)

@csrf_protect
def manage_account(request):
    online_user = request.user
    user = User.objects.get(pk=online_user.user_id)
    form = EditUserProfileForm(request.POST or None, initial={'first_name': online_user.first_name,
                                                    'last_name': online_user.last_name, 'nickname': online_user.nickname,
                                                    'email_address': online_user.email_address}, instance=request.user)

    if request.method == 'POST':
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.nickname = form.cleaned_data['nickname']
            user.email_address = form.cleaned_data['email_address']

            user.save()

            messages.success(request, 'User information changes have been successfully saved.')

            return HttpResponseRedirect(reverse('index'))

    else:
        form = EditUserProfileForm(instance=online_user)

    return render(request, "accounts/manageAccount.html", {'form': form})


class SignUpView(CreateView):
    form_class = UserCreateForm
    model = User
    template_name = "accounts/signUp.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        new_user = form.save()
        messages.info(self.request, 'Thanks for registering. You may now login.')

        # after the new user is created, login the user
        new_user = authenticate(username=form.cleaned_data['nickname'], password=form.cleaned_data['password1'])
        login(self.request, new_user)

        return super(SignUpView, self).form_valid(form)

class LogoutView(RedirectView):
    url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Successfully logged out.')
        return super().get(request, *args, **kwargs)


# Create your views here.

