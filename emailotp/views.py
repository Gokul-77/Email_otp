from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import EmailOTPModule

otp_module = EmailOTPModule()

@api_view(['POST'])
def send_otp(request):
    email = request.data.get('email')
    status = otp_module.generate_OTP_email(email)
    return Response({'status': status})
@api_view(['POST'])
def verify_otp(request):
    email = request.data.get('email')
    otp = request.data.get('otp')
    
    # ✅ Don't pass 'request', pass email and otp only!
    status = otp_module.check_otp_http(email, otp)
    
    return Response({'status': status})
