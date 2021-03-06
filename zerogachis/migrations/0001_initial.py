# Generated by Django 2.2.18 on 2021-03-25 07:55

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZerogachisSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(default='magazin')),
                ('picture', models.TextField()),
                ('geom', djgeojson.fields.PointField()),
                ('partenaire', models.BooleanField()),
            ],
        ),
    ]
