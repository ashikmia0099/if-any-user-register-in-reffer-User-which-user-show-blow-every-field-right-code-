# Generated by Django 4.2.11 on 2024-05-28 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Student_Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_image',
            name='Image',
            field=models.ImageField(blank=True, default=' ', null=True, upload_to='Student_Profile/media/'),
        ),
        migrations.CreateModel(
            name='Student_Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Certificate', models.FileField(blank=True, default=' ', null=True, upload_to='Student_Profile/media/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
