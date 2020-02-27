from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth.models import User
from django.contrib.auth import login

from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


from .tokens import account_activation_token
from .forms import UserRegistrationForm
# Create your views here.

def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Activate your Minimalist blog account."
            message = render_to_string(
                'registration/account_activation_mail.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                })
            to_email = user.email 
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return redirect(reverse('homepage'))
    context = {'form': form}
    return render(request, 'registration/register.html', context=context)



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('homepage')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')