# Generated by Django 4.1.3 on 2022-12-02 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_berita_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.CharField(max_length=255)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='berita',
            name='kategori_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.kategori'),
        ),
    ]
