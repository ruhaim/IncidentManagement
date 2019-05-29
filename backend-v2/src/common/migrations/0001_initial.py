# Generated by Django 2.2.1 on 2019-05-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_category', models.CharField(max_length=200)),
                ('sub_category', models.CharField(max_length=200)),
                ('sn_top_category', models.CharField(max_length=200)),
                ('sn_sub_category', models.CharField(max_length=200)),
                ('tm_top_category', models.CharField(max_length=200)),
                ('tm_sub_category', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
