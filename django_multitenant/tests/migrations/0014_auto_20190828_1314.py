# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-28 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django_multitenant.fields
import django_multitenant.mixins


class Migration(migrations.Migration):
    dependencies = [
        ("tests", "0013_auto_20190517_1607"),
    ]

    operations = [
        migrations.CreateModel(
            name="MigrationTestModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
            bases=(django_multitenant.mixins.TenantModelMixin, models.Model),
        ),
    ]
