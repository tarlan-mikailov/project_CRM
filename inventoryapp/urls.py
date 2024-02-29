from django.urls import path
from inventoryapp import views
from django.contrib.auth.decorators import login_required, permission_required 
from .views import CommodityCreate, CommodityDelete, CommodityDetail, CommodityList, CommodityUpdate, OrderCreate, OrderDelete, OrderDetail, OrderList, OrderUpdate

urlpatterns = [
    path('inventory/delete_order/', login_required(views.orderDelete), name='OrderDel'),
    path('inventory/delete_commodity/', login_required(views.commodityDelete), name='CommodityDel'),
    path('commodity/create/', login_required(CommodityCreate.as_view()), name = 'CommodityCreate'),
    path('commodity/list/', login_required(CommodityList.as_view()), name = 'CommodityList'),
    path('commodity/detail/<int:pk>', login_required(CommodityDetail.as_view()), name = 'CommodityDetail'),
    path('commodity/update/<int:pk>', login_required(CommodityUpdate.as_view()), name = 'CommodityUpdate'),
    path('commodity/delete/<int:pk>', login_required(CommodityDelete.as_view()), name = 'CommodityDelete'),
    path('order/create/', login_required(OrderCreate.as_view()), name = 'OrderCreate'),
    path('order/list/', login_required(OrderList.as_view()), name = 'OrderList'),
    path('order/detail/<int:pk>', login_required(OrderDetail.as_view()), name = 'OrderDetail'),
    path('order/update/<int:pk>', login_required(OrderUpdate.as_view()), name = 'OrderUpdate'),
    path('order/delete/<int:pk>', login_required(OrderDelete.as_view()), name = 'OrderDelete'),
]