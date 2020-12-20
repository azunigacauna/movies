# Generated by Django 3.1.4 on 2020-12-20 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MovieDick', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('peliculas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieDick.pelicula')),
            ],
        ),
    ]