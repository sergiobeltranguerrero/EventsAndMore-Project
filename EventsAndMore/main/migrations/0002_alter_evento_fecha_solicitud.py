<<<<<<< HEAD
# Generated by Django 4.0.4 on 2022-05-26 09:17
=======
# Generated by Django 4.0.4 on 2022-05-27 15:13
>>>>>>> sergio

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_solicitud',
<<<<<<< HEAD
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 9, 17, 31, 70747)),
=======
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 13, 3, 232440)),
>>>>>>> sergio
        ),
    ]
