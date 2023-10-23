# Generated by Django 4.2.6 on 2023-10-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_comment_options_rename_body_comment_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.CharField(max_length=80),
        ),
    ]