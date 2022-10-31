from django.db import models


# Create your models here.
class Contacts(models.Model):
    first_name = models.CharField(max_length=32, null=False, blank=False)
    last_name = models.CharField(max_length=32, null=False, blank=False)
    email = models.EmailField()
    company = models.CharField(max_length=64, null=False, blank=False)
    birthday = models.DateField()
    instagram = models.CharField(max_length=32, null=False, blank=False)
    whatsapp = models.BooleanField(default=False)
    mobile = models.CharField(max_length=16, null=False, blank=False)
    house_office = models.CharField(max_length=16)
    image_contact = models.ImageField(upload_to='jewelry/images/%Y/%m/%d/')
    address = models.CharField(max_length=128, null=False, blank=False)
    notes = models.TextField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class CategoryJewelry(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return self.name


class ModelsJewelry(models.Model):
    category = models.ForeignKey(
        CategoryJewelry, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return self.model


class TypesMetals(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.name


class TypesStones(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.name


class TypesPearls(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.name


class Indicators(models.Model):
    fine_gold = models.FloatField(null=False, blank=False)
    parallel_dollar = models.FloatField(null=False, blank=False)


class Jewelry(models.Model):
    GENRE_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Unisex", "Unisex"),
    )
    product_name = models.CharField(max_length=128, null=False, blank=False)
    category = models.ForeignKey(
        CategoryJewelry, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(
        ModelsJewelry, on_delete=models.SET_NULL, null=True)
    genre = models.CharField(
        max_length=8, choices=GENRE_CHOICES, blank=False, null=False)
    weight = models.FloatField(null=False, blank=False)
    length = models.FloatField(null=False, blank=False)
    width = models.FloatField(null=False, blank=False)
    heigth = models.FloatField(null=False, blank=False)
    thickness = models.FloatField(null=False, blank=False)
    metal = models.ForeignKey(
        TypesMetals, on_delete=models.SET_NULL, null=True)
    image_jewel = models.ImageField(upload_to='jewelry/images/%Y/%m/%d/')
    note = models.TextField()

    def __str__(self):
        return self.product_name


class Services(models.Model):
    PIECE_CHOICES = (
        ("Metal", "Metal"),
        ("Stones", "Stones"),
        ("Pearls", "Pearls"),
    )
    piece = models.CharField(
        max_length=8, choices=PIECE_CHOICES, blank=False, null=False)
    provider = models.CharField(max_length=64, null=False, blank=False)
    service = models.CharField(max_length=64, null=False, blank=False)
    value = models.FloatField(null=False, blank=False)
    jewelry_id = models.ManyToManyField(Jewelry)

    def __str__(self):
        return self.service


class Pearls(models.Model):
    pearl = models.ForeignKey(
        TypesPearls, on_delete=models.SET_NULL, null=True)
    origin = models.CharField(max_length=32, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    size = models.FloatField(null=False, blank=False)
    color = models.CharField(max_length=16, null=False, blank=False)
    value = models.FloatField(null=False, blank=False)
    jewelry_id = models.ManyToManyField(Jewelry)


class Stones(models.Model):
    stone = models.ForeignKey(
        TypesStones, on_delete=models.SET_NULL, null=True)
    origin = models.CharField(max_length=32, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    size = models.FloatField(null=False, blank=False)
    carat = models.FloatField(null=False, blank=False)
    value = models.FloatField(null=False, blank=False)
    jewelry_id = models.ManyToManyField(Jewelry)
