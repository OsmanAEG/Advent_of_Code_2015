# part 1
def part1():
  num_nice = 0 # number of nice strings

  vowels = ['a', 'e', 'i', 'o', 'u']
  bad_strings = ['ab', 'cd', 'pq', 'xy']

  # loading in santas list and checking for nice strings
  with open('input.txt') as f:
    for line in f:
      double_letter = False
      bad_string = False

      vowel_count = 0

      # checking for number of vowels
      for i in range(len(line)):
        if line[i] in vowels: vowel_count += 1

      # checking for double letters and bad strings
      for i in range(len(line) - 1):
          if line[i] == line[i + 1]: double_letter = True
          if line[i] + line[i+1] in bad_strings: bad_string = True

      if vowel_count >= 3 and double_letter == True and bad_string == False:
        num_nice += 1

  print('There are ' + str(num_nice) + ' nice strings in Santas first model!')

# part 2
def part2():
  num_nice = 0 # number of nice strings

  # loading in santas list and checking for nice strings
  with open('input.txt') as f:
    for line in f:

      double_pair = False
      double_letter = False

      # checking for double letters and bad strings
      N = len(line)
      for i in range(N-1):
        # checking for double pairs
        if(double_pair == False):
          pair = line[i] + line[i+1]
          split1 = line[:i]
          split2 = line[i+2:]

          if pair in split1 or pair in split2: double_pair = True

        # checking for in between repeats
        if(double_letter == False):
          for j in range(1, N-1):
            if line[i-1] == line[i+1]:
              double_letter = True

        if double_pair == True and double_letter == True:
          num_nice += 1
          break

  print('There are ' + str(num_nice) + ' nice strings in Santas second model!')

part1()
part2()