from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Client:
    id: int
    name: str
    img: str

class Service(models.Model):
    name = models.CharField(max_length=30)
    details = models.TextField(max_length=400)
    img = models.FileField(upload_to='static/images/icons/services/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'svg'])])