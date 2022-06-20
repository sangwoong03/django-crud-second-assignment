import re

from django.core.exceptions import ValidationError

def validate_email(value) :
    EMAIL_CHECK =  "^[a-zA-Z0-9+_.]+@[a-zA-Z0-9-.]+$"

    if not re.match(EMAIL_CHECK, value) :
        raise ValidationError("INVALID_EMAIL")

def validate_password(value) :
    PW_CHECK =  "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$"

    if not re.match(PW_CHECK, value) :
        raise ValidationError("INVALID_PASSWORD")