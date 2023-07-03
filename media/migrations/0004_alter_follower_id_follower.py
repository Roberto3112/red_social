# Generated by Django 4.2.1 on 2023-06-01 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_image'),
        ('media', '0003_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='id_follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='accounts.profile'),
        ),
    ]
