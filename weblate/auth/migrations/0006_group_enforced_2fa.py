# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 5.0.7 on 2024-08-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("weblate_auth", "0005_invitation_full_name_invitation_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="enforced_2fa",
            field=models.BooleanField(
                default=False,
                help_text="Requires users to have two-factor authentication configured.",
                verbose_name="Enforced two-factor authentication",
            ),
        ),
    ]
