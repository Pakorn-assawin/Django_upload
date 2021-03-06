# Generated by Django 3.2.5 on 2021-07-31 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(blank=True, max_length=100, null=True)),
                ('job_name', models.CharField(blank=True, max_length=100, null=True)),
                ('job_data', models.DateField(auto_now_add=True)),
                ('job_time', models.TimeField(auto_now_add=True)),
                ('job_officerid', models.CharField(blank=True, max_length=100, null=True)),
                ('job_picture', models.URLField(blank=True, max_length=500, null=True)),
                ('vol_name', models.CharField(blank=True, max_length=100, null=True)),
                ('eq_name', models.CharField(blank=True, max_length=100, null=True)),
                ('subeq_name', models.CharField(blank=True, max_length=100, null=True)),
                ('abnor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('abnor_other', models.CharField(blank=True, max_length=200, null=True)),
                ('nameimageold', models.CharField(blank=True, max_length=100, null=True)),
                ('nameimagenew', models.CharField(blank=True, max_length=100, null=True)),
                ('pathimage', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
