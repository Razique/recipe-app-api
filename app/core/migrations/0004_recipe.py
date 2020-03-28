# Generated by Django 3.0.3 on 2020-03-28 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('time_minutes', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('Ingredients', models.ManyToManyField(to='core.Ingredient')),
                ('tags', models.ManyToManyField(to='core.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
