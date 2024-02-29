from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('all_staff/', login_required(views.ListStaffView.as_view()), name='all_staff'),
    path('detail_staff/<int:pk>', login_required(views.DetailStaffView.as_view()), name='staff_detail'),
    path('create_staff/', login_required(views.create_staff_view), name='create_staff'),
    path('update_staff/<int:pk>', login_required(views.update_staff_view), name='update_staff'),
    path('delete_staff/<int:pk>', login_required(views.DeleteStaffUserView.as_view()), name='delete_staff'),
    path('schedule_staff/<id_staff>', login_required(views.detail_schedule_staff_view), name='schedule_staff'),
    path('all_schedule/', login_required(views.AllScheduleView.as_view()), name='all_schedule'),
    path('create_schedule/', login_required(views.CreateScheduleStaffView.as_view()), name='create_schedule'),
    path('detail_schedule/<int:pk>', login_required(views.DetailScheduleView.as_view()), name='schedule_detail'),
    path('delete_schedule/<int:pk>', login_required(views.DeleteScheduleView.as_view()), name='delete_schedule')
]
