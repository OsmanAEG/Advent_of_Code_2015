# reading the input
with open('input.txt') as f:
  directions = f.readlines()[0]

# function to calculate the step to take
def step_taken(step, coordinates):
  if step   == '>': coordinates[0] += 1
  elif step == '<': coordinates[0] -= 1
  elif step == '^': coordinates[1] += 1
  else:             coordinates[1] -= 1

  return coordinates

# Part 1 ------------------------
def part1():
  # house coordinates
  coordinates = [0, 0]

  # number of presents per house
  present_dict = {}

  present_dict['[0, 0]'] = 1

  for step in directions:
    coordinates = step_taken(step, coordinates)
    coord = str(coordinates)

    if coord in present_dict.keys(): present_dict[coord] += 1
    else: present_dict[coord] = 1

  print('The amount of houses that received at least one present is ' + str(len(present_dict)) + '!')

# Part 2 ------------------------
def part2():
  santa_coordinates = [0, 0]
  robot_coordinates = [0, 0]

  # number of presents per house
  present_dict = {}

  present_dict['[0, 0]'] = 2

  direction_list = list(directions)

  for i in range(0, len(direction_list), 2):
    step_santa = direction_list[i]
    step_robot = direction_list[i+1]

    santa_coordinates = step_taken(step_santa, santa_coordinates)
    robot_coordinates = step_taken(step_robot, robot_coordinates)

    santa_coord = str(santa_coordinates)
    robot_coord = str(robot_coordinates)

    if santa_coord in present_dict.keys(): present_dict[santa_coord] += 1
    else: present_dict[santa_coord] = 1

    if robot_coord in present_dict.keys(): present_dict[robot_coord] += 1
    else: present_dict[robot_coord] = 1

  print('The amount of houses that received at least one present is ' + str(len(present_dict)) + '!')

part1()
part2()






