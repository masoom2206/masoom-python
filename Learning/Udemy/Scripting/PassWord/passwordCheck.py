# Check which password can be hack or not,
# in other word which password will be strong for you
# https://haveibeenpwned.com

import requests
import hashlib
import sys

# url = 'https://api.pwnedpasswords.com/range/' + 'masoom'
# url = 'https://api.pwnedpasswords.com/range/' + '68B75'# hash SHA1 key of "masoom" is "68B759512B0F0D6B9312BE6BADCE668E77F62648"
# url = 'https://api.pwnedpasswords.com/range/' + '3F3E8'
# url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
# res = requests.get(url)
# print(res)# <Response [400]> # No Error, But its not good required 200 here

def requestAPIData(queryChar):
  url = 'https://api.pwnedpasswords.com/range/' + queryChar
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f"Error fetching: {res.status_code}, check API.")
  return res

# def read_res(response):
#   print(response.text)

def getPasswordLeaksCount(hashes, hasgToCheck):
  hashList = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashList:
    # print(h, count)
    if h == hasgToCheck:
      return count
  return 0

def pwnedAPICheck(password):
  # print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5Char, tail = sha1password[:5], sha1password[5:]
  response = requestAPIData(first5Char)
  # print(first5Char, tail)
  # return read_res(response)
  return getPasswordLeaksCount(response, tail)

def main(args):
  for password in args:
    count = pwnedAPICheck(password)
    if count:
      print(f"{password} was found {count} times... You should probably change your password.")
    else:
      print(f"{password} was not found, carry on!")
  return 'Done'

# /opt/homebrew/bin/python3 /Users/masoom2206/coading/python/masoom-python/Learning/Udemy/Scripting/PassWord/passwordCheck.py hello masoom 123 Mas@allurion123
if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
# pwnedAPICheck('124')
