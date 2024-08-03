# Generated by Django 5.0.7 on 2024-08-03 20:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("modersite", "0005_remove_alertribbon_resume_alertribbon_summary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alertribbon",
            name="position",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Top left"),
                    (1, "Bottom left"),
                    (2, "Top right"),
                    (3, "Bottom right"),
                    (4, "Top center"),
                    (5, "Bottom center"),
                ],
                db_index=True,
                default=2,
                verbose_name="Position",
            ),
        ),
        migrations.AlterField(
            model_name="alertribbon",
            name="start_date",
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name="Start date"),
        ),
    ]
