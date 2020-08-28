from django.db import models

class HomeModel(models.Model):
    main_text = models.TextField()
    secondary_text = models.TextField()
    button_link = models.CharField(max_length=120)
