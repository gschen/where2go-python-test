from werkzeug.security import generate_password_hash,check_password_hash
str1 = "abc"
str2 = generate_password_hash("abc")
str3 = generate_password_hash("cde")
def x(a,b):
    return check_password_hash(a,b)
if  x(str2,str1):
    print("x")
