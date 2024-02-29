from django.urls import path
from serviceapp import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('service/list_resource/', login_required(views.ListResourceView.as_view()), name='list_resource'),
    path('service/create_resource/', login_required(views.CreateResourceView.as_view()), name='create_resource'),
    path('service/detail_resource/<int:pk>', login_required(views.DetailResourceView.as_view()), name='detail_resource'),
    path('service/delete_resource/<int:pk>', login_required(views.DeleteResourceView.as_view()), name='delete_resource'),
    path('service/update_resource/<int:pk>', login_required(views.UpdateResourceView.as_view()), name='update_resource'),
    path('service/list_service/', login_required(views.ListServiceView.as_view()), name='list_service'),
    path('service/create_service/', login_required(views.create_service_view), name='create_service'),
    path('service/detail_service/<int:pk>', login_required(views.detail_service_list_resources_view), name='detail_service'),
    path('service/delete_service/<int:pk>', login_required(views.DeleteServiceView.as_view()), name='delete_service'),
    path('service/update_service/<int:pk>', login_required(views.UpdateServiceView.as_view()), name='update_service'),
    path('service/add_resource_for_service/<int:pk>', login_required(views.add_resource_for_service_view), name='add_resource_for_service'),
]
