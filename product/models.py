from django.db import models

# Create your models here.

COVER_CHOICE = (
    (1, 'Hardback'),
    (2, 'Paperback'),
    (3, 'Softcover'),
)
class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    author_first_name = models.CharField(max_length=100, null=True, blank=True)
    author_last_name = models.CharField(max_length=100, null=True, blank=True)
    year_of_publication = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1000), max_value_current_year])
    number_of_pages = models.IntegerField(MinValueValidator= 1, MaxValueValidator=1000)
    cover = models.CharField(choice='COVER_CHOICE', default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    price = models.IntegerField(max_digit=4)

class Language
    
