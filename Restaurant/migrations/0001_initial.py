# Generated by Django 3.2.7 on 2022-10-11 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('Ethnics', 'Ethnics'), ('Fast Food', 'Fast Food'), ('Fast Casual', 'Fast Casual'), ('Casual Dining', 'Casual Dining'), ('Premium Casual', 'Premium Casual'), ('family Style', 'family Style'), ('Fine Dining', 'Fine Dining'), ('Cafeteria', 'Cafeteria'), ('Coffer House', 'Coffer House')], max_length=200, null=True)),
                ('cuisin', models.CharField(choices=[('Bangladeshi', 'Bangladeshi'), ('Chinses', 'Chinses'), ('Indian', 'Indian'), ('Pakistani', 'Pakistani'), ('Thai', 'Thai'), ('Arabian', 'Arabian')], max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenter_name', models.CharField(max_length=200)),
                ('comment_body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Restaurant.restaurant')),
            ],
        ),
    ]
