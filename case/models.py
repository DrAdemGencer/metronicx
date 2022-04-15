from tabnanny import verbose
from django.db import models
from django.urls import reverse

# Create your models here.
class Case(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('InProgress', 'InProgress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    case_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    davaci = models.CharField(max_length=50)
    davaci_vekili = models.CharField(max_length=150)
    davali = models.CharField(max_length=100)
    davali_vekili = models.CharField(max_length=150)
    mahkeme = models.CharField(max_length=150)
    esas = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS, default='Pending')
    case_date = models.DateField()
    due_date = models.DateField()

    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'case'
        verbose_name_plural = 'cases'

    def get_url(self):
        return reverse('case_detail', args=[self.slug])

    def __str__(self):
        return self.case_name
    