# Generated by Django 5.1 on 2024-08-19 23:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Repository",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("key", models.CharField(max_length=100, verbose_name="Key")),
                (
                    "description",
                    models.CharField(default="", max_length=500, verbose_name="Description"),
                ),
                (
                    "default_branch",
                    models.CharField(default="", max_length=100, verbose_name="Default branch"),
                ),
                (
                    "homepage",
                    models.CharField(default="", max_length=100, verbose_name="Homepage"),
                ),
                ("language", models.CharField(default="", max_length=50, verbose_name="Language")),
                ("license", models.CharField(default="", max_length=100, verbose_name="License")),
                ("size", models.PositiveIntegerField(default=0, verbose_name="Size in KB")),
                ("topics", models.JSONField(default=list, verbose_name="Topics")),
                ("is_archived", models.BooleanField(default=False, verbose_name="Is archived")),
                ("is_fork", models.BooleanField(default=False, verbose_name="Is fork")),
                ("is_template", models.BooleanField(default=False, verbose_name="Is template")),
                (
                    "has_downloads",
                    models.BooleanField(default=False, verbose_name="Has downloads"),
                ),
                ("has_issues", models.BooleanField(default=False, verbose_name="Has issues")),
                ("has_pages", models.BooleanField(default=False, verbose_name="Has pages")),
                ("has_projects", models.BooleanField(default=False, verbose_name="Has projects")),
                ("has_wiki", models.BooleanField(default=False, verbose_name="Has wiki")),
                (
                    "forks_count",
                    models.PositiveIntegerField(default=0, verbose_name="Forks count"),
                ),
                (
                    "open_issues_count",
                    models.PositiveIntegerField(default=0, verbose_name="Open issues count"),
                ),
                (
                    "stars_count",
                    models.PositiveIntegerField(default=0, verbose_name="Stars count"),
                ),
                (
                    "subscribers_count",
                    models.PositiveIntegerField(default=0, verbose_name="Subscribers count"),
                ),
                (
                    "platform",
                    models.CharField(
                        choices=[("github", "GitHub")],
                        default="github",
                        max_length=10,
                        verbose_name="Platform",
                    ),
                ),
                ("pushed_at", models.DateTimeField(verbose_name="Pushed at")),
                ("original_created_at", models.DateTimeField(verbose_name="Original created_at")),
                ("original_updated_at", models.DateTimeField(verbose_name="Original updated_at")),
                (
                    "owner_login",
                    models.CharField(default="", max_length=100, verbose_name="Owner login"),
                ),
                (
                    "owner_type",
                    models.CharField(
                        choices=[("organization", "Organization"), ("user", "User")],
                        default="user",
                        max_length=20,
                        verbose_name="Owner type",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Repositories",
                "db_table": "repositories",
                "constraints": [
                    models.UniqueConstraint(
                        fields=("key", "platform", "owner_login"), name="unique_key_platform_owner"
                    )
                ],
            },
        ),
    ]