from django.db import models

from products.models import Product


class Order(models.Model):

    phone_number = models.CharField(
        max_length=13, verbose_name='Phone number'
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    add_to_work = models.DateTimeField(
        auto_now=False
    )
    completed = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.id} - {self.phone_number}'

    def get_sum(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Product, on_delete=models.CASCADE,
                             verbose_name='Product name'
                             )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.order}'

    def get_cost(self):
        return self.price * self.quantity
