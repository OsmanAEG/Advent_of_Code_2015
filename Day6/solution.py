import numpy as np

# grid dimensions
m = 1000
n = 1000

# loading in santas list of instructions
def loading_instructions():
  instructions = []
  # loading in santas list of instructions
  with open('input.txt') as f:
    for line in f:
      line = line.strip('\n')
      line = line.replace('turn ', '')
      split = line.split(' ')

      # getting switch state
      state = split[0]

      # coordinate range
      start = list(map(int, split[1].split(',')))
      end = list(map(int, split[3].split(',')))

      instructions.append([state, start, end])

  return instructions

def part1(instructions):
  lights = np.full((m, n), -1, dtype= int) # lights start off

  # going through Santas instructions
  for instruction in instructions:
    state = instruction[0]
    start = instruction[1]
    end = instruction[2]

    for i in range(start[0], end[0] + 1):
      for j in range(start[1], end[1] + 1):
        if state == 'on': lights[i][j] = 1
        elif state == 'off': lights[i][j] = -1
        else: lights[i][j] *= -1

  num_lit = np.count_nonzero(lights == 1)
  print('As per Santas original instructions, ' + str(num_lit) + ' lights are lit!')

def part2(instructions):
  lights = np.zeros((m, n), dtype= int) # lights start at 0 brightness

  # going through Santas instructions
  for instruction in instructions:
    state = instruction[0]
    start = instruction[1]
    end = instruction[2]

    for i in range(start[0], end[0] + 1):
      for j in range(start[1], end[1] + 1):
        if state == 'on': lights[i][j] += 1
        if state == 'off' and lights[i][j] > 0: lights[i][j] -= 1
        if state == 'toggle': lights[i][j] += 2

  total_brightness = np.sum(lights)

  print('As per Santas new instructions, the total brightness is ' + str(total_brightness) + '!')

instructions = loading_instructions()
part1(instructions)
part2(instructions)