#!/bin/python3
import random, sys

def main():
  
  print("====Password Generator====")
  print("==========================")
  print("")
  
  enterId()

def enterId():
  all = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=|\}]{[":;,<.>/?1234567890'
  lowerCase = 'abcdefghijklmnopqrstuvwxyz'
  upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  nums = '1234567890'
  specialChars = '`~!@#$%^&*()_-+=|\}]{[":;,<.>/?'
  set = ''  
    
  print("Enter the ID numbers of character types to include:\n\n    (Example: 134 -OR- 5)")
  print("    1. Lower case letters")
  print("    2. Upper case letters")
  print("    3. Numbers")
  print("    4. Special characters")
  print("    5. All of the above (recommended)")
    
  chars = input()
  
  count = 0
  for c in range(len(chars)):
    if chars[c] == '1':
      set += lowerCase
      count += 1
    if chars[c] == '2':
      set += upperCase
      count += 1
    if chars[c] == '3':
      set += nums
      count += 1
    if chars[c] == '4':
      set += specialChars
      count += 1
    if chars[c] == '5':
      set = all
      count += 1
  if count < 1:
    print('Invalid choice. Please use integers 1-5.\n')
    enterId()

  numPw = input("Enter the amount of passwords you wish to create:")
  numPw = int(numPw)
  
  lenPw = input("Enter the desired length of each password:")
  lenPw = int(lenPw)
  print('')
  
  password = ''
  
  z = 0
  
  for x in range(numPw):
    for y in range(lenPw):
      password += random.choice(set)
    z += 1
    print(z,":",password)
    password = ''
      
  runAgain = input('\nRun again? Y or N:')
  print("")
  if runAgain == 'Y' or runAgain == 'y':
    main()
  else:
    sys.exit()

main()