from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.forms import UserLoginForm


def login(request):
    if request.method == 'GET':
        # 返回登录页面
        return render(request, 'login.html')

    if request.method == 'POST':
        # 获取所有的请求数据
        data = request.POST
        # 将数据交给form表单验证
        form = UserLoginForm(data)

        if form.is_valid():
            # 如果验证通过就将数据保存到数据库
            user = auth.authenticate(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
            if not user:
                # 没有user对象，表示验证密码不通过
                return render(request, 'login.html')
            # 实现登录，request.user等于登录系统用户对象
            auth.login(request, user)
            return HttpResponseRedirect(reverse('user:index'))

        else:
            # 验证失败返回错误信息
            errors = form.errors
            return render(request, 'login.html', {'errors': errors})


@login_required
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    if request.method == 'POST':
        return render(request, 'index.html')
