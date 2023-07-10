from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe

class User(AbstractUser):
    img = models.ImageField(
        upload_to='users/profile_picture',
        default='users/default_profile_picture.svg',
        blank=True,
        null=True
    )
    bio = models.CharField(max_length=200, blank=True)

    @mark_safe
    def icon(self, text: str = None) -> str:
        children = [f'<img src="{self.img.url}" style="width: 30px; border-radius: 50%; margin-right: 10px;">']
        if text is not None:
            children.append(f'<div>{text}</div>')
        
        parent = (
            '<div style="display: flex; align-items: center;">',
            '\n'.join(f'    {child}' for child in children),
            '</div>'
        )
        return '\n'.join(parent)

    def __str__(self) -> str:
        if self.img:
            return self.icon(text=self.username)
        return self.username

