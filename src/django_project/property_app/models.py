import uuid

from django.db import models

from src.django_project.useraccount_app.models import User


class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=100, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    guests = models.PositiveIntegerField()
    country = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)
    category = models.CharField(max_length=255)
    favorited = models.ManyToManyField(User, related_name="favorites", blank=True)
    image = models.ImageField(upload_to="uploads/properties")
    landlord = models.ForeignKey(
        User,
        related_name="properties",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def image_url(self):
        return f"{self.image.url}".replace(
            "https://clone-airbnb.https://s3.tebi.io",
            "https://s3.tebi.io/clone-airbnb",
        )

    def __str__(self):
        return self.title


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(
        Property,
        related_name="reservations",
        on_delete=models.CASCADE,
    )
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_nights = models.PositiveIntegerField()
    guests = models.PositiveIntegerField()
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name="reservations",
        on_delete=models.CASCADE,
    )
