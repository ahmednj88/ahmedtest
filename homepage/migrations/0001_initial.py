# Generated by Django 3.1.7 on 2021-02-28 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('detailsofacivity', models.CharField(max_length=200, null=True)),
                ('typeofactiviy', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('street', models.CharField(max_length=200, null=True)),
                ('allay', models.CharField(max_length=200, null=True)),
                ('long', models.IntegerField(max_length=200, null=True)),
                ('lg', models.IntegerField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=80)),
                ('phone', models.IntegerField(max_length=40, null=True)),
                ('email_user', models.EmailField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.location')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loction_id', models.CharField(max_length=200, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user')),
            ],
        ),
        migrations.CreateModel(
            name='Pro_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('bio', models.CharField(max_length=200, null=True)),
                ('facebook_id', models.IntegerField(max_length=90, null=True)),
                ('insta_id', models.IntegerField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('unspacifide', 'Unspacifide')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('body', models.CharField(max_length=200, null=True)),
                ('date_of_start', models.CharField(max_length=100, null=True)),
                ('how_many_days', models.IntegerField(max_length=365, null=True)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.location')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user')),
            ],
        ),
        migrations.CreateModel(
            name='Conversation_reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_text', models.CharField(max_length=200, null=True)),
                ('time', models.CharField(max_length=75, null=True)),
                ('status', models.CharField(max_length=300, null=True)),
                ('c_id', models.CharField(max_length=200, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user')),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_text', models.CharField(max_length=200, null=True)),
                ('user_id', models.CharField(max_length=200, null=True)),
                ('time', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(max_length=200, null=True)),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.conversation_reply')),
            ],
        ),
        migrations.CreateModel(
            name='acti_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.activity')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.post')),
            ],
        ),
    ]
