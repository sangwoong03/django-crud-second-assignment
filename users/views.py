import json
import re
import bcrypt
import jwt

from django.http import JsonResponse
from django.views import View

from users.models import User
from my_settings import ALGORITHM, SECRET_KEY

class SignUpView(View) :
  def post(self, request) :
    try :
        data          =  json.loads(request.body)
        email         = data["email"]
        last_name     = data["last_name"]
        first_name    = data["first_name"]
        account       = data["account"]
        phone_number  = data["phone_number"]
        date_of_birth = data["date_of_birth"]
        password      = data["password"]

        encoded_password = password.encode("utf-8") # 문자열 > 바이트 인코딩
        secret_password  = bcrypt.hashpw(encoded_password, bcrypt.gensalt()) # 해싱
        decoded_password = secret_password.decode("utf-8") # 해싱 > 문자열 디코딩 후 저장

        EMAIL_CHECK = "^[a-zA-Z0-9+_.]+@[a-zA-Z0-9-.]+$"
        PW_CHECK    = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$"
        
        # 이메일 중복 확인
        if User.objects.filter(email = email).exists() :
            return JsonResponse({"Message" : "THIS_EMAIL_ALEADY_EXIST"}, status = 400)

        # 이메일에 "@" "." 여부 확인
        if not re.match(EMAIL_CHECK, email) :
            return JsonResponse({"Message": "INVALID EMAIL"}, status=401)

        # 비밀번호가 8자리 이상의 문자, 숫자, 특수문자 포함 확인
        if not re.match(PW_CHECK, password) :
            return JsonResponse({"Message": "INVALID PASSWORD"}, status=401)

        User.objects.create(
            last_name     = last_name,  
            first_name    = first_name,   
            account       = account,      
            phone_number  = phone_number, 
            date_of_birth = date_of_birth,
            email         = email,
            password      = decoded_password
        )
        
        return JsonResponse({"Message": "SUCCESS"}, status=201)

    except KeyError:
      return JsonResponse({"Message": "KEY_ERROR"}, status=400)
      
class LoginView(View):
    def post(self, request):
        try:
            data              = json.loads(request.body)
            user_account      = data["account"]
            user_password     = data["password"]
            user_id           = User.objects.get(account = user_account).id

            hashed_password   = user_password.encode("utf-8") # 받은 비밀번호 인코딩
            saved_password    = User.objects.get(account = user_account).password # 저장된 비밀번호 꺼내오기
            
            BLANK_CHECK       = "^$"
            is_account_blank  = re.match(BLANK_CHECK, user_account)
            is_password_blank = re.match(BLANK_CHECK, user_password)

            if is_account_blank or is_password_blank :
                return JsonResponse({"Message": "CHECK_BLANK"}, status=401)
            
            if not User.objects.filter(account = user_account).exists() :
                return JsonResponse({"Message": "INVALID_USER"}, status=401)
            
            if not bcrypt.checkpw(hashed_password, saved_password.encode("utf-8")) : # 받은 비밀번호 인코딩 = 저장된 비밀번호 인코딩
                return JsonResponse({"Message": "INVALID_USER"}, status=401)

            access_token = jwt.encode({"user_id" : user_id }, SECRET_KEY, ALGORITHM)           

            return JsonResponse({"ACCESS_TOKEN" : access_token}, status=200)            

        except KeyError:
            return JsonResponse({"Message" : "KEY_ERROR"}, status=400)