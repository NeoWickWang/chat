from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth import authenticate, login

from .models import Account
from .forms import AccountLoginForm, AccountLogonForm

from django.contrib.auth.hashers import make_password
from django.db.models import Q


 
def index(request):
    return render(request, "chat/selectRoom.html")  # choose room
    # return render(request, "chat/login.html")

def room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})

def log_in(request):
    # return HttpResponse('登录成功')
    if request.method == 'POST':
        user_login_form = AccountLoginForm(request.POST)

        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']
            hashed_password = make_password(password)

            user = user_login_form.save(commit=False)
            user.username = username
            user.password = hashed_password
            # user.save()

            # usernames = Account.objects.values('username')
            account = Account.objects.get(username=username)
            if account:
                if account.password == user.password:
                    user.login = 1
                    user.save()
                    return redirect("chat:room")
                else:
                    error_message = "密码错误，请重新输入！"
                    return render(request, "error/notLoginError.html", {'error_message': error_message})

            else:
                error_message = "用户名不存在，请注册！"
                return render(request, "error/notLoginError.html", {'error_message': error_message})

            # 用户验证
            # authenticated_user = authenticate(username=username, password=password)

            # if authenticated_user is not None:
            #     # 验证通过，执行登录
            #     login(request, user)
            #     return redirect("chat:room")

        else:
            error_message = "帐号密码错误，请重新输入~"
            return render(request, "error/notLoginError.html", {'error_message': error_message})
    
    elif request.method == 'GET':
        user_login_form = AccountLoginForm()
        context = {'form': user_login_form}
        return render(request, 'chat/login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")
    
def checkLogin(request, account):
    if account.login != 1:
        error_message = "未登录！"
        return render(request, "error/notLoginError.html", {'error_message': error_message})
    else:
        return True
    

def logon(request):
    # return HttpResponse('注册页面')
    if request.method == 'POST':
        user_register_form = AccountLogonForm(request.POST)

        if user_register_form.is_valid():
            username = user_register_form.cleaned_data['username']
            password = user_register_form.cleaned_data['password']
            hashed_password = make_password(password)

            user = user_register_form.save(commit=False)
            user.username = username
            user.password = hashed_password
            # user.login = 0

            account = Account.objects.get(username=username)

            if account:
                error_message = "用户名已存在，请重新注册！"
                return render(request, "error/notLoginError.html", {'error_message': error_message})

            else:
                user.save()
                return redirect("chat:login")
        else:
            error_message = "注册输入有误。请重新输入~"
            return render(request, "error/notLoginError.html", {'error_message': error_message})

    elif request.method == 'GET':
        user_register_form = AccountLogonForm()
        context = { 'form': user_register_form }
        return render(request, 'chat/register.html', context)
    else:
        error_message = "请使用GET或POST请求数据"
        return render(request, "error/notLoginError.html", {'error_message': error_message})


def logout(request):
    return HttpResponse('退出')

# def index(request):
#     return HttpResponse('主页面')

def error(request):
    return render(request, 'error/printError.html')