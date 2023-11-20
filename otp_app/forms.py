# # from django import forms

# # class UserInfoForm(forms.Form):
# #     first_name = forms.CharField(max_length=100)
# #     last_name = forms.CharField(max_length=100)
# #     email = forms.EmailField()
# #     age = forms.IntegerField(min_value=1)

from django import forms

class otpform(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()