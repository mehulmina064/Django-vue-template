from django.db import models

class TaskType(models.Model):
    weight = models.FloatField()
    description = models.TextField()
    class Meta:
        db_table = 'TaskType'
        verbose_name = 'Task Type'
        verbose_name_plural = 'Task Types'
        permissions = (
            ('create_TaskType', 'Can create Task Type'),
            ('read_TaskType', 'Can read Task Type'),
            ('write_TaskType', 'Can write Task Type'),
            ('delete_TaskType', 'Can delete Task Type'),
            ('email_TaskType', 'Can email Task Type'),
            ('share_TaskType', 'Can share Task Type'),
            ('print_TaskType', 'Can print Task Type'),
            ('report_TaskType', 'Can report Task Type'),
            ('export_TaskType', 'Can export Task Type'),
            ('import_TaskType', 'Can import Task Type'),
            ('amend_TaskType', 'Can amend Task Type'),
            ('cancel_TaskType', 'Can cancel Task Type'),
            ('set_user_permissions_TaskType', 'Can set user permissions Task Type'),
            ('submit_TaskType', 'Can submit Task Type'),
        )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __getitem__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other
