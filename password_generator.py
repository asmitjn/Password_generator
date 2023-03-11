from random_password_creator import Password
import argparse

args=argparse.ArgumentParser()
args.add_argument('-c','--charset',required=True)
args.add_argument('-l','--length',default=8)

# args.add_argument('charset')
# args.add_argument('length',default=8)

options=args.parse_args()
print(options.charset)
print(options.length)

password=Password(options.charset,int(options.length))
password.set_the_charset()
password.generate_password()
print('The random password is:',password.get_password())

# l=lowercase
# u=uppercase
# d=digits
# s=special chars
# Argsparse is used to take command-line arguments