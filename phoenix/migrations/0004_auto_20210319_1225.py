# Generated by Django 3.1.6 on 2021-03-19 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0003_auto_20210319_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarkovitem',
            name='craftingstation',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='craftedat', to='phoenix.tarkovhideout'),
        ),
    ]