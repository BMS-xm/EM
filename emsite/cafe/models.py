from django.db import models

class Order(models.Model):
    table_number = models.IntegerField()
    total_price = models.FloatField()
    status = models.CharField(max_length=10)

class Item(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    price = models.FloatField()
