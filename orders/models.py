from django.db import models
from users.models import User

# Create your models here.
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order ID: {self.order_id}, User: {self.user.username}, Total Amount: {self.total_amount}"