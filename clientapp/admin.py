from django.contrib import admin
from .models import Client, ClientPhoto

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'birthday', 'comment')

@admin.register(ClientPhoto)
class ClientPhotoAdmin(admin.ModelAdmin):
    pass