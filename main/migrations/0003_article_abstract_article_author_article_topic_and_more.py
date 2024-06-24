# Generated by Django 5.0.6 on 2024-06-23 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_title_article_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='abstract',
            field=models.CharField(default='No abstract available.', max_length=200),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.CharField(default='General', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(default='Untitled', max_length=100),
        ),
    ]
