from django.db import models

# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    description=models.TextField()
    pdf=models.FileField(upload_to="books/pdfs/")

    def funtion(self):
        return self.title

