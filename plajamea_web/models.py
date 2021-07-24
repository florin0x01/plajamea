from django.db import models

class Umbrella(models.Model):
    num_seats = models.IntegerField()
    umbrella_number = models.IntegerField()
    is_occupied = models.BooleanField()

class Table(models.Model):
    table_number = models.IntegerField()
    umbrella_number = models.ForeignKey(Umbrella, on_delete=models.DO_NOTHING)

class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=7, decimal_places=3)
    category = models.CharField(max_length=30)

    def __str__(self):
        return f'Product {self.name} with price {self.price} category {self.category}'

class Order(models.Model):
    date_started = models.DateField()
    date_ended = models.DateField()
    table_number = models.ForeignKey(Table, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=7, decimal_places=3)

class Waiter(models.Model):
    name = models.CharField(max_length=80)

class WaitedTables(models.Model):
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)
    table_number = models.ForeignKey(Table, on_delete=models.CASCADE)

class OrderProduct(models.Model):
    order_number = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
