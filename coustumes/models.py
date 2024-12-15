from django.db import models  # type: ignore
from users.models import CustomUser


# trending,casual,forms,dance coustumes
class RentedCostumes(models.Model):
    CATEGORY = (
        ("trending costumes", "Trending Costumes"),
        ("casual costumes", "Casual Costumes"),
        ("formal costumes", "Formals Costumes"),
        ("dance costumes", "Dance Costumes"),
        ("party wear", "Party wear"),
        ("sweater", "Sweater"),
    )
    item_name = models.CharField(max_length=200)
    material = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="coustume_images")
    small_size_stock = models.PositiveBigIntegerField(default=0)
    large_size_stock = models.PositiveBigIntegerField(default=0)
    medium_size_stock = models.PositiveBigIntegerField(default=0)
    XL_size_stock = models.PositiveBigIntegerField(default=0)
    XXL_size_stock = models.PositiveBigIntegerField(default=0)
    per_date_price = models.PositiveBigIntegerField()
    size = models.CharField(max_length=100)
    colour = models.CharField(max_length=200)
    costume_categories = models.CharField(max_length=200, choices=CATEGORY)

    def __str__(self):
        return self.item_name


class BookingRentedCostumes(models.Model):
    STATUS = (
        ("received", "Received"),
        ("undelivered.", "undelivered"),
        ("return", "Return"),
        ("completed.", "Completed"),
    )
    username = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True
    )
    booked_date = models.DateTimeField(auto_now=True, editable=False)
    item = models.ForeignKey(
        RentedCostumes, on_delete=models.CASCADE, null=True, blank=True
    )
    pairs = models.PositiveBigIntegerField(null=True, blank=True)
    price = models.PositiveBigIntegerField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=200, choices=STATUS, default="undelivered")
    address = models.CharField(max_length=200, null=True, blank=True)


class DressCode(models.Model):
    TYPE = (
        ("shirt", "Shirt"),
        ("t shirt", " T Shirt"),
        ("kurtha", "Kurtha"),
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    material = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="dress_image", null=True, blank=True)
    total_stock = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    outfit_type = models.CharField(max_length=200, choices=TYPE, null=True, blank=True)
    respond = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=1)
    #address
    #expected price
