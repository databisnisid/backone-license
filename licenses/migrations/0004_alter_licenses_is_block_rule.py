# Generated by Django 4.2.11 on 2024-06-27 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0003_licenses_is_block_rule_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licenses',
            name='is_block_rule',
            field=models.BooleanField(default=True, verbose_name='Block Rule at Expired'),
        ),
    ]
