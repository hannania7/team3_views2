# Generated by Django 3.2.3 on 2021-09-23 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0002_auto_20210919_0258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.CharField(blank=True, max_length=255, null=True)),
                ('shampoo', models.CharField(blank=True, max_length=255, null=True)),
                ('perm', models.CharField(blank=True, max_length=255, null=True)),
                ('dye', models.CharField(blank=True, max_length=255, null=True)),
                ('current_hair', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.CharField(blank=True, max_length=255, null=True)),
                ('care_prefer', models.CharField(blank=True, max_length=255, null=True)),
                ('buying_point', models.CharField(blank=True, max_length=255, null=True)),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'survey',
                'managed': False,
            },
        ),
    ]