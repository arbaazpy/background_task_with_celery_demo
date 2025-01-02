from celery import shared_task
from .models import UserProfile
import time

@shared_task
def update_full_name(user_profile_id, sleep_for=None):
    if sleep_for is not None:
        time.sleep(sleep_for)
    try:
        user_profile = UserProfile.objects.get(id=user_profile_id)
        user_profile.full_name = f"{user_profile.first_name} {user_profile.last_name}"
        user_profile.save()
    except UserProfile.DoesNotExist:
        pass  # Handle the case where the user profile does not exist
