# Generated by Django 2.1.1 on 2018-09-21 16:12

from django.db import migrations
from django.db.models import Q


def migrate_preferred_address_to_wallet(apps, schema_editor):
    Profile = apps.get_model('dashboard', 'Profile')
    Wallet = apps.get_model('economy', 'Wallet')
    profiles = Profile.objects.all()

    for profile in profiles:
        pref_address = getattr(profile, 'preferred_payout_address', '')
        if pref_address:
            try:
                existing_wallet = Wallet.objects.get(address=pref_address)
                existing_wallet.wallet_users.add(profile)
            except Wallet.DoesNotExist:
                try:
                    Wallet.objects.create(profile=profile, address=pref_address, is_default=True)
                except Exception as e:
                    print(f'Exception in economy migration 0007 - Exception: ({e}) - Profile: {profile}')


class Migration(migrations.Migration):

    dependencies = [
        ('economy', '0006_wallet'),
    ]

    operations = [migrations.RunPython(migrate_preferred_address_to_wallet), ]