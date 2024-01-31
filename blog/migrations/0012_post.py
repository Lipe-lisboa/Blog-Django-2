# Generated by Django 5.0.1 on 2024-01-31 15:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_page'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('slug', models.SlugField(blank=True, default=None, max_length=70, null=True, unique=True)),
                ('excerpt', models.CharField(max_length=150)),
                ('is_published', models.BooleanField(default=False, help_text='Este campo precisa estar marcado para o post ser exibida publicamente')),
                ('content', models.TextField()),
                ('cover', models.ImageField(blank=True, upload_to='posts/%Y/%m/')),
                ('cover_in_post_content', models.BooleanField(default=True, help_text='Este campo precisa estar marcado para exibir a capa entro do post')),
                ('date_Time_created', models.DateTimeField(auto_now_add=True)),
                ('date_Time_updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, default='', to='blog.tag')),
                ('user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
