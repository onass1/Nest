# Generated by Django 5.1.1 on 2024-09-09 16:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("github", "0042_alter_issue_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="updated_at",
            field=models.DateTimeField(db_index=True, verbose_name="Updated at"),
        ),
    ]