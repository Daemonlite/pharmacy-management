from django.db import models
import uuid


class Drug(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    # total product in stock
    quantity = models.PositiveIntegerField(default=0)
    expiry_date = models.DateTimeField(blank=True, null=True)
    manufacturer = models.CharField(max_length=100)
    supplier_info = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    on_sale = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(quantity__gte=0), name="quantity_gte_0"
            ),
            models.CheckConstraint(check=models.Q(price__gte=0), name="price_gte_0"),
        ]


# to record purchases made
class Purchase(models.Model):
    purchase_uid = models.UUIDField(default=uuid.uuid4, editable=False)
    drug = models.ForeignKey(Drug, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=0)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.drug)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(purchase_price__gte=0), name="p_price_gte_0"
            )
        ]


class Dispenser(models.Model):
    full_name = models.CharField(max_length=100)


class History(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.purchase)
