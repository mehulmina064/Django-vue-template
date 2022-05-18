# Generated by Django 3.2.6 on 2022-05-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20220517_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_import',
            name='Pending',
            field=models.CharField(blank=True, choices=[('Error', 'Error'), ('Success', 'Success'), ('Partial Success', 'Partial Success')], default='Success', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='docfield',
            name='fieldtype',
            field=models.CharField(blank=True, choices=[('Float', ''), ('Dynamic Link', ''), ('Currency', ''), ('Column Break', ''), ('Code', ''), ('Heading', ''), ('Password', ''), ('Read Only', ''), ('Small Text', ''), ('Table MultiSelect', ''), ('HTML Editor', ''), ('Geolocation', ''), ('Data', ''), ('Button', ''), ('Int', ''), ('Datetime', ''), ('Percent', ''), ('Barcode', ''), ('Markdown Editor', ''), ('Link', ''), ('Check', ''), ('Time', ''), ('Duration', ''), ('Table', ''), ('Color', ''), ('Tab Break', ''), ('Image', ''), ('Text', ''), ('JSON', ''), ('Attach', ''), ('Select', ''), ('Rating', ''), ('Autocomplete', ''), ('Signature', ''), ('Section Break', ''), ('Text Editor', ''), ('Date', ''), ('Icon', ''), ('HTML', ''), ('Long Text', ''), ('Attach Image', ''), ('Fold', ''), ('Phone', '')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='docfield',
            name='precision',
            field=models.CharField(blank=True, choices=[('8', ''), ('1', ''), ('3', ''), ('4', ''), ('5', ''), ('6', ''), ('2', ''), ('7', ''), ('9', '')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='doctype',
            name='document_type',
            field=models.CharField(blank=True, choices=[('System', 'System'), ('Document', 'Document'), ('Setup', 'Setup'), ('Other', 'Other')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctype',
            name='name_case',
            field=models.CharField(blank=True, choices=[('Title Case', 'Title Case'), ('UPPER CASE', 'UPPER CASE')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctype',
            name='sort_order',
            field=models.CharField(blank=True, choices=[('ASC', 'ASC'), ('DESC', 'DESC')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctype_state',
            name='color',
            field=models.CharField(choices=[('1', 'Blue'), ('2', 'Cyan'), ('8', 'Purple'), ('10', 'Yellow'), ('9', 'Red'), ('4', 'Green'), ('7', 'Pink'), ('5', 'Light Blue'), ('6', 'Orange'), ('3', 'Gray')], max_length=100),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='reference_doctype',
            field=models.CharField(choices=[('System', 'System'), ('Document', 'Document'), ('Setup', 'Setup'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='navbar_item',
            name='item_type',
            field=models.CharField(choices=[('Separator', 'Separator'), ('Action', 'Action'), ('Route', 'Route')], max_length=100),
        ),
        migrations.AlterField(
            model_name='package',
            name='license_type',
            field=models.CharField(choices=[('MIT License', 'MIT License'), ('GNU Affero General', 'GNU Affero General'), ('GNU General Public License', 'GNU General Public License'), ('Public License', 'Public License')], max_length=255),
        ),
        migrations.AlterField(
            model_name='prepared_report',
            name='status',
            field=models.CharField(choices=[('Queued', 'Queued'), ('Completed', 'Completed'), ('Error', 'Error')], max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.CharField(choices=[('Report Builder', 'Report Builder'), ('Script Report', 'Script Report'), ('Query Report', 'Query Report'), ('Custom Report', 'Custom Report')], max_length=100),
        ),
        migrations.AlterField(
            model_name='report_column',
            name='fieldtype',
            field=models.CharField(choices=[('IntigerField', 'IntigerField'), ('Float', 'Float'), ('ManyToOneRelation', 'ManyToOneRelation'), ('ManyToManyField', 'ManyToManyField'), ('OneToManyRelation', 'OneToManyRelation'), ('Date', 'Date'), ('ForeignKey', 'ForeignKey'), ('boolean', 'boolean'), ('DateField', 'DateField'), ('Currency', 'Currency'), ('OneToOneRelation', 'OneToOneRelation'), ('charfield', 'charfield')], max_length=255),
        ),
        migrations.AlterField(
            model_name='scheduled_job_log',
            name='status',
            field=models.CharField(choices=[('Failed', 'Failed'), ('Complete', 'Complete'), ('Scheduled', 'Scheduled')], max_length=20),
        ),
        migrations.AlterField(
            model_name='scheduled_job_type',
            name='frequency',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Hourly Long', 'Hourly Long'), ('All', 'All'), ('Hourly', 'Hourly'), ('Annual', 'Annual'), ('Yearly', 'Yearly'), ('Cron', 'Cron'), ('Weekly', 'Weekly'), ('Weekly Long', 'Weekly Long'), ('Monthly Long', 'Monthly Long'), ('Monthly', 'Monthly'), ('Daily Long', 'Daily Long')], max_length=100),
        ),
        migrations.AlterField(
            model_name='server_script',
            name='doctype_event',
            field=models.CharField(choices=[('Before Insert', 'Before Insert'), ('Before Validate', 'Before Validate'), ('After Delete', 'After Delete'), ('After Cancel', 'After Cancel'), ('After Insert', 'After Insert'), ('Before Delete', 'Before Delete'), ('After Save', 'After Save'), ('Before Cancel', 'Before Cancel'), ('Before Submit', 'Before Submit'), ('Before Save', 'Before Save'), ('Before Save', 'After Save'), ('On Payment Authorization', 'On Payment Authorization'), ('After Submit', 'After Submit')], max_length=100),
        ),
        migrations.AlterField(
            model_name='server_script',
            name='event_frequency',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Hourly Long', 'Hourly Long'), ('All', 'All'), ('Hourly', 'Hourly'), ('Annual', 'Annual'), ('Yearly', 'Yearly'), ('Cron', 'Cron'), ('Weekly', 'Weekly'), ('Weekly Long', 'Weekly Long'), ('Monthly Long', 'Monthly Long'), ('Monthly', 'Monthly'), ('Daily Long', 'Daily Long')], max_length=100),
        ),
        migrations.AlterField(
            model_name='system_settings',
            name='currency_precision',
            field=models.CharField(choices=[('8', ''), ('1', ''), ('3', ''), ('4', ''), ('0', ''), ('5', ''), ('6', ''), ('2', ''), ('7', ''), ('9', '')], max_length=100),
        ),
        migrations.AlterField(
            model_name='system_settings',
            name='date_format',
            field=models.CharField(choices=[('ymd', 'yyyy-mm-dd'), ('dmy', 'dd.mm.yyyy'), ('mdy', 'mm-dd-yyyy'), ('dmy', 'dd-mm-yyyy'), ('mdy', 'mm/dd/yyyy'), ('dmy', 'dd/mm/yyyy')], max_length=100),
        ),
        migrations.AlterField(
            model_name='system_settings',
            name='first_day_of_the_week',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday')], default='Sunday', max_length=100),
        ),
        migrations.AlterField(
            model_name='system_settings',
            name='float_precision',
            field=models.CharField(choices=[('8', ''), ('3', ''), ('4', ''), ('5', ''), ('6', ''), ('2', ''), ('7', ''), ('9', '')], max_length=100),
        ),
        migrations.AlterField(
            model_name='translation',
            name='contribution_status',
            field=models.CharField(choices=[('pending', 'pending'), ('rejected', 'rejected'), ('verified', 'verified')], max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='desk_theme',
            field=models.CharField(blank=True, choices=[('Light', 'Light'), ('Dark', 'Dark'), ('Automatic', 'Automatic')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='document_follow_frequency',
            field=models.CharField(blank=True, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Hourly', 'Hourly'), ('All', 'All')], max_length=100, null=True),
        ),
    ]