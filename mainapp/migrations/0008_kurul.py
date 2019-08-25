# Generated by Django 2.2.3 on 2019-08-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20190825_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kurul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurul_name', models.CharField(max_length=150, verbose_name='Kurul Adı')),
                ('kurul_icerik', models.TextField(verbose_name='Kurul İçeriği')),
                ('kurul_ustkurul', models.CharField(blank=True, max_length=100, null=True, verbose_name='Üst Kurul')),
            ],
        ),
    ]