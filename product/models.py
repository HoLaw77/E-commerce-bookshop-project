from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Product(models.Model):
    """model to store book products"""
    COVER_CHOICE = (
        (1, 'Hardback'),
        (2, 'Paperback'),
        (3, 'Softcover'),
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    year_of_publication = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1000), max_value_current_year])
    number_of_pages = models.IntegerField(MinValueValidator= 1, MaxValueValidator=1000)
    cover = models.CharField(choice='COVER_CHOICE', default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    price = models.DecimalField(max_digit=10, decimal_place=2, null=False, default=0)

    def __str__(self):
        return self.name    

class Language(models.Model):
    """model to store language option for books"""
    LANGUAGE_CHOICE = (
        (1, 'English'),
        (2, 'French'),
        (3, 'German'),
        (4, 'Japanese'),
        (5, 'Chinese'),
        (6, 'Russian'),
        (7, 'Greek')
    )    
    language = models.CharField(choice='LANGUAGE_CHOICE', default=1)
    note = models.CharField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Category(models.Model):
    """model to store cateogy of books"""
    GENRE_CHOICE = (
        (1, 'Romance fiction'),
        (2, 'Thriller fiction'),
        (3, 'Detective fiction'),
        (4, 'Classic'),
        (5, 'Nonfiction'),
        (6, 'Sci-fi/Fantasy'),
        (7, 'Poetry'),
        (8, 'Science'),
        (9, 'Social Science'),
        (10, 'Philosophy'),
    )

    REGION_CHOICE = (
        (1, 'United States'),
        (2, 'United Kingdom'),
        (3, 'Germany')
        (4, 'France'),
        (5, 'Japan'),
        (6, 'Russia'),
        (7, 'Greece'),
        (8, 'China'),
    ) 

    genre = models.CharField(choice='GENRE_CHOICE', default=1)
    region = models.CharField(choice='REGION_CHOICE', default=1)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    """model to store product image"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url =  models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField('product_image', folder='product_images', null=True, blank=True)
    alt_text = models.CharField(max_length=1000, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
