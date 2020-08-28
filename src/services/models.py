from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

class Service(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image   = models.ImageField(upload_to='image/', blank=True, null=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    


    def get_absolute_url(self):
        return f"/services/{self.slug}"