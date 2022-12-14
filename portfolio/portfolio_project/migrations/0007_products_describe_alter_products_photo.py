# Generated by Django 4.0.6 on 2022-07-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_project', '0006_remove_rubricks_image_alter_products_all_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='describe',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фотографія'),
        ),
    ]
