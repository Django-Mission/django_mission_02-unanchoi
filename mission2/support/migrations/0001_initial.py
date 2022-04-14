# Generated by Django 4.0.4 on 2022-04-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('category', models.CharField(choices=[('python', 'python'), ('mission', 'mission'), ('django', 'django')], default='mission', max_length=30)),
                ('answer', models.TextField()),
                ('writer', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('editor', models.CharField(max_length=50)),
                ('edited_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]