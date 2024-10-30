# Variable and data type
a1=int(input("Enter 1st no . = "))
a2=int(input("Enter 2nd no . = "))
a3=int(input("Enter 3rd no . = "))
a4=int(input("Enter 4th no . = "))

if(a1>a2 and a1>a3 and a1>a4):
  print("1st no. is largest")
  print("1st no.")
elif(a2>a3 and a2>a4):
  print("2nd no. is largest")
  print("2nd no.")
elif(a3>a4):
  print("3rd no. is largest")
  print("3rd no.")
else:
  print("4th no. is largest")
  print("4th no.3")