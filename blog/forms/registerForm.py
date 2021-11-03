from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Địa chỉ Email'
		}
	))

	username = forms.CharField(required=True, widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Tên đăng nhập'
		}
	))

	password1 = forms.CharField(required=True, widget=forms.PasswordInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Mật khẩu',
		}
	))

	password2 = forms.CharField(required=True, widget=forms.PasswordInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Nhập lại mật khẩu',
		}
	))

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(UserRegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.is_staff = True

		if commit:
			user.save()
		return user