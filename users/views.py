from django.shortcuts import render

# Create your views here.
import json, re

from django.http import JsonResponse
from django.views import View

from users.models import User

class SignUpView(View) :

  def post(self, request) :
     
    try :
      data  = json.loads(request.body)
      email = data["email"]
      pw    = data["password"]
      
      EMAIL_CHECK = "^[a-zA-Z0-9+_.]+@[a-zA-Z0-9-.]+$"
      PW_CHECK    = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$"
      
      # 이메일 중복 확인
      if User.objects.filter(email = email).exists() :
        return JsonResponse({"Message" : "THIS_EMAIL_ALEADY_EXIST"}, status = 400)

      # 이메일에 "@" "." 여부 확인
      if not re.match(EMAIL_CHECK, email) :
        return JsonResponse({"Message": "INVALID EMAIL"}, status=401)

      # 비밀번호가 8자리 이상의 문자, 숫자, 특수문자 포함 확인
      if not re.match(PW_CHECK, pw) :
        return JsonResponse({"Message": "INVALID PASSWORD"}, status=401)

      User.objects.create(
        last_name     = data["last_name"],
        first_name    = data["first_name"],
        account       = data["account"],
        phone_number  = data["phone_number"],
        date_of_birth = data["date_of_birth"],
        email         = email,
        password      = pw
      )
      
      return JsonResponse({"Message": "SUCCESS"}, status=201)

    except KeyError:
      return JsonResponse({"Message": "KEY_ERROR"}, status=400)
      
