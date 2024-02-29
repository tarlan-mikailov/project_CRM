from django.contrib.auth.models import User
from django.db import models, IntegrityError
from decimal import Decimal


class Commodity(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.IntegerField()

    class Meta:
        db_table = 'Commodity'
        constraints = [
            models.CheckConstraint(check=models.Q(amount__gte=0), name="amount_commodity_gte_0"),
            models.CheckConstraint(check=models.Q(price__gt=0), name="price_commodity_gte_0"),
        ]

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    id_commodity = models.ForeignKey(Commodity, on_delete=models.PROTECT, related_name='commodity')
    id_employee = models.ForeignKey(User, on_delete=models.PROTECT, related_name='staff')
    amount = models.IntegerField()
    discount = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 'Order'
        constraints = [
            models.CheckConstraint(check=models.Q(amount__gte=0), name="amount_order_gte_0"),
            models.CheckConstraint(check=models.Q(discount__range=[0, 99]), name="discount_order_range"),
        ]

    def __str__(self):
        return f'{self.date}, {self.id_commodity}, {self.id_employee}, {self.amount}, {self.discount}'

    @property
    def total_price(self):
        if self.discount == None:
            return self.id_commodity.price
        else:
            return f'{self.id_commodity.price * Decimal(1 - self.discount/100):.2f}'
    
    def save(self, *args, **kwargs):
        try:
            com = Commodity.objects.get(id=self.id_commodity.id)
            com.amount -= self.amount
            com.save()
        except IntegrityError as e:
            print(e)
        return super().save(*args, **kwargs)