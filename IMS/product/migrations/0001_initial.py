# Generated by Django 3.2 on 2021-05-11 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ims_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('url_slug', models.CharField(max_length=255)),
                ('thumbnail', models.FileField(upload_to='')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url_slug', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('product_max_price', models.CharField(max_length=255)),
                ('product_discount_price', models.CharField(max_length=255)),
                ('product_description', models.TextField()),
                ('product_long_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_stock', models.IntegerField(default=1)),
                ('is_active', models.IntegerField(default=1)),
                ('added_by_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims_users.staffuser')),
            ],
        ),
        migrations.CreateModel(
            name='productVarient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='subCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('url_slug', models.CharField(max_length=255)),
                ('thumbnail', models.FileField(upload_to='')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categories')),
            ],
        ),
        migrations.CreateModel(
            name='productVarientItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
                ('product_varient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productvarient')),
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
            name='productMedia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('media_type', models.CharField(choices=[(1, 'Image'), (2, 'Video')], max_length=255)),
                ('media_content', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
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
        migrations.CreateModel(
            name='customerOrders',
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
    ]
