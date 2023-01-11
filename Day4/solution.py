import hashlib

n = 5
i = 0
answer1 = 0
answer2 = 0

# reading the input string
with open('input.txt') as f:
  secret_key = f.readlines()[0]

while True:
  i += 1
  md5_input = secret_key + str(i)
  md5hash = hashlib.md5(md5_input.encode())
  md5_output = md5hash.hexdigest()
  if answer1 == 0 and md5_output[0:5] == '00000':  answer1 = i
  if answer2 == 0 and md5_output[0:6] == '000000': answer2 = i
  if answer1 != 0 and answer2 != 0: break

print('Santas First Answer is: ' + str(answer1) + '!')
print('Santas Second Answer is: ' + str(answer2) + '!')

