from django.db import models
from django.urls import reverse

class Company(models.Model):
    # CHOICES
    PUBLIC_LIMITED_COMPANY = 'PLC'
    PRIVATE_COMPANY_LIMITED = 'LTD'
    LIMITED_LIABILITY_PARTNERSHIP = 'LLP'
    COMPANY_TYPE_CHOICES = (
        (PUBLIC_LIMITED_COMPANY, 'Public limited company'),
        (PRIVATE_COMPANY_LIMITED, 'Private company limited by shares'),
        (LIMITED_LIABILITY_PARTNERSHIP, 'Limited liability partnership'),
    )

    # DATABASE FIELDS
    name = models.CharField('name', max_length=30)
    vat_identification_number = models.CharField('VAT', max_length=20)
    company_type = models.CharField('type', max_length=3, choices=COMPANY_TYPE_CHOICES)

    # MANAGERS
    objects = models.Manager()
    limited_companies = LimitedCompanyManager()

    # META CLASS
    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # SAVE METHOD
    def save(self, *args, **kwargs):
        do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        do_something_else()

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('company_details', kwargs={'pk': self.id})

    # OTHER METHODS
    def process_invoices(self):
        do_something()
