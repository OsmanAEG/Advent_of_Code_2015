# constants

bitmax = 65535

# loading in the instructions booklet
def loading_instructions():
  instructions = {}
  signals = {}
  wires = []
  # loading in santas list of instructions
  with open('input.txt') as f:
    for line in f:
      line = line.strip('\n')
      split = line.split(' ')
      wires.append(split[-1])
      N = len(split)
      depends_on = []

      if N == 3:
        if not split[0].isnumeric(): depends_on.append(split[0])
        instructions[split[-1]] = {'Entries': [split[0]],
                                   'Dependencies': depends_on,
                                   'Logic': 'None',
                                   'N': 3,
                                   'Value': 0}
      elif N == 4:
        if not split[1].isnumeric(): depends_on.append(split[1])
        instructions[split[-1]] = {'Entries': [split[1]],
                                   'Dependencies': depends_on,
                                   'Logic': split[0],
                                   'N': 4,
                                   'Value': 0}
      elif N == 5 and split[1] == 'LSHIFT' or split[1] == 'RSHIFT':
        if not split[0].isnumeric(): depends_on.append(split[0])
        if not split[2].isnumeric(): depends_on.append(split[2])
        instructions[split[-1]] = {'Entries': [split[0], split[2]],
                                   'Dependencies': depends_on,
                                   'Logic': split[1],
                                   'N': 5,
                                   'Value': 0}
      else:
        if not split[0].isnumeric(): depends_on.append(split[0])
        if not split[2].isnumeric(): depends_on.append(split[2])
        instructions[split[-1]] = {'Entries': [split[0], split[2]],
                                   'Dependencies': depends_on,
                                   'Logic': split[1],
                                   'N': 5,
                                   'Value': 0}

      signals[split[-1]] = depends_on

  return instructions, signals, wires

# sorting the instructions
def topological_sorter(current, checked, stack):
  # checking the current wire
  checked.append(current)

  # if the current dependency has not been checked - check it
  for i in signals[current]:
    if i not in checked:
      topological_sorter(i, checked, stack)

  # appending the current wire
  stack.append(current)

instructions, signals, wires = loading_instructions()
checked = []
stack = []

# topological sort
for i in wires:
  if i not in checked:
    topological_sorter(i, checked, stack)

def calculating_signals():
  # running through the circuit information
  for sorted in stack:
    instruction  = instructions[sorted]
    entries      = instruction['Entries']
    logic        = instruction['Logic']
    n            = instruction['N']

    signal = []

    for entry in entries:
      if entry.isnumeric(): signal.append(int(entry))
      else: signal.append(instructions[entry]['Value'])

    if   n == 3: instruction['Value'] = int(signal[0])
    elif n == 4: instruction['Value'] = bitmax - int(instructions[entries[0]]['Value'])
    else:
      value_1 = 0
      value_2 = 0

      if entries[0].isnumeric():
        value_1 = int(entries[0])
      else:
        value_1 = int(instructions[entries[0]]['Value'])

      if entries[1].isnumeric():
        value_2 = int(entries[1])
      else:
        value_2 = int(instructions[entries[1]]['Value'])

      if    logic == 'AND':    instruction['Value'] = value_1 & value_2
      elif  logic == 'OR':     instruction['Value'] = value_1 | value_2
      elif  logic == 'LSHIFT': instruction['Value'] = value_1 << value_2
      else:                    instruction['Value'] = value_1 >> value_2

calculating_signals()

# checking a value (answer for part 1)
a_val_old = instructions['a']['Value']
print(a_val_old)

# getting new a value with adjusted b signal
for i in stack:
  instructions[i]['Value'] = 0

instructions['b']['Entries'] = [str(a_val_old)]

calculating_signals()

# checking a value (answer for part 2)
a_val_new = instructions['a']['Value']
print(a_val_new)