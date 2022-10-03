# Generated by Django 4.1 on 2022-10-03 01:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('idtype', models.CharField(max_length=300, verbose_name='ID Type')),
                ('idnumber', models.CharField(max_length=30, verbose_name='ID Number')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventory', models.BigAutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('isbn', models.CharField(max_length=45)),
                ('purchasedQuantity', models.IntegerField(default=0)),
                ('soldQuantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('sale', models.AutoField(primary_key=True, serialize=False)),
                ('dateSales', models.DateTimeField()),
                ('amount', models.IntegerField(default=0)),
                ('totalOrder', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('product', models.AutoField(primary_key=True, serialize=False)),
                ('name_prod', models.CharField(max_length=90)),
                ('author', models.CharField(max_length=45)),
                ('editorial', models.CharField(max_length=45)),
                ('category', models.CharField(max_length=45)),
                ('type_prod', models.CharField(max_length=45)),
                ('num_page', models.BigIntegerField()),
                ('isbn', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=250)),
                ('rank', models.CharField(max_length=45)),
                ('format_prod', models.CharField(max_length=45)),
                ('presentation', models.CharField(max_length=45)),
                ('image', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=3, max_digits=6)),
                ('visits', models.BigIntegerField()),
                ('description', models.CharField(max_length=250)),
                ('name_cat', models.CharField(max_length=45)),
                ('subcategory', models.CharField(max_length=45)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookFaceApp.inventory')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookFaceApp.sales')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.CharField(max_length=100, unique=True, verbose_name='Sesion')),
                ('status', models.CharField(max_length=45, verbose_name='Status')),
                ('creationAt', models.DateField()),
                ('updateAt', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.IntegerField(default=0)),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookFaceApp.sales')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
