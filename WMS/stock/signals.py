from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from stock.models import Product, Tracker, UserProfile
from datetime import datetime

@receiver(post_save)
def update_model(sender, instance, created,**kwargs):
	date = datetime.now()
	user = Tracker.objects.last().user
	up = UserProfile.objects.filter(user=user)
	if created:
		instance.create_date= date
		if up:
			instance.create_user = up
		instance.save()
	# else:
	# 	instance.update_date= date
	# 	instance.update_user=up
	# instance.save()