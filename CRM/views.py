from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect, render
from CRM.forms import UserRegistrationForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.POST['return_to'])
    context = {"return_to_value": request.GET.get('next', '/all_staff/')}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/login/')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            User = get_user_model()
            if len(User.objects.all()) == 0:
                new_user.is_superuser = True
                new_user.is_staff = True
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})