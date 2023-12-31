# Generated by Django 4.2.6 on 2023-10-23 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_author_email_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='email',
            new_name='user_email',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
    ]
