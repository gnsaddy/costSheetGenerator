# Generated by Django 3.0.8 on 2020-07-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_cmt_mainlabel_polybag_thread'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='threadColor',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
