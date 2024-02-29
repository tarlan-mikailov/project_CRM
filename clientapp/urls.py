from django.urls import path, re_path
from clientapp import views
from django.contrib.auth.decorators import login_required, permission_required 
from .views import ClientCreate, ClientList, ClientDetail, ClientUpdate, ClientDelete


urlpatterns = [
    
    # path('client/delete_client/', login_required(views.clientDelete), name='ClientDel'),
    path('client/create/', login_required(ClientCreate.as_view()), name = 'ClientCreate'),
    path('client/list/', login_required(ClientList.as_view()), name = 'ClientList'),
    path('client/detail/<int:pk>', login_required(ClientDetail.as_view()), name = 'ClientDetail'),
    path('client/update/<int:pk>', login_required(ClientUpdate.as_view()), name = 'ClientUpdate'),
    path('client/delete/<int:pk>', login_required(ClientDelete.as_view()), name = 'ClientDelete'),
    # path('client/<subClient>/', login_required(views.client_form_view), name='client'),
]