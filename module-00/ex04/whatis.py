import sys as s

if (len(s.argv) != 2):
  print("AssertionError: more than one argument is provided")
elif (not s.argv[1].lstrip('-').isdigit()):
  print("AssertionError: argument is not an integer")
else:
  text = 'I\'m Even.' if int(s.argv[1]) % 2 == 0 else 'I\'m Odd.'
  print(f"{text}")