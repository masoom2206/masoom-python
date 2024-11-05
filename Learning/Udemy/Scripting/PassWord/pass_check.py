# Check password with API
import requests
import hashlib
import sys

def passCheck(args):
  for password in args:
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5Char, tail = sha1password[:5], sha1password[5:]
    url = 'https://api.pwnedpasswords.com/range/' + first5Char
    res = requests.get(url)
    hashList = (line.split(':') for line in res.text.splitlines())
    count = 0
    for h, c in hashList:
      # print(h, count)
      if h == tail:
        count = c
    if count:
      print(f"{password} was found {count} times... You should probably change your password.")
    else:
      print(f"{password} was not found, carry on!")
  return 'Done'

if __name__ == '__main__':
  sys.exit(passCheck(sys.argv[1:]))

# /opt/homebrew/bin/python3 /Users/masoom2206/coading/python/masoom-python/Learning/Udemy/Scripting/PassWord/pass_check.py hello masoom 123 Mas@allurion123