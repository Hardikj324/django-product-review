from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.utils import timezone
class UserRegister(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, max_length=70)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        Group,
        related_name='userregister_set',  # Custom related_name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='userregister_set_permissions',  # Custom related_name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    class Meta:
        verbose_name = "Custom User "
        verbose_name_plural = "Custom Users "

    def save(self, *args, **kwargs):
        if not self.pk:  # Ensures password is hashed when creating a new user
            self.password = make_password(self.password)
        super(UserRegister, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('smartphones', 'Smartphones'),
        ('laptops', 'Laptops'),
        ('audio', 'Audio Devices'),
        ('wearables', 'Wearables'),
        ('accessories', 'Accessories'),
    ]
    product_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, db_index=True)
    over_view = models.TextField(db_index=True)
    about = models.TextField()
    purchase_link = models.TextField(default='NA')
    image = models.ImageField(upload_to='product_photo/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name

class Review(models.Model):
    Review = models.TextField()
    user = models.ForeignKey(UserRegister, on_delete=models.CASCADE, related_name="review", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_review", null=True)
    created_at= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review by {self.user.username} on {self.product.product_name}'