# Generated by Django 3.1.6 on 2021-03-19 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TarkovHideout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.RenameField(
            model_name='tarkovitem',
            old_name='FIRquest',
            new_name='firquest',
        ),
        migrations.AddField(
            model_name='tarkovquest',
            name='leadsto',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='tarkovquest',
            name='prereqs',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='tarkovquest',
            name='questgiver',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TarkovItemHideout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level1itemcount', models.IntegerField()),
                ('level2itemcount', models.IntegerField()),
                ('level3itemcount', models.IntegerField()),
                ('tarkovhideout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phoenix.tarkovhideout')),
                ('tarkovitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phoenix.tarkovitem')),
            ],
        ),
        migrations.AddField(
            model_name='tarkovitem',
            name='craftingstation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='stationmats', to='phoenix.tarkovhideout'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarkovitem',
            name='hideout',
            field=models.ManyToManyField(through='phoenix.TarkovItemHideout', to='phoenix.TarkovHideout'),
        ),
    ]
