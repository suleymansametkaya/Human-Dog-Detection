import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Mail bilgilerini ayarla
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "sender@gmail.com" # Mail gonderen e-posta adresi 
sender_password = "2 Factor Authentication Password" # Mail gonderen e-posta sifresi

""" 
2 Factor Authentication Password:
Bu link uzerinden 2 Factor Authentication Password olusturabilirsiniz.
https://myaccount.google.com/apppasswords
"""

# E-posta gonderme fonksiyonu
def send_email(subject, body,receiver_email):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Sunucuya baglanir ve e-postayi gonderir
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Mail başarıyla gönderildi.")
    except Exception as e:
        print(f"Mail gönderme hatası: {e}")
