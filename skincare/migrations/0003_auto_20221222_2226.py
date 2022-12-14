# Generated by Django 3.2 on 2022-12-22 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skincare', '0002_auto_20221203_0409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skincare',
            options={'ordering': ['usage'], 'verbose_name': 'Skincare Product'},
        ),
        migrations.RenameField(
            model_name='skincare',
            old_name='alchol_free',
            new_name='alcohol_free',
        ),
        migrations.RenameField(
            model_name='skincare',
            old_name='crultey_free',
            new_name='cruelty_free',
        ),
        migrations.RemoveField(
            model_name='skincare',
            name='skin_concern',
        ),
        migrations.AddField(
            model_name='skincare',
            name='skin_concern',
            field=models.ManyToManyField(to='skincare.SkinConcern'),
        ),
        migrations.RemoveField(
            model_name='skincare',
            name='skin_type',
        ),
        migrations.AddField(
            model_name='skincare',
            name='skin_type',
            field=models.ManyToManyField(to='skincare.SkinType'),
        ),
    ]
