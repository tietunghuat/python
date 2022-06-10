# 發送郵件
# #googleaccount>security>lesssecure
# import email.message 
# msg=email.message.EmailMessage()
# msg["From"]="tunghuat.2000@gmail.com"
# msg["To"]="tunghuat.2000@gmail.com"
# msg["Subject"]="Python Training"
# msg.send_content("Python testing123") #純文字類型
# msg.add_alternative("<h3 style='color:red;'>優惠券</h3>")#多樣化的內用

# import stmplib as lib
# #到網路上搜狐尋gmail stmp server 鏈接port
# server=lib.SMTP_SSL("smtp.gmail.com",587) #gmail主機的名稱
# server.login("email","password")
# server.send_message(msg)
# server.close()