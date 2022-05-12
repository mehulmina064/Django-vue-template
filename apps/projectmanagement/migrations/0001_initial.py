# Generated by Django 4.0.4 on 2022-05-12 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(max_length=255)),
                ('costing_rate', models.DecimalField(decimal_places=2, max_digits=19)),
                ('billing_rate', models.DecimalField(decimal_places=2, max_digits=19)),
                ('disabled', models.BooleanField(default=False)),
            ],
            options={
                'permissions': (('view_activity_type', 'Can view activity_type'), ('add_activity_type', 'Can add activity_type'), ('change_activity_type', 'Can change activity_type'), ('delete_activity_type', 'Can delete activity_type')),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('expected_start_date', models.DateField()),
                ('copied_from', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('actual_start_date', models.DateField()),
                ('actual_time', models.FloatField()),
                ('actual_end_date', models.DateField()),
                ('estimated_costing', models.FloatField()),
                ('total_costing_amount', models.FloatField()),
                ('total_expense_claim', models.FloatField()),
                ('total_purchase_cost', models.FloatField()),
                ('total_sales_amount', models.FloatField()),
                ('total_billable_amount', models.FloatField()),
                ('total_billed_amount', models.FloatField()),
                ('total_consumed_material_cost', models.FloatField()),
                ('gross_margin', models.FloatField()),
                ('per_gross_margin', models.FloatField()),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('first_email', models.TimeField()),
                ('second_email', models.TimeField()),
                ('daily_time_to_send', models.TimeField()),
                ('weekly_time_to_send', models.TimeField()),
                ('message', models.TextField()),
                ('priority', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('quick_entry', models.BooleanField(default=True)),
                ('search_fields', models.CharField(max_length=255)),
                ('show_name_in_global_search', models.BooleanField(default=True)),
                ('sort_field', models.CharField(max_length=255)),
                ('sort_order', models.CharField(max_length=255)),
                ('timeline_field', models.CharField(max_length=255)),
                ('title_field', models.CharField(max_length=255)),
                ('track_seen', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_type', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('creation', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('modified_by', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=255)),
                ('allow_copy', models.BooleanField()),
                ('allow_guest_to_view', models.BooleanField()),
                ('allow_import', models.BooleanField()),
                ('allow_rename', models.BooleanField()),
                ('autoname', models.CharField(max_length=255)),
                ('beta', models.BooleanField()),
                ('custom', models.BooleanField()),
                ('docstatus', models.IntegerField()),
                ('doctype', models.CharField(max_length=255)),
                ('document_type', models.CharField(max_length=255)),
                ('editable_grid', models.BooleanField()),
                ('engine', models.CharField(max_length=255)),
                ('has_web_view', models.BooleanField()),
                ('hide_heading', models.BooleanField()),
                ('hide_toolbar', models.BooleanField()),
                ('idx', models.IntegerField()),
                ('image_view', models.BooleanField()),
                ('in_create', models.BooleanField()),
                ('is_submittable', models.BooleanField()),
                ('issingle', models.BooleanField()),
                ('is_table', models.BooleanField()),
                ('max_attachments', models.IntegerField()),
                ('module', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('name_case', models.CharField(max_length=255)),
                ('quick_entry', models.BooleanField()),
                ('read_only', models.BooleanField()),
                ('read_only_onload', models.BooleanField()),
                ('show_name_in_global_search', models.BooleanField()),
                ('sort_field', models.CharField(max_length=255)),
                ('sort_order', models.CharField(max_length=255)),
                ('track_changes', models.BooleanField()),
                ('track_seen', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_copy', models.BooleanField(default=False)),
                ('allow_events_in_timeline', models.BooleanField(default=False)),
                ('allow_guest_to_view', models.BooleanField(default=False)),
                ('allow_import', models.BooleanField(default=False)),
                ('allow_rename', models.BooleanField(default=False)),
                ('autoname', models.CharField(blank=True, max_length=255, null=True)),
                ('beta', models.BooleanField(default=False)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('custom', models.BooleanField(default=False)),
                ('docstatus', models.IntegerField(default=0)),
                ('doctype', models.CharField(blank=True, max_length=255, null=True)),
                ('document_type', models.CharField(blank=True, max_length=255, null=True)),
                ('editable_grid', models.BooleanField(default=False)),
                ('engine', models.CharField(blank=True, max_length=255, null=True)),
                ('has_web_view', models.BooleanField(default=False)),
                ('hide_heading', models.BooleanField(default=False)),
                ('hide_toolbar', models.BooleanField(default=False)),
                ('idx', models.IntegerField(default=0)),
                ('image_view', models.BooleanField(default=False)),
                ('in_create', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_group', models.BooleanField(default=False)),
                ('exp_start_date', models.DateField(blank=True, null=True)),
                ('expected_time', models.FloatField(blank=True, null=True)),
                ('task_weight', models.FloatField(blank=True, null=True)),
                ('exp_end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('act_start_date', models.DateField(blank=True, null=True)),
                ('actual_time', models.FloatField(blank=True, null=True)),
                ('act_end_date', models.DateField(blank=True, null=True)),
                ('total_costing_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_expense_claim', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_billing_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('review_date', models.DateField()),
                ('closing_date', models.DateField()),
                ('lft', models.IntegerField()),
                ('rgt', models.IntegerField()),
                ('old_parent', models.CharField(max_length=140)),
                ('is_template', models.BooleanField()),
                ('start', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('completed_on', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
                ('completed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanagement.project')),
            ],
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Task Type',
                'verbose_name_plural': 'Task Types',
                'db_table': 'TaskType',
                'permissions': (('create_TaskType', 'Can create Task Type'), ('read_TaskType', 'Can read Task Type'), ('write_TaskType', 'Can write Task Type'), ('delete_TaskType', 'Can delete Task Type'), ('email_TaskType', 'Can email Task Type'), ('share_TaskType', 'Can share Task Type'), ('print_TaskType', 'Can print Task Type'), ('report_TaskType', 'Can report Task Type'), ('export_TaskType', 'Can export Task Type'), ('import_TaskType', 'Can import Task Type'), ('amend_TaskType', 'Can amend Task Type'), ('cancel_TaskType', 'Can cancel Task Type'), ('set_user_permissions_TaskType', 'Can set user permissions Task Type'), ('submit_TaskType', 'Can submit Task Type')),
            },
        ),
        migrations.CreateModel(
            name='TimesheetDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('expected_hours', models.FloatField()),
                ('to_time', models.DateTimeField()),
                ('hours', models.FloatField()),
                ('completed', models.BooleanField(default=False)),
                ('is_billable', models.BooleanField(default=False)),
                ('billing_hours', models.FloatField()),
                ('billing_rate', models.FloatField()),
                ('billing_amount', models.FloatField(default=0)),
                ('costing_rate', models.FloatField()),
                ('costing_amount', models.FloatField(default=0)),
                ('project_name', models.CharField(max_length=255)),
                ('base_billing_rate', models.FloatField()),
                ('base_billing_amount', models.FloatField()),
                ('base_costing_rate', models.FloatField()),
                ('base_costing_amount', models.FloatField()),
                ('activity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanagement.activitytype')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanagement.project')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanagement.task')),
            ],
            options={
                'db_table': 'timesheet_detail',
            },
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('employee_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_hours', models.FloatField()),
                ('total_billable_hours', models.FloatField()),
                ('total_billed_hours', models.FloatField()),
                ('total_costing_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_billable_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_billed_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('per_billed', models.FloatField()),
                ('note', models.TextField()),
                ('base_total_costing_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('base_total_billable_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('base_total_billed_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('exchange_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.currency')),
                ('parent_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanagement.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskDependsOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('project', models.TextField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanagement.task')),
            ],
            options={
                'verbose_name': 'Task Depends On',
                'verbose_name_plural': 'Task Depends On',
                'db_table': 'tabTask Depends On',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanagement.tasktype'),
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='images/')),
                ('full_name', models.CharField(max_length=254)),
                ('welcome_email_sent', models.BooleanField(default=False)),
                ('view_attachments', models.BooleanField(default=False)),
                ('project_status', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_user_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_user_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project User',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProjectTemplateTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('creation', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('sort_field', models.CharField(max_length=255)),
                ('sort_order', models.CharField(max_length=255)),
                ('track_changes', models.BooleanField()),
                ('is_table', models.BooleanField()),
                ('quick_entry', models.BooleanField()),
                ('editable_grid', models.BooleanField()),
                ('engine', models.CharField(max_length=255)),
                ('doctype', models.CharField(max_length=255)),
                ('module', models.CharField(max_length=255)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanagement.task')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('project_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanagement.projecttype')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='project_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanagement.projecttemplate'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanagement.projecttype'),
        ),
        migrations.CreateModel(
            name='DependentTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_copy', models.BooleanField(default=False)),
                ('allow_import', models.BooleanField(default=False)),
                ('allow_rename', models.BooleanField(default=False)),
                ('beta', models.BooleanField(default=False)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('custom', models.BooleanField(default=False)),
                ('docstatus', models.IntegerField(default=0)),
                ('doctype', models.CharField(default='DocType', max_length=255)),
                ('document_type', models.CharField(default='', max_length=255)),
                ('editable_grid', models.BooleanField(default=False)),
                ('hide_heading', models.BooleanField(default=False)),
                ('hide_toolbar', models.BooleanField(default=False)),
                ('idx', models.IntegerField(default=0)),
                ('image_view', models.BooleanField(default=False)),
                ('in_create', models.BooleanField(default=False)),
                ('is_submittable', models.BooleanField(default=False)),
                ('issingle', models.BooleanField(default=False)),
                ('is_table', models.BooleanField(default=False)),
                ('max_attachments', models.IntegerField(default=0)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('module', models.CharField(default='Projects', max_length=255)),
                ('name', models.CharField(default='Dependent Task', max_length=255)),
                ('name_case', models.CharField(default='', max_length=255)),
                ('quick_entry', models.BooleanField(default=False)),
                ('read_only', models.BooleanField(default=False)),
                ('read_only_onload', models.BooleanField(default=False)),
                ('sort_field', models.CharField(default='modified', max_length=255)),
                ('sort_order', models.CharField(default='DESC', max_length=255)),
                ('track_seen', models.BooleanField(default=False)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanagement.task')),
            ],
            options={
                'verbose_name': 'Dependent Task',
                'verbose_name_plural': 'Dependent Task',
                'db_table': 'Dependent Task',
            },
        ),
        migrations.CreateModel(
            name='ActivityCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('billing_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('costing_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('title', models.CharField(max_length=100)),
                ('activity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanagement.activitytype')),
            ],
        ),
    ]