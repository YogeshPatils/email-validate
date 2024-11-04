def validate_email(s):
    email_domains=("com", "org", "net", "edu", "gov", "info", "biz", "me", "io", "co", "us", "uk", "ca", "in",
    "edu.in", "co.uk", "ac.in", "gov.in", "org.in", "net.in", "com.au", "co.in", "gov.uk", 
    "co.za", "com.sg", "co.jp", "com.cn", "co.kr", "ac.uk", "com.ph", "com.br")
    splitted_email=s.split('@')
    if s[0].isalpha() and len(splitted_email)==2  and bool(splitted_email[1])==True: #checking wheather given email has only @, first letter is capital, and edge case when no extension afetr @
        for i in splitted_email[0]:
            if i.isalpha() or i.isalnum() or i in ('.','_','-'): #email username can contain '.','-','_' and alphabets
                pass
            else:
                return False
        for i in splitted_email[1].split('.')[0]:  # checking second half of email format i.e extension.domain
            if not(i.isalpha()):
                return False    
        if splitted_email[1].split('.')[-1] not in email_domains:
            return False
    else:
        return False
    return True
print(validate_email('YOUR INPUT'))                    #enter your input here
'''
USE THIS FOR MULTI LINE INPUT WITH FORMAT
user-1 <username@exension.domain>
user-2 <username@exension.domain>
    .
    .
    .
user-n <username@exension.domain>

input_emails = [input().strip() for _ in range(int(input().strip()))]
n=len(input_emails)
j=0
q=0
while j<n: #[1,2,3,4,5,6]
    if not(validate_email(input_emails[j].split()[1][1:-1])):#calling function by passing each email by one by one and validating the email
        input_emails.pop(j-q) #here i am considering email is enclosed between <>
        q+=1
    j+=1
print('\n'.join(input_emails))
'''
