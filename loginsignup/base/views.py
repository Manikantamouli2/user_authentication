
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'registration/home.html')

def authView(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # ✅ Use URL name, not a template path
    return render(request, 'registration/signup.html', {'form': form})
