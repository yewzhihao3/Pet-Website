from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.files.storage import default_storage
from django.templatetags.static import static

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pets')
    breed = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        upload_to='pet_images/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'webp'])],
        help_text="Upload a pet image (JPG, PNG, GIF, or WebP)",
        null=True,
        blank=True
    )
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.species}"

    @property
    def image_or_default_url(self) -> str:
        """Return image URL if file exists; otherwise return default static image URL."""
        if self.image and default_storage.exists(self.image.name):
            return self.image.url
        return static('images/default-pet.jpg')