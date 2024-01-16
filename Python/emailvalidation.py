# 1. atleast 5 chars in username
# 2. @ &  domain name must be in (gmail.com, yahoo.co.in, amazon.com)
# 3. username should not have special chars and should not start with numbers


def validating_email(mail_id):
    # user_name = mail_id.split('@')[0]
    # domain_name = mail_id.split('@')[1]
    [user_name,domain_name] = mail_id.split("@")
    if len(user_name) < 5:
        return False
    required_domain_names=['gmail.com','yahoo.co.in','amazon.com']
    if  domain_name not in required_domain_names:
        return False
    if not user_name.isalpha() and user_name[0].isdigit():
        return False
    return True

email_id=input("Enter your Email Id : ")
if validating_email(email_id):
    print(f"{email_id} is a valid email id")
else:
    print(f"{email_id} is not a valid email id")
    

