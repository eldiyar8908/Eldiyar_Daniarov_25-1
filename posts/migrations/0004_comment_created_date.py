# Generated by Django 4.1.6 on 2023-02-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]