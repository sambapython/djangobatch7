from django import forms
from stock.models import UserProfile, StockOperations, Product
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		#fields = "__all__"
		fields = ["address",'phone','role']
class UserProfileFormAll(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = "__all__"
		#fields = ["address",'phone','role']	
class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = "__all__"

class StockOperationForm(forms.ModelForm):
	class Meta:
		model = StockOperations
		#fields = "__all__"
		exclude=['update_date','delete_date','update_user','delete_user']

