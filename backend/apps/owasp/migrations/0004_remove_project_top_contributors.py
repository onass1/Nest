# Generated by Django 5.1.1 on 2024-09-22 23:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("owasp", "0003_project_top_contributors"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="top_contributors",
        ),
    ]
