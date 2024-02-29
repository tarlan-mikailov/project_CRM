from django.db import models


def user_directory_path(instance, filename):
    return 'client_{0}_{1}/{2}'.format(instance.client_id.first_name, instance.client_id.last_name, filename)


class Client(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=30, blank=True, default='')
    birthday = models.DateField(null=True, blank=True, default=None)
    comment = models.CharField(max_length=150, blank=True, default='')

    class Meta:
        db_table = 'Client'

    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name}, {self.phone}, {self.email}, {self.birthday}, {self.comment}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    

class ClientPhoto(models.Model):
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    client_id = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='photo', null=True, default=None)

    class Meta:
        db_table = 'ClientImage'
    
    def __str__(self) -> str:
        return f'{self.image}'