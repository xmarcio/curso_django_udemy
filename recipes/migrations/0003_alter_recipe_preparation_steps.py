# Generated by Django 4.1.5 on 2023-01-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_category_options_alter_recipe_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='preparation_steps',
            field=models.TextField(),
        ),
    ]
