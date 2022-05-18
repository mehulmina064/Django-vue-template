# Generated by Django 3.2.6 on 2022-05-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220516_1120'),
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
            field=models.CharField(blank=True, choices=[('Insert New Records', 'Insert New Records'), ('Update Existing Records', 'Update Existing Records')], default='Insert New Records', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='docfield',
            name='fieldtype',
            field=models.CharField(blank=True, choices=[('HTML Editor', ''), ('Phone', ''), ('Date', ''), ('Dynamic Link', ''), ('Signature', ''), ('Time', ''), ('Select', ''), ('Tab Break', ''), ('Geolocation', ''), ('Duration', ''), ('Section Break', ''), ('Button', ''), ('Rating', ''), ('Read Only', ''), ('Float', ''), ('Column Break', ''), ('Autocomplete', ''), ('Datetime', ''), ('Barcode', ''), ('JSON', ''), ('Markdown Editor', ''), ('Fold', ''), ('Table', ''), ('Table MultiSelect', ''), ('Image', ''), ('Text Editor', ''), ('Text', ''), ('Password', ''), ('Percent', ''), ('Long Text', ''), ('Small Text', ''), ('Attach Image', ''), ('Int', ''), ('Link', ''), ('Heading', ''), ('Check', ''), ('Color', ''), ('Code', ''), ('Icon', ''), ('Data', ''), ('Currency', ''), ('Attach', ''), ('HTML', '')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='docfield',
            name='precision',
            field=models.CharField(blank=True, choices=[('3', ''), ('7', ''), ('5', ''), ('8', ''), ('1', ''), ('4', ''), ('9', ''), ('6', ''), ('2', '')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='doctype',
            name='document_type',
            field=models.CharField(blank=True, choices=[('Setup', 'Setup'), ('Document', 'Document'), ('Other', 'Other'), ('System', 'System')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctype_state',
            name='color',
            field=models.CharField(choices=[('1', 'Blue'), ('4', 'Green'), ('3', 'Gray'), ('6', 'Orange'), ('10', 'Yellow'), ('9', 'Red'), ('8', 'Purple'), ('7', 'Pink'), ('5', 'Light Blue'), ('2', 'Cyan')], max_length=100),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='reference_doctype',
            field=models.CharField(choices=[('Setup', 'Setup'), ('Document', 'Document'), ('Other', 'Other'), ('System', 'System')], max_length=100),
        ),
        migrations.AlterField(
            model_name='package',
            name='license_type',
            field=models.CharField(choices=[('GNU General Public License', 'GNU General Public License'), ('Public License', 'Public License'), ('MIT License', 'MIT License'), ('GNU Affero General', 'GNU Affero General')], max_length=255),
        ),
        migrations.AlterField(
            model_name='page',
            name='standard',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='prepared_report',
            name='status',
            field=models.CharField(choices=[('Error', 'Error'), ('Completed', 'Completed'), ('Queued', 'Queued')], max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='is_standard',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.CharField(choices=[('Report Builder', 'Report Builder'), ('Script Report', 'Script Report'), ('Query Report', 'Query Report'), ('Custom Report', 'Custom Report')], max_length=100),
        ),
        migrations.AlterField(
            model_name='report_column',
            name='fieldtype',
            field=models.CharField(choices=[('Currency', 'Currency'), ('ForeignKey', 'ForeignKey'), ('Date', 'Date'), ('Float', 'Float'), ('DateField', 'DateField'), ('charfield', 'charfield'), ('IntigerField', 'IntigerField'), ('ManyToOneRelation', 'ManyToOneRelation'), ('boolean', 'boolean'), ('OneToManyRelation', 'OneToManyRelation'), ('OneToOneRelation', 'OneToOneRelation'), ('ManyToManyField', 'ManyToManyField')], max_length=255),
        ),
        migrations.AlterField(
            model_name='scheduled_job_log',
            name='status',
            field=models.CharField(choices=[('Complete', 'Complete'), ('Scheduled', 'Scheduled'), ('Failed', 'Failed')], max_length=20),
        ),
        migrations.AlterField(
            model_name='scheduled_job_type',
            name='frequency',
            field=models.CharField(choices=[('Hourly', 'Hourly'), ('All', 'All'), ('Hourly Long', 'Hourly Long'), ('Daily', 'Daily'), ('Yearly', 'Yearly'), ('Daily Long', 'Daily Long'), ('Weekly', 'Weekly'), ('Cron', 'Cron'), ('Weekly Long', 'Weekly Long'), ('Monthly', 'Monthly'), ('Annual', 'Annual'), ('Monthly Long', 'Monthly Long')], max_length=100),
        ),
        migrations.AlterField(
            model_name='server_script',
            name='doctype_event',
            field=models.CharField(choices=[('After Delete', 'After Delete'), ('On Payment Authorization', 'On Payment Authorization'), ('Before Delete', 'Before Delete'), ('Before Save', 'Before Save'), ('After Insert', 'After Insert'), ('After Save', 'After Save'), ('Before Validate', 'Before Validate'), ('Before Insert', 'Before Insert'), ('Before Save', 'After Save'), ('Before Submit', 'Before Submit'), ('After Submit', 'After Submit'), ('After Cancel', 'After Cancel'), ('Before Cancel', 'Before Cancel')], max_length=100),
        ),
        migrations.AlterField(
            model_name='server_script',
            name='event_frequency',
            field=models.CharField(choices=[('Hourly', 'Hourly'), ('All', 'All'), ('Hourly Long', 'Hourly Long'), ('Daily', 'Daily'), ('Yearly', 'Yearly'), ('Daily Long', 'Daily Long'), ('Weekly', 'Weekly'), ('Cron', 'Cron'), ('Weekly Long', 'Weekly Long'), ('Monthly', 'Monthly'), ('Annual', 'Annual'), ('Monthly Long', 'Monthly Long')], max_length=100),
        ),
        migrations.AlterField(
            model_name='server_script',
            name='script_type',
            field=models.CharField(choices=[('API', 'API'), ('Permission Query', 'Permission Query'), ('Scheduler Event', 'Scheduler Event'), ('DocType Event', 'DocType Event')], max_length=100),
        ),
        migrations.AlterField(
            model_name='system_settings',
            name='currency_precision',
            field=models.CharField(choices=[('0', ''), ('3', ''), ('7', ''), ('5', ''), ('8', ''), ('1', ''), ('4', ''), ('9', ''), ('6', ''), ('2', '')], max_length=100),
        ),
        migrations.AlterField(
            model_name='system_settings',
            name='date_format',
            field=models.CharField(choices=[('ymd', 'yyyy-mm-dd'), ('dmy', 'dd.mm.yyyy'), ('mdy', 'mm/dd/yyyy'), ('dmy', 'dd/mm/yyyy'), ('dmy', 'dd-mm-yyyy'), ('mdy', 'mm-dd-yyyy')], max_length=100),
        ),
        migrations.AlterField(
            model_name='system_settings',
            name='first_day_of_the_week',
            field=models.CharField(choices=[('Friday', 'Friday'), ('Sunday', 'Sunday'), ('Thursday', 'Thursday'), ('Monday', 'Monday'), ('Saturday', 'Saturday'), ('Wednesday', 'Wednesday'), ('Tuesday', 'Tuesday')], default='Sunday', max_length=100),
        ),
        migrations.AlterField(
            model_name='system_settings',
            name='float_precision',
            field=models.CharField(choices=[('3', ''), ('7', ''), ('5', ''), ('8', ''), ('4', ''), ('9', ''), ('6', ''), ('2', '')], max_length=100),
        ),
        migrations.AlterField(
            model_name='system_settings',
            name='time_format',
            field=models.CharField(choices=[('24', 'HH:mm:ss'), ('12', 'HH:mm')], max_length=100),
        ),
        migrations.AlterField(
            model_name='translation',
            name='contribution_status',
            field=models.CharField(choices=[('verified', 'verified'), ('pending', 'pending'), ('rejected', 'rejected')], max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='desk_theme',
            field=models.CharField(blank=True, choices=[('Automatic', 'Automatic'), ('Dark', 'Dark'), ('Light', 'Light')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='document_follow_frequency',
            field=models.CharField(blank=True, choices=[('Hourly', 'Hourly'), ('All', 'All'), ('Weekly', 'Weekly'), ('Daily', 'Daily')], max_length=100, null=True),
        ),
    ]
