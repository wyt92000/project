# Generated by Django 2.0.6 on 2021-04-04 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('real_name', models.CharField(max_length=30, verbose_name='真实姓名')),
                ('password', models.CharField(max_length=64)),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0)),
                ('register', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '管理员',
                'verbose_name_plural': '管理员',
                'db_table': 'bz_admin',
            },
        ),
    ]
