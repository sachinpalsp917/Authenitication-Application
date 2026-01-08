from aiosmtplib import send
from email.message import EmailMessage
from core.config import settings

class EmailService:
    @staticmethod
    async def send_mail(to_email: str, subject: str, body: str):
        message = EmailMessage()
        message['From'] = settings.MAIL_FROM
        message['To'] = to_email
        message['Subject'] = subject
        message.set_content(body)

        try:
            await send(
                message,
                hostname=settings.MAIL_SERVER,
                port=settings.MAIL_PORT,
                username=settings.MAIL_USERNAME or None,
                password=settings.MAIL_PASSWORD or None,
                use_tls=False
            )
            print(f"Email sent to {to_email}")
        except Exception as e:
            print(f"Failed to send email: {e}")
        
    @staticmethod
    async def send_verification_email(to_email: str, code: str):
        subject = "Verify your email"
        body = f"""
        Hello,
        
        Please verify your email address by entering the following code:
        
        {code}
        
        This code expires in 15 minutes.
        """
        await EmailService.send_mail(to_email, subject, body)

    @staticmethod
    async def send_password_reset_email(to_email: str, code: str):
        subject = "Reset your password"
        body = f"""
        Hello,
        
        You requested a password reset. Use the code below to proceed:
        
        {code}
        
        If you did not request this, please ignore this email.
        """
        await EmailService.send_mail(to_email, subject, body)