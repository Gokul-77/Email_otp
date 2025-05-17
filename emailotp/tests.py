from django.test import TestCase
from .utils import EmailOTPModule, STATUS_EMAIL_INVALID, STATUS_EMAIL_OK, STATUS_OTP_OK
from unittest.mock import patch, MagicMock


class MockInputStream:
    def __init__(self, otps):
        self.otps = otps
        self.index = 0

    def readOTP(self):
        otp = self.otps[self.index]
        self.index += 1
        return otp

class EmailOTPTestCase(TestCase):

    def setUp(self):
        self.module = EmailOTPModule()

    @patch('emailotp.utils.send_mail')
    def test_generate_valid_email(self, mock_send_mail):
        result = self.module.generate_OTP_email("test@gmail.com")
        self.assertEqual(result, STATUS_EMAIL_OK)

    def test_invalid_email(self):
        result = self.module.generate_OTP_email("notvalid@outlook.com")
        self.assertEqual(result, STATUS_EMAIL_INVALID)

    def test_check_otp_success(self):
        module = EmailOTPModule()

    # Create a real OTP entry in the database
        from .models import EmailOTP
        EmailOTP.objects.create(email="example@gmail.com", otp="123456")

        class MockInputStream:
            def __init__(self, inputs):
                self.inputs = inputs
                self.index = 0

            def readOTP(self):
                if self.index < len(self.inputs):
                    otp = self.inputs[self.index]
                    self.index += 1
                    return otp
                return "000000"

        mock_input = MockInputStream(["123456"])
        
        
        result = module.check_OTP(mock_input, "example@gmail.com")
        self.assertEqual(result, STATUS_OTP_OK)
