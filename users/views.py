import json
import bcrypt
import jwt

from django.http import JsonResponse
from django.views import View

from users.models import User
from users.validations import validate_email, validate_password
from assignment_2nd.settings import ALGORITHM, SECRET_KEY

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

        validate_email(email)
        validate_password(password)
       
        # 이메일 중복 확인
        if User.objects.filter(email = email).exists() :
            return JsonResponse({"message" : "THIS_EMAIL_ALEADY_EXIST"}, status = 400)

        encoded_password = password.encode("utf-8") # 문자열 > 바이트 인코딩
        secret_password  = bcrypt.hashpw(encoded_password, bcrypt.gensalt()) # 해싱
        decoded_password = secret_password.decode("utf-8") # 해싱 > 문자열 디코딩 후 저장
 
        User.objects.create(
            last_name     = last_name,  
            first_name    = first_name,   
            account       = account,      
            phone_number  = phone_number, 
            date_of_birth = date_of_birth,
            email         = email,
            password      = decoded_password
        )
        
        return JsonResponse({"message": "SUCCESS"}, status=201)

    except KeyError:
      return JsonResponse({"message": "KEY_ERROR"}, status=400)
      
class LoginView(View):
    def post(self, request):
        try:
            data              = json.loads(request.body)
            user_account      = data["account"]
            user_password     = data["password"]
            
            user              = User.objects.get(account = user_account)
            hashed_password   = user_password.encode("utf-8") # 받은 비밀번호 인코딩
            saved_password    = user.password.encode("utf-8") # 저장된 비밀번호 꺼내오기
            
            if not bcrypt.checkpw(hashed_password, saved_password) : # 받은 비밀번호 인코딩 = 저장된 비밀번호 인코딩
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            access_token = jwt.encode({"user_id" : user.id }, SECRET_KEY, ALGORITHM)           

            return JsonResponse({"access_token" : access_token}, status=200)            

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status=400)