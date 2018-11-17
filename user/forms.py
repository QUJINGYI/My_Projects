from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=2, required=True,
                               error_messages={
                                   'max_length': '账号最长10',
                                   'min_length': '账号最短2',
                                   'required': '账号必填',
                               })
    password = forms.CharField(max_length=18, min_length=6, required=True,
                               error_messages={
                                   'max_length': '密码最长18',
                                   'min_length': '账号最短6',
                                   'required': '密码必填',
                               })

    def clean(self):
        # 使用django自带的User
        user = User.objects.filter(username=self.cleaned_data.get('username'))
        if not user:
            raise forms.ValidationError({'username': '该账号没有注册无法登录，请去注册'})

        # pw = User.objects.filter(self.cleaned_data.get('password'))
        #
        # if self.password != pw:
        #     raise forms.ValidationError({'password': '密码不正确'})

        return self.cleaned_data







