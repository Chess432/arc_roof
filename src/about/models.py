from django.db import models


class Testimonials(models.Model):
    image_testimonial     = models.ImageField(upload_to='image/', blank=True, null=True)
    name  = models.CharField(max_length=120)
    proffesion = models.CharField(max_length=120)
    testimony = models.TextField(null=True, blank=True)


