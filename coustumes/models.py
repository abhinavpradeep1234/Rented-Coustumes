from django.db import models  # type: ignore


# trending,casual,forms,dance coustumes
class RentedCostumes(models.Model):
    CATEGORY = (
        ("trending costumes", "Trending Costumes"),
        ("casual costumes", "Casual Costumes"),
        ("formals costumes", "formals Costumes"),
        ("dance costumes", "dance Costumes"),
        # ("formals costumes","formals Costumes")
    )
    item_name = models.CharField(max_length=200)
    material = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="coustume_images")
    total_stock = models.PositiveBigIntegerField(default=0)
    per_date_price = models.PositiveBigIntegerField()
    size = models.CharField(max_length=100)
    colour = models.CharField(max_length=200)
    costume_categories = models.CharField(max_length=200, choices=CATEGORY)
