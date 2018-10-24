# Generated by Django 2.1.2 on 2018-10-24 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=150)),
                ('qty', models.IntegerField(default=0)),
                ('brand', models.CharField(max_length=150)),
                ('photo', models.FileField(blank=True, upload_to='')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.Category')),
            ],
        ),
    ]