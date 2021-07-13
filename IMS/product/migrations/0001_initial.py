# Generated by Django 3.2 on 2021-07-13 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('url_slug', models.SlugField(unique=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='photos/categories/%Y/%m/%d/')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url_slug', models.SlugField(unique=True)),
                ('product_name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('product_max_price', models.CharField(max_length=255)),
                ('product_discount_price', models.CharField(max_length=255)),
                ('product_description', models.TextField()),
                ('product_long_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_stock', models.IntegerField(default=1)),
                ('media_content', models.ImageField(blank=True, null=True, upload_to='photos/products/%Y/%m/%d/')),
                ('is_active', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='subCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('url_slug', models.SlugField(unique=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='photos/subcategories/%Y/%m/%d/')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categories')),
            ],
        ),
        migrations.CreateModel(
            name='recipt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_price', models.CharField(max_length=255)),
                ('coupon_code', models.CharField(max_length=255)),
                ('discount_amount', models.CharField(max_length=255)),
                ('product_status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.products')),
            ],
        ),
        migrations.CreateModel(
            name='productTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_product_count', models.IntegerField(default=1)),
                ('transaction_type', models.CharField(choices=[(1, 'Cash'), (2, 'Card'), (3, 'Crypto')], max_length=255)),
                ('transcation_description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
        ),
        migrations.CreateModel(
            name='productTags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='sub_categories_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.subcategories'),
        ),
        migrations.CreateModel(
            name='productDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('title_details', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
        ),
        migrations.CreateModel(
            name='productAbout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
        ),
    ]
