# Generated by Django 4.0.6 on 2022-07-23 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_project', '0005_alter_products_rubrick'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rubricks',
            name='image',
        ),
        migrations.AlterField(
            model_name='products',
            name='all_rating',
            field=models.IntegerField(default=0, verbose_name='Увесь рейтинг'),
        ),
        migrations.AlterField(
            model_name='products',
            name='avaibility',
            field=models.IntegerField(default=0, verbose_name='кількість на базі'),
        ),
        migrations.AlterField(
            model_name='products',
            name='number_of_rating',
            field=models.IntegerField(default=0, verbose_name='кількість людей які поклали оцінку'),
        ),
        migrations.AlterField(
            model_name='products',
            name='rubrick',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rubricks', to='portfolio_project.rubricks'),
        ),
        migrations.AlterField(
            model_name='products',
            name='tag',
            field=models.ManyToManyField(to='portfolio_project.tags', verbose_name='Фірми'),
        ),
    ]
