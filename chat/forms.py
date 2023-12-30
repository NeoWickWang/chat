from django import forms
from .models import Account

class AccountLoginForm(forms.ModelForm):
    class Meta:
        model = Account

        fields = ('username', 'password', 'login')

class AccountLogonForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()
    
    class Meta:
        model = Account

        fields = ('username', 'password')

    # 对两次输入的密码是否一致进行检查
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密码输入不一致,请重试。")