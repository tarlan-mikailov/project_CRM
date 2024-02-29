# from django.template.loader import render_to_string
# from serviceapp import forms
# from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from serviceapp.forms import ServiceForm, ResourceForm, AddResourceForServiceForm, CreateServiceForm
from serviceapp.models import Resource, Service


class ListResourceView(ListView):
    model = Resource
    field = '__all__'
    context_object_name = 'list_resource'
    ordering = '-id'
    paginate_by = 10
    template_name = 'serviceapp/resource_list.html'


class DetailResourceView(DetailView):
    model = Resource
    template_name = 'serviceapp/resource_detail.html'
    context_object_name = 'detail_resource'


class DeleteResourceView(PermissionRequiredMixin, DeleteView):
    permission_required = 'serviceapp.delete_resource'
    model = Resource
    template_name = 'serviceapp/delete_confirm.html'
    success_url = '/service/list_resource/'
    context_object_name = 'delete_obj'


class UpdateResourceView(PermissionRequiredMixin, UpdateView):
    permission_required = 'serviceapp.update_resource'
    model = Resource
    form_class = ResourceForm
    template_name = 'serviceapp/resource_update.html'

    def get_success_url(self):
        resource_id = self.kwargs['pk']
        return reverse('detail_resource', kwargs={'pk': resource_id})


class CreateResourceView(CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'serviceapp/resource_create.html'
    success_url = '/service/create_resource/'


class ListServiceView(ListView):
    model = Service
    paginate_by = 10
    context_object_name = 'list_service'
    template_name = 'serviceapp/service_list.html'
    ordering = '-id'


class DeleteServiceView(PermissionRequiredMixin, DeleteView):
    permission_required = 'serviceapp.delete_service'
    model = Service
    template_name = 'serviceapp/delete_confirm.html'
    success_url = '/service/list_service/'
    context_object_name = 'delete_obj'


class UpdateServiceView(PermissionRequiredMixin, UpdateView):
    permission_required = 'serviceapp.update_service'
    model = Service
    form_class = ServiceForm
    template_name = 'serviceapp/service_update.html'

    def get_success_url(self):
        service_id = self.kwargs['pk']
        return reverse('detail_service', kwargs={'pk': service_id})


def create_service_view(request):
    form = CreateServiceForm
    if request.method == 'POST':
        new_service = Service.objects.create(name=request.POST['name'])
        if request.POST.get('resource'):
            new_service.resources.add(*request.POST.getlist('resource'))
    return render(request, 'serviceapp/service_create.html', {'form': form})


def detail_service_list_resources_view(request, pk):
    current_serv = Service.objects.get(id=pk)
    resources_list = current_serv.resources.all()
    return render(request, 'serviceapp/service_detail.html',
                  {'data_resource': resources_list, 'data_service': current_serv})


def add_resource_for_service_view(request, pk):
    form = AddResourceForServiceForm
    current_serv = Service.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST.get('resource'):
            current_serv.resources.add(*request.POST.getlist('resource'))
        else:
            current_serv.resources.remove(*Resource.objects.all())
        return detail_service_list_resources_view(request, pk)
    return render(request, 'serviceapp/add_resource_for_service.html', {'form': form})
