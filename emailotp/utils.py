import random
import re
from django.core.mail import send_mail
from .models import EmailOTP
from django.utils import timezone

EMAIL_REGEX = r"^[\w\.-]+@gmail\.com$"

STATUS_EMAIL_OK = "STATUS_EMAIL_OK"
STATUS_EMAIL_FAIL = "STATUS_EMAIL_FAIL"
STATUS_EMAIL_INVALID = "STATUS_EMAIL_INVALID"

STATUS_OTP_OK = "STATUS_OTP_OK"
STATUS_OTP_FAIL = "STATUS_OTP_FAIL"
STATUS_OTP_TIMEOUT = "STATUS_OTP_TIMEOUT"

class EmailOTPModule:

    def generate_OTP_email(self, user_email):
        try:
            if not re.match(EMAIL_REGEX, user_email):
                return STATUS_EMAIL_INVALID

            otp = str(random.randint(100000, 999999))
            email_body = f"Your OTP Code is {otp}. The code is valid for 1 minute"

            send_mail(
                'Your OTP Code',
                email_body,
                'no-reply@example.com',
                [user_email],
                fail_silently=False
            )

            EmailOTP.objects.create(email=user_email, otp=otp)
            return STATUS_EMAIL_OK

        except Exception as e:
            print("Error:", e)
            return STATUS_EMAIL_FAIL

    def check_otp_http(self, email, otp):
        try:
            otp_obj = EmailOTP.objects.filter(email=email).order_by('-created_at').first()
            if not otp_obj:
                return STATUS_OTP_FAIL
            if otp_obj.is_expired():
                return STATUS_OTP_TIMEOUT
            if otp_obj.otp != otp:
                return STATUS_OTP_FAIL
            return STATUS_OTP_OK
        except Exception as e:
            print("OTP verification error:", e)
            return STATUS_OTP_FAIL
