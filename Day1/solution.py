# finding santas floor
def final_floor(steps):
  floor = 0
  position = 0
  first_base_entry = False
  first_base_position = 0

  for step in steps:
    position += 1
    if step == '(': floor += 1
    else: floor -= 1

    if floor == -1 and first_base_entry == False:
      first_base_position = position
      first_base_entry = True

  return floor, first_base_position

# reading the input
with open('input.txt') as f:
  steps = f.readlines()[0]

# getting santas floor
floor, first_base_position = final_floor(steps)
print('Santa must deliver the present to floor ' + str(floor) + '!')
print('Position ' + str(first_base_position) + ' causes Santa to enter the basement!')