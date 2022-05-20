# Generated by Django 4.0.4 on 2022-05-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_data_import_pending_alter_docfield_fieldtype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_import',
            name='Pending',
            field=models.CharField(blank=True, choices=[('Error', 'Error'), ('Success', 'Success'), ('Partial Success', 'Partial Success')], default='Success', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='data_import',
            name='import_type',
            field=models.CharField(blank=True, choices=[('Update Existing Records', 'Update Existing Records'), ('Insert New Records', 'Insert New Records')], default='Insert New Records', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='docfield',
            name='fieldtype',
            field=models.CharField(blank=True, choices=[('Dynamic Link', ''), ('Data', ''), ('Int', ''), ('Rating', ''), ('Currency', ''), ('HTML', ''), ('Percent', ''), ('JSON', ''), ('Read Only', ''), ('Heading', ''), ('Section Break', ''), ('Autocomplete', ''), ('Icon', ''), ('Check', ''), ('Float', ''), ('Markdown Editor', ''), ('Barcode', ''), ('Date', ''), ('Password', ''), ('Column Break', ''), ('Datetime', ''), ('HTML Editor', ''), ('Attach Image', ''), ('Text', ''), ('Table MultiSelect', ''), ('Text Editor', ''), ('Code', ''), ('Image', ''), ('Phone', ''), ('Time', ''), ('Duration', ''), ('Attach', ''), ('Table', ''), ('Link', ''), ('Select', ''), ('Color', ''), ('Fold', ''), ('Button', ''), ('Signature', ''), ('Geolocation', ''), ('Tab Break', ''), ('Small Text', ''), ('Long Text', '')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='docfield',
            name='precision',
            field=models.CharField(blank=True, choices=[('9', ''), ('6', ''), ('2', ''), ('5', ''), ('7', ''), ('4', ''), ('1', ''), ('3', ''), ('8', '')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='doctype',
            name='document_type',
            field=models.CharField(blank=True, choices=[('Setup', 'Setup'), ('Document', 'Document'), ('System', 'System'), ('Other', 'Other')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctype',
            name='engine',
            field=models.CharField(blank=True, choices=[('MyISAM', 'MyISAM'), ('InnoDB', 'InnoDB')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctype_state',
            name='color',
            field=models.CharField(choices=[('2', 'Cyan'), ('3', 'Gray'), ('9', 'Red'), ('4', 'Green'), ('8', 'Purple'), ('10', 'Yellow'), ('7', 'Pink'), ('1', 'Blue'), ('6', 'Orange'), ('5', 'Light Blue')], max_length=100),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='reference_doctype',
            field=models.CharField(choices=[('Setup', 'Setup'), ('Document', 'Document'), ('System', 'System'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='navbar_item',
            name='item_type',
            field=models.CharField(choices=[('Route', 'Route'), ('Separator', 'Separator'), ('Action', 'Action')], max_length=100),
        ),
        migrations.AlterField(
            model_name='package',
            name='license_type',
            field=models.CharField(choices=[('Public License', 'Public License'), ('GNU Affero General', 'GNU Affero General'), ('MIT License', 'MIT License'), ('GNU General Public License', 'GNU General Public License')], max_length=255),
        ),
        migrations.AlterField(
            model_name='prepared_report',
            name='status',
            field=models.CharField(choices=[('Error', 'Error'), ('Completed', 'Completed'), ('Queued', 'Queued')], max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.CharField(choices=[('Script Report', 'Script Report'), ('Query Report', 'Query Report'), ('Custom Report', 'Custom Report'), ('Report Builder', 'Report Builder')], max_length=100),
        ),
        migrations.AlterField(
            model_name='report_column',
            name='fieldtype',
            field=models.CharField(choices=[('IntigerField', 'IntigerField'), ('OneToOneRelation', 'OneToOneRelation'), ('boolean', 'boolean'), ('Float', 'Float'), ('ForeignKey', 'ForeignKey'), ('charfield', 'charfield'), ('Date', 'Date'), ('DateField', 'DateField'), ('ManyToOneRelation', 'ManyToOneRelation'), ('OneToManyRelation', 'OneToManyRelation'), ('ManyToManyField', 'ManyToManyField'), ('Currency', 'Currency')], max_length=255),
        ),
        migrations.AlterField(
            model_name='scheduled_job_log',
            name='status',
            field=models.CharField(choices=[('Failed', 'Failed'), ('Scheduled', 'Scheduled'), ('Complete', 'Complete')], max_length=20),
        ),
        migrations.AlterField(
            model_name='scheduled_job_type',
            name='frequency',
            field=models.CharField(choices=[('Yearly', 'Yearly'), ('Annual', 'Annual'), ('Hourly Long', 'Hourly Long'), ('Cron', 'Cron'), ('Weekly Long', 'Weekly Long'), ('Hourly', 'Hourly'), ('Weekly', 'Weekly'), ('Daily', 'Daily'), ('Daily Long', 'Daily Long'), ('All', 'All'), ('Monthly Long', 'Monthly Long'), ('Monthly', 'Monthly')], max_length=100),
        ),
        migrations.AlterField(
            model_name='server_script',
            name='doctype_event',
            field=models.CharField(choices=[('After Insert', 'After Insert'), ('Before Delete', 'Before Delete'), ('After Delete', 'After Delete'), ('Before Save', 'Before Save'), ('Before Submit', 'Before Submit'), ('After Save', 'After Save'), ('Before Save', 'After Save'), ('After Submit', 'After Submit'), ('After Cancel', 'After Cancel'), ('Before Cancel', 'Before Cancel'), ('Before Insert', 'Before Insert'), ('On Payment Authorization', 'On Payment Authorization'), ('Before Validate', 'Before Validate')], max_length=100),
        ),
        migrations.AlterField(
            model_name='server_script',
            name='event_frequency',
            field=models.CharField(choices=[('Yearly', 'Yearly'), ('Annual', 'Annual'), ('Hourly Long', 'Hourly Long'), ('Cron', 'Cron'), ('Weekly Long', 'Weekly Long'), ('Hourly', 'Hourly'), ('Weekly', 'Weekly'), ('Daily', 'Daily'), ('Daily Long', 'Daily Long'), ('All', 'All'), ('Monthly Long', 'Monthly Long'), ('Monthly', 'Monthly')], max_length=100),
        ),
        migrations.AlterField(
            model_name='server_script',
            name='script_type',
            field=models.CharField(choices=[('Permission Query', 'Permission Query'), ('Scheduler Event', 'Scheduler Event'), ('DocType Event', 'DocType Event'), ('API', 'API')], max_length=100),
        ),
        migrations.AlterField(
            model_name='system_settings',
            name='currency_precision',
            field=models.CharField(choices=[('5', ''), ('9', ''), ('2', ''), ('6', ''), ('7', ''), ('4', ''), ('1', ''), ('0', ''), ('3', ''), ('8', '')], max_length=100),
        ),
        migrations.AlterField(
            model_name='system_settings',
            name='date_format',
            field=models.CharField(choices=[('ymd', 'yyyy-mm-dd'), ('dmy', 'dd.mm.yyyy'), ('dmy', 'dd-mm-yyyy'), ('mdy', 'mm-dd-yyyy'), ('mdy', 'mm/dd/yyyy'), ('dmy', 'dd/mm/yyyy')], max_length=100),
        ),
        migrations.AlterField(
            model_name='system_settings',
            name='first_day_of_the_week',
            field=models.CharField(choices=[('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Monday', 'Monday'), ('Saturday', 'Saturday'), ('Tuesday', 'Tuesday'), ('Sunday', 'Sunday')], default='Sunday', max_length=100),
        ),
        migrations.AlterField(
            model_name='system_settings',
            name='float_precision',
            field=models.CharField(choices=[('5', ''), ('9', ''), ('2', ''), ('6', ''), ('7', ''), ('4', ''), ('3', ''), ('8', '')], max_length=100),
        ),
        migrations.AlterField(
            model_name='translation',
            name='contribution_status',
            field=models.CharField(choices=[('rejected', 'rejected'), ('verified', 'verified'), ('pending', 'pending')], max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='desk_theme',
            field=models.CharField(blank=True, choices=[('Automatic', 'Automatic'), ('Dark', 'Dark'), ('Light', 'Light')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='document_follow_frequency',
            field=models.CharField(blank=True, choices=[('Weekly', 'Weekly'), ('Hourly', 'Hourly'), ('All', 'All'), ('Daily', 'Daily')], max_length=100, null=True),
        ),
    ]