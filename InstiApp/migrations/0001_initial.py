# Generated by Django 4.2.4 on 2023-08-13 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(blank=True, max_length=150, null=True)),
                ('Age', models.IntegerField(default=0)),
                ('ResidencePhone', models.CharField(blank=True, max_length=20, null=True)),
                ('WhatsApp', models.CharField(blank=True, max_length=55, null=True)),
                ('Adress', models.TextField(blank=True, max_length=300, null=True)),
                ('SelfDescription', models.TextField(blank=True, max_length=450, null=True)),
                ('InstrumentChoice', models.IntegerField(choices=[(0, 'Violin'), (1, 'Viola'), (2, 'Cello')], default=2)),
                ('DateCreation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]