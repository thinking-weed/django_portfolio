from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 必要に応じて追加フィールドを定義
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_user_set',  # 変更
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts_user_permissions_set',  # 変更
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    def __str__(self):
        return self.username
    
