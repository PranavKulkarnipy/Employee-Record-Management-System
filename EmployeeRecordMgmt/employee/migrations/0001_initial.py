
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer1name', models.CharField(max_length=100, null=True)),
                ('employer1desig', models.CharField(max_length=100, null=True)),
                ('employer1ctc', models.CharField(max_length=100, null=True)),
                ('employer1duration', models.CharField(max_length=100, null=True)),
                ('employer2name', models.CharField(max_length=100, null=True)),
                ('employer2desig', models.CharField(max_length=100, null=True)),
                ('employer2ctc', models.CharField(max_length=100, null=True)),
                ('employer2duration', models.CharField(max_length=100, null=True)),
                ('employer3name', models.CharField(max_length=100, null=True)),
                ('employer3desig', models.CharField(max_length=100, null=True)),
                ('employer3ctc', models.CharField(max_length=100, null=True)),
                ('employer3duration', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursepg', models.CharField(max_length=100, null=True)),
                ('schoolclgpg', models.CharField(max_length=200, null=True)),
                ('yearpassingpg', models.CharField(max_length=20, null=True)),
                ('percentagepg', models.CharField(max_length=30, null=True)),
                ('coursegra', models.CharField(max_length=100, null=True)),
                ('schoolclggra', models.CharField(max_length=200, null=True)),
                ('yearpassinggra', models.CharField(max_length=20, null=True)),
                ('percentagegra', models.CharField(max_length=30, null=True)),
                ('coursessc', models.CharField(max_length=100, null=True)),
                ('schoolclgssc', models.CharField(max_length=200, null=True)),
                ('yearpassingssc', models.CharField(max_length=20, null=True)),
                ('percentagessc', models.CharField(max_length=30, null=True)),
                ('coursehsc', models.CharField(max_length=100, null=True)),
                ('schoolclghsc', models.CharField(max_length=200, null=True)),
                ('yearpassinghsc', models.CharField(max_length=20, null=True)),
                ('percentagehsc', models.CharField(max_length=30, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empcode', models.CharField(max_length=100, null=True)),
                ('empdept', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('joiningdate', models.DateField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
