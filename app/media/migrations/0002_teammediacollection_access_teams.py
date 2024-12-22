# Generated by Django 5.0.7 on 2024-12-01 21:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("media", "0001_initial"),
        ("teams", "0003_remove_team_format_prompt_remove_team_summary_prompt"),
    ]

    operations = [
        migrations.AddField(
            model_name="teammediacollection",
            name="access_teams",
            field=models.ManyToManyField(
                blank=True,
                help_text="You can share this media collection with other teams on this platform. You can search teams by team name or team owner email address.",
                related_name="media_collection_access",
                to="teams.team",
            ),
        ),
    ]
