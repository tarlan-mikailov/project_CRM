from typing import Any

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models
from django.shortcuts import render
from django.template.loader import render_to_string
from clientapp import forms
from clientapp.models import Client, ClientPhoto
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse


class ClientCreate(CreateView):
    model = Client
    form_class = forms.ClientForm
    template_name = 'client_create.html'
    success_url = '/client/create/'

    def post(self, request, *args, **kwargs):
        super().post(request=request, args=args, kwargs=kwargs)
        client = Client.objects.order_by("-id")[0]
        for i in request.FILES.getlist('image'):
            form = forms.ClientPhotoForm(files={"image": i}, data={'client_id': client})
            if form.is_valid():
                form.save()
        return JsonResponse({
            'message': 'success'
        })
    

class ClientList(ListView):
    model = Client
    template_name = 'client_list.html'
    success_url = '/client/create/'
    context_object_name = 'client_list'
    ordering = '-id'
    paginate_by = 10


class ClientDetail(DetailView):
    model = Client
    template_name = 'client_detail.html'

    def get_object(self, queryset=None):
        client = Client.objects.get(id=self.kwargs.get(self.pk_url_kwarg))
        photo_queryset = ClientPhoto.objects.filter(client_id=self.kwargs.get(self.pk_url_kwarg))
        if photo_queryset:
            new_photo = photo_queryset.all()
        else:
            new_photo = None
        if client:
            record = client.records.all()
        else:
            record = None
        return {"client": super().get_object(queryset), "photo": new_photo, 'records': record}


class ClientUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'clientapp.change_client'
    model = Client
    form_class = forms.ClientForm
    success_url = '/client/list/'
    template_name = 'client_update_form.html'


class ClientDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'clientapp.delete_client'
    model = Client
    success_url = '/client/list/'
    template_name = 'client_confirm_delete.html'