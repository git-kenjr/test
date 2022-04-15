# import email.message
# import smtplib
# msg = email.message.EmailMessage() #建立物件
# msg["From"]='寄件人帳號@gmail.com' #寄件人
# msg["To"]='收件人帳號@gmail.com'   #收件人
#  ["Subject"]="安安你好"           #主題
# msg.set_content("測試看看")         #純文字內容
# #寄送html 格式內容  subtype告知寫入的形態
# # msg.add_alternative("<h3>優惠券</h3>滿五百送一百",subtype='html')
# server=smtplib.SMTP_SSL("smtp.gmail.com",465) #(SSL驗證)
# server.login("寄件人帳號","應用程式密碼")
# server.send_message(msg)
# server.close()

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# content = MIMEMultipart()  #建立MIMEMultipart物件
# content["subject"] = "Learn Code With Mike"  #郵件標題
# content["from"] = "pydemo123@gmail.com"  #寄件者
# content["to"] = "example@gmail.com" #收件者
# content.attach(MIMEText("Demo python send email"))  #郵件內容
# with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器 (TLS驗證)
#     try:
#         smtp.ehlo()  # 必須呼叫的函式 向郵件主機註冊身份(驗證SMTP伺服器)
#         smtp.starttls()  # 建立加密傳輸
#         smtp.login("寄件人@gmail.com", "ymxrcasvlbwfvape")  # 登入寄件者gmail
#         smtp.send_message(content)  # 寄送郵件
#         print("Complete!")
#     except Exception as e:
#         print("Error message: ", e)



# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from pathlib import Path
# content = MIMEMultipart()  # 建立MIMEMultipart物件
# content["subject"] = "python"  # 郵件標題
# content["from"] = "寄件人帳號@gmail.com"  # 寄件者
# content["to"] = "寄件人帳號@gmail.com"  # 收件者
# content.attach(MIMEText("Demo python send email"))  # 郵件純文字內容
# content.attach(MIMEImage(Path("狗狗5411953.jpg").read_bytes()))  # 郵件圖片內容
# import smtplib
# with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
#     try:
#         smtp.ehlo()  # 驗證SMTP伺服器
#         smtp.starttls()  # 建立加密傳輸
#         smtp.login("寄件人帳號@gmail.com", "應用程式密碼")  # 登入寄件者gmail
#         smtp.send_message(content)  # 寄送郵件
#         print("Complete!")
#     except Exception as e:
#         print("Error message: ", e)



