# Generated by Django 4.1.7 on 2023-04-19 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=13)),
                ('address', models.TextField()),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_model', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('product_tax', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('brand_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='ims.brands')),
                ('category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='ims.category')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='ims.supplier')),
                ('product_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='ims.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='ims.supplier'),
        ),
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_item', models.IntegerField()),
                ('name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='ims.customer')),
                ('product_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='ims.product')),
            ],
        ),
        migrations.AddField(
            model_name='brands',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='ims.category'),
        ),
    ]
