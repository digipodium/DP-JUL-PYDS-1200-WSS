print("Register your details")
name = input("Enter ur username : ")
email = input("Enter ur Email : ")
password = input("Enter ur password : ")
cpassword = input("confirm password : ")
gender = input("enter ur gender (M/F/O) : ")

if len(name) > 4 and len(name) < 25:
    if '@' in email:
        if password == cpassword:
            print("You are registered ✅👑👑")
        else:
            print("❌ passwords do not match")
    else:
        print("❌ Email is invalid")
else:
    print('❌ username must be between 4 and 25 chars')