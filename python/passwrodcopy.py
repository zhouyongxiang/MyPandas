import sys,pyperclip
pw = {"email":12345,"qq":11111}
if len(sys.argv)<2:
    print('Usage:python pw.py [account] - copy account password')
    sys.exit()
account= sys.argv[1]
print(account)
if account in pw:
    pyperclip.copy(pw[account])
    print('passwrd for'+ account + 'copiied to clipboard.')
else:
    print("no password")