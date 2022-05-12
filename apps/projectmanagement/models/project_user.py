from django.db import models
from django.contrib.auth.models import User


class ProjectUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    image = models.ImageField(upload_to='images/')
    full_name = models.CharField(max_length=254)
    welcome_email_sent = models.BooleanField(default=False)
    view_attachments = models.BooleanField(default=False)
    project_status = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_user_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_user_updated_by')
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Project User'
