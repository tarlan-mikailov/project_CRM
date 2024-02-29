from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.template.loader import render_to_string
from django.http import HttpResponse
from inventoryapp.models import Commodity, Order
from inventoryapp import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class CommodityCreate(CreateView):
    model = Commodity
    form_class = forms.ComodityForm
    template_name = 'commodity_create.html'
    success_url = '/commodity/create/'


class CommodityList(ListView):
    model = Commodity
    template_name = 'commodity_list.html'
    success_url = '/commodity/create/'
    ordering = '-id'
    paginate_by = 10


class CommodityDetail(DetailView):
    model = Commodity
    template_name = 'commodity_detail.html'


class CommodityUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'inventoryapp.change_commodity'
    model = Commodity
    form_class = forms.ComodityForm
    success_url = '/commodity/list/'
    template_name = 'commodity_update_form.html'


class CommodityDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'inventoryapp.delete_commodity'
    model = Commodity
    success_url = '/commodity/list/'
    template_name = 'commodity_confirm_delete.html'




class OrderCreate(CreateView):
    model = Order
    template_name = 'order_create.html'
    success_url = '/order/create/'

    def get(self, *args, **kwargs):
        formset = forms.orderFormSet(queryset=Order.objects.none())
        return self.render_to_response({"order_formset": formset})
    
    def post(self, *args, **kwargs):
        formset = forms.orderFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect('/order/list/')
        
        return self.render_to_response({"order_formset": formset})


class OrderList(ListView):
    model = Order
    template_name = 'order_list.html'
    success_url = '/order/create/'
    ordering = '-id'
    paginate_by = 10


class OrderDetail(DetailView):
    model = Order
    template_name = 'order_detail.html'


class OrderUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'inventoryapp.change_order'
    model = Order
    form_class = forms.OrderForm
    success_url = '/order/list/'
    template_name = 'order_update_form.html'


class OrderDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'inventoryapp.delete_order'
    model = Order
    success_url = '/order/list/'
    template_name = 'order_confirm_delete.html'


@permission_required('inventoryapp.delete_commodity')
def commodityDelete(request):
    try:
        for i in request.POST.copy().pop('id'):
            Commodity.objects.get(id=int(i)).delete()
        rendered = render_to_string('commodity_deleted.html')
        return HttpResponse(rendered)
    except KeyError:
        data = Commodity.objects.all()
        context = {'form': data}
        return render(request, 'commodity_db.html', context)
    

@permission_required('inventoryapp.delete_order')
def orderDelete(request):
    try:
        for i in request.POST.copy().pop('id'):
            Order.objects.get(id=int(i)).delete()
        rendered = render_to_string('order_deleted.html')
        return HttpResponse(rendered)
    except KeyError:
        data = Order.objects.all()
        context = {'form': data}
        return render(request, 'order_db.html', context)