# Generated by Django 5.1.6 on 2025-03-24 21:19

import uuid
from typing import ClassVar
from decimal import Decimal

import django.core.validators
import django.db.models.deletion
from django.db import models, migrations


class Migration(migrations.Migration):
    initial = True

    dependencies: ClassVar = []

    operations: ClassVar = [
        migrations.CreateModel(
            name="Bank",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=255)),
                (
                    "currency",
                    models.CharField(
                        choices=[("NGN", "Ngn")], default="NGN", max_length=100
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
            ],
            options={
                "db_table": "banks",
                "indexes": [
                    models.Index(fields=["code"], name="banks_code_740a70_idx"),
                    models.Index(fields=["name"], name="banks_name_f09ef4_idx"),
                ],
            },
        ),
        migrations.CreateModel(
            name="StateLGA",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("state", models.CharField(max_length=100)),
                ("lga", models.CharField(max_length=100)),
                ("created_at", models.DateField(auto_now_add=True)),
            ],
            options={
                "db_table": "state_lgas",
                "indexes": [
                    models.Index(fields=["state"], name="state_lgas_state_86b8fc_idx")
                ],
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=20)),
                ("profile_picture", models.CharField(max_length=255, null=True)),
                ("tier", models.IntegerField(default=1)),
                ("pin", models.CharField(max_length=10, null=True)),
                ("otp", models.CharField(max_length=10, null=True)),
                ("is_validated", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                ("is_enabled", models.BooleanField(default=False)),
                ("is_deleted", models.BooleanField(default=False)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("last_updated_at", models.DateField(auto_now=True)),
                (
                    "state_lga",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.statelga",
                    ),
                ),
            ],
            options={
                "db_table": "users",
            },
        ),
        migrations.CreateModel(
            name="UserKYCInformation",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("bvn", models.CharField(max_length=20, null=True)),
                (
                    "document_type",
                    models.CharField(
                        choices=[
                            ("Int'l Passport", "Intl Passport"),
                            ("Voter's Card", "Voters Card"),
                            ("Driver's Licence", "Drivers Licence"),
                            ("NIN", "Nin"),
                        ],
                        max_length=30,
                        null=True,
                    ),
                ),
                ("document_id", models.CharField(max_length=255, null=True)),
                ("is_bvn_verified", models.BooleanField(default=False, null=True)),
                ("is_document_verified", models.BooleanField(default=False, null=True)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("last_updated_at", models.DateField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="kyc",
                        to="api.user",
                    ),
                ),
            ],
            options={
                "db_table": "users_kyc_information",
            },
        ),
        migrations.CreateModel(
            name="UserNextOfKin",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=255, null=True)),
                ("last_name", models.CharField(max_length=255, null=True)),
                ("address", models.CharField(max_length=255, null=True)),
                ("phone_number", models.CharField(max_length=20, null=True)),
                ("email", models.EmailField(max_length=255, null=True)),
                (
                    "relationship",
                    models.CharField(
                        choices=[
                            ("father", "Father"),
                            ("mother", "Mother"),
                            ("brother", "Brother"),
                            ("sister", "Sister"),
                            ("uncle", "Uncle"),
                            ("aunt", "Aunt"),
                            ("cousin", "Cousin"),
                            ("nephew", "Nephew"),
                            ("niece", "Niece"),
                            ("son", "Son"),
                            ("daughter", "Daughter"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("last_updated_at", models.DateField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="next_of_kin",
                        to="api.user",
                    ),
                ),
            ],
            options={
                "db_table": "users_nest_of_kin",
            },
        ),
        migrations.CreateModel(
            name="UserWithdrawalInformation",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "currency",
                    models.CharField(
                        choices=[("NGN", "Ngn")], default="NGN", max_length=100
                    ),
                ),
                ("bank_code", models.CharField(max_length=10)),
                ("bank_name", models.CharField(max_length=255)),
                ("account_number", models.CharField(max_length=30)),
                ("account_name", models.CharField(max_length=255)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("last_updated_at", models.DateField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="withdrawal_informations",
                        to="api.user",
                    ),
                ),
            ],
            options={
                "db_table": "users_withdrawal_information",
            },
        ),
        migrations.CreateModel(
            name="Wallet",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("account_number", models.CharField(max_length=30, unique=True)),
                (
                    "currency",
                    models.CharField(
                        choices=[("NGN", "Ngn")], default="NGN", max_length=100
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("tag", models.CharField(max_length=100, null=True)),
                (
                    "daily_transaction_limit",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0"), max_digits=14
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_enabled", models.BooleanField(default=True)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("last_updated_at", models.DateField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wallets",
                        to="api.user",
                    ),
                ),
            ],
            options={
                "db_table": "wallets",
            },
        ),
        migrations.CreateModel(
            name="WalletLimit",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "tier",
                    models.IntegerField(
                        default=1,
                        unique=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                1, "Account tier is not valid"
                            ),
                            django.core.validators.MaxValueValidator(
                                3, "Account tier is not valid"
                            ),
                        ],
                    ),
                ),
                (
                    "daily_transaction_limit",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("1"), max_digits=14
                    ),
                ),
                (
                    "total_balance_limit",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("1"), max_digits=14
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("last_updated_at", models.DateField(auto_now=True)),
            ],
            options={
                "db_table": "wallet_limits",
                "indexes": [
                    models.Index(
                        fields=["created_at"], name="wallet_limi_created_7e2a5a_idx"
                    ),
                    models.Index(
                        fields=["last_updated_at"],
                        name="wallet_limi_last_up_c7b1bc_idx",
                    ),
                ],
            },
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(fields=["first_name"], name="users_first_n_0c5a67_idx"),
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(fields=["last_name"], name="users_last_na_5e9a3c_idx"),
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(fields=["tier"], name="users_tier_8aada5_idx"),
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(
                fields=["is_validated"], name="users_is_vali_0d788b_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(fields=["is_active"], name="users_is_acti_847b48_idx"),
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(fields=["is_enabled"], name="users_is_enab_c3c6b9_idx"),
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(fields=["created_at"], name="users_created_6541e9_idx"),
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(
                fields=["last_updated_at"], name="users_last_up_c6daeb_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="userkycinformation",
            index=models.Index(
                fields=["is_bvn_verified"], name="users_kyc_i_is_bvn__ba2416_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="userkycinformation",
            index=models.Index(
                fields=["is_document_verified"], name="users_kyc_i_is_docu_7ef477_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="userkycinformation",
            index=models.Index(
                fields=["created_at"], name="users_kyc_i_created_4bb709_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="userkycinformation",
            index=models.Index(
                fields=["last_updated_at"], name="users_kyc_i_last_up_99aeda_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="usernextofkin",
            index=models.Index(
                fields=["created_at"], name="users_nest__created_968b96_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="usernextofkin",
            index=models.Index(
                fields=["last_updated_at"], name="users_nest__last_up_ffece8_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="wallet",
            index=models.Index(
                fields=["account_number"], name="wallets_account_6b3c19_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="wallet",
            index=models.Index(fields=["currency"], name="wallets_currenc_378bd9_idx"),
        ),
        migrations.AddIndex(
            model_name="wallet",
            index=models.Index(fields=["is_active"], name="wallets_is_acti_3744ed_idx"),
        ),
        migrations.AddIndex(
            model_name="wallet",
            index=models.Index(
                fields=["is_enabled"], name="wallets_is_enab_640046_idx"
            ),
        ),
    ]
