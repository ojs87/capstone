# Generated by Django 3.1.6 on 2021-03-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0005_auto_20210319_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='TarkovQuestTester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('questhref', models.URLField(blank=True)),
                ('objectives', models.JSONField(blank=True, default=dict)),
                ('rewards', models.JSONField(blank=True, default=dict)),
                ('requirements', models.JSONField(blank=True, default=dict)),
                ('questgiver', models.CharField(blank=True, max_length=128)),
                ('prereqs', models.JSONField(blank=True, default=dict)),
                ('leadsto', models.JSONField(blank=True, default=dict)),
            ],
        ),
        migrations.AlterField(
            model_name='tarkovitemquest',
            name='foundinraid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='tarkovquest',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='tarkovquest',
            name='leadsto',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='tarkovquest',
            name='objectives',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='tarkovquest',
            name='prereqs',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='tarkovquest',
            name='questgiver',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='tarkovquest',
            name='rewards',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
