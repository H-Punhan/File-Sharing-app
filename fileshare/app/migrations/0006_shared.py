# Generated by Django 3.2.4 on 2021-06-09 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shared',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shared_file', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('shared', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shared', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]