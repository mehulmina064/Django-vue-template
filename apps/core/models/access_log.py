from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

Field_Types = (
    ('csv','CSV'),
    ('excel', 'EXCEL'),
)

class Access_Log(models.Model):
    export_form = models.CharField(max_length=150, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=CASCADE, blank=True, null=True)
    now = models.DateTimeField(auto_now=True)
    reference_document = models.CharField(max_length=150, blank=True, null=True)
    file_type = models.CharField(max_length=150, blank=True, null=True,choices=Field_Types,default='csv')
    report_name = models.CharField(max_length=150, blank=True, null=True)
    page = models.CharField(max_length=150, blank=True, null=True)
    log_data_section = models.CharField(max_length=150, blank=True, null=True)
    private_file_section = models.CharField(max_length=150, blank=True, null=True)
    report_information_section = models.CharField(max_length=150, blank=True, null=True)
    raw_information_log_section = models.CharField(max_length=150, blank=True, null=True)
    method = models.CharField(max_length=150, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='Access_Log_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='Access_Log_modified_by')
    def __str__(self):
        return self.export_form
    class Meta:
        verbose_name_plural = "Access_Log"
