from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from CRM.forms import UserRegistrationForm
from .models import Schedule
from .forms import CreateScheduleStaffForm, FilterScheduleForm, UpdateStaffUserForm


class ListStaffView(ListView):
    model = User
    template_name = 'staffapp/staff_list.html'
    ordering = '-id'
    paginate_by = 10


class DetailStaffView(DetailView):
    model = User
    template_name = 'staffapp/staff_detail.html'


def create_staff_view(request):
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
            staff_list = User.objects.all()
            return render(request, 'staffapp/staff_list.html', {'object_list': staff_list})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'staffapp/staff_create.html', {'user_form': user_form})


class DeleteStaffUserView(PermissionRequiredMixin, DeleteView):
    permission_required = 'auth.delete_user'
    model = User
    template_name = 'staffapp/delete_confirm.html'
    success_url = '/all_staff'


@permission_required('auth.change_user')
def update_staff_view(request, pk):
    current_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateStaffUserForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            if current_user.groups.all():
                current_user.groups.get().user_set.remove(current_user)
            Group.objects.get(id=(request.POST['group'])).user_set.add(pk)
            return redirect(to='all_staff')
    else:
        form = UpdateStaffUserForm(instance=current_user)
    return render(request, 'staffapp/staff_update_form.html', {'form': form})


class AllScheduleView(ListView):
    model = Schedule
    template_name = 'staffapp/schedule_list.html'
    ordering = '-id'
    paginate_by = 10


class CreateScheduleStaffView(CreateView):
    model = Schedule
    form_class = CreateScheduleStaffForm
    success_url = '/create_schedule/'
    template_name = 'staffapp/schedule_staff_create.html'


def detail_schedule_staff_view(request, id_staff):
    filter_schedule_form = FilterScheduleForm
    staff = User.objects.get(id=id_staff)
    if request.GET.getlist('date'):
        schedule = Schedule.objects.filter(date__range=request.GET.getlist('date'), id_staff=id_staff).order_by('date')
    else:
        schedule = Schedule.objects.filter(id_staff=id_staff).order_by('date')
    return render(request, 'staffapp/list_schedule_staff.html',
                  {'data_schedule': schedule, 'data_staff': staff, 'form_filter': filter_schedule_form})


class DetailScheduleView(DetailView):
    model = Schedule
    template_name = 'staffapp/schedule_detail.html'


class DeleteScheduleView(PermissionRequiredMixin, DeleteView):
    permission_required = 'staffapp.delete_schedule'
    model = Schedule
    template_name = 'staffapp/delete_confirm.html'
    success_url = '/all_schedule/'
