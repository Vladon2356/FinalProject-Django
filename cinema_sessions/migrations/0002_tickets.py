# Generated by Django 4.0.4 on 2022-05-10 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cinema_sessions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tickets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("column", models.SmallIntegerField()),
                ("row", models.SmallIntegerField()),
                ("sold", models.BooleanField(default=False)),
                ("ticket_price", models.SmallIntegerField()),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to="cinema_sessions.sessions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ticket",
                "verbose_name_plural": "Tickets",
            },
        ),
    ]
