# Generated by Django 3.0.6 on 2020-06-08 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion', models.TextField(help_text='Descripción del producto')),
                ('stock', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nombre'],
            },
        ),
    ]
