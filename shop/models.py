from django.db import models

MAIN_CATEGORIES = (
    ('Mobiles', 'mobiles'),
    ('Laptops', 'laptops'),
    ('Tablets', 'tablets'),
    ('Tvs', 'tvs'),
    ('Accessories', 'accessories')
)


class Sub_Category(models.Model):
    category = models.CharField(choices=MAIN_CATEGORIES, max_length=100)
    sub_name = models.CharField(max_length=150)

    def __str__(self):
        return (("{} | {}").format(self.sub_name, self.category))


class Product(models.Model):
    name = models.CharField(max_length=155)
