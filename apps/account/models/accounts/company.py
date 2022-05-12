from django.db import models

from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=200)
    company_website = models.CharField(max_length=200)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='company_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='company_modified_by')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Company"


class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_id = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.emp_name


class Brand(models.Model):
    brand = models.CharField(max_length=200)
    country = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    url = models.URLField(max_length=300)

    def __str__(self):
        return self.brand
