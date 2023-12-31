# Generated by Django 4.2.1 on 2023-05-10 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_riss', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=255)),
                ('l_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('logins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_riss.user_log')),
            ],
        ),
    ]
