from django.urls import path
from .views import ClientList, Client#, DeleteClientView clients#, client, ClientList, Client, ClientListView, SingleClientView

urlpatterns = [
    path('clients/', ClientList.as_view(), name='ClientListCreateAPI'),
    path('clients/<int:pk>', Client.as_view(), name='ClientUpdateAPI'),
    # path('clients/<int:pk>', DeleteClientView.as_view()),
    # path('clients', ClientListView.as_view()),
    # path('clients/<int:pk>', client),
]