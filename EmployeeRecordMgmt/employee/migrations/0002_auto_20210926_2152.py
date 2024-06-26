
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='employer1desig',
            new_name='company1desig',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='employer1duration',
            new_name='company1duration',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='employer1ctc',
            new_name='company1name',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='employer1name',
            new_name='company1salary',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='employer2ctc',
            new_name='company2desig',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='employer2desig',
            new_name='company2duration',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='employer2duration',
            new_name='company2name',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='employer2name',
            new_name='company2salary',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='employer3ctc',
            new_name='company3desig',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='employer3desig',
            new_name='company3duration',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='employer3duration',
            new_name='company3name',
        ),
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='employer3name',
            new_name='company3salary',
        ),
    ]
