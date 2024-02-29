from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import CreateRecordView, ListRecordView

urlpatterns = [
    path('record/list/', login_required(ListRecordView.as_view()), name='list_record'),
    path('record/create/', login_required(CreateRecordView.as_view()), name='create_record')
]
