# Generated by Django 4.2.5 on 2023-10-09 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('unit_value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('main_units', models.ManyToManyField(to='course.main_unit')),
            ],
        ),
        migrations.CreateModel(
            name='Public_unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('unit_value', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='term',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='student',
            name='university',
        ),
        migrations.RenameModel(
            old_name='University',
            new_name='Term',
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=256)),
                ('unit', models.ManyToManyField(to='course.main_unit')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.major')),
                ('students', models.ManyToManyField(to='course.student')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.term')),
            ],
        ),
        migrations.AddField(
            model_name='major',
            name='public_units',
            field=models.ManyToManyField(to='course.public_unit'),
        ),
        migrations.AddField(
            model_name='student',
            name='major',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.major'),
            preserve_default=False,
        ),
    ]
