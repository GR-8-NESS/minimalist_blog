from django.shortcuts import render

from .forms import UserRegistrationForm
# Create your views here.

def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'registration/register.html', context=context)