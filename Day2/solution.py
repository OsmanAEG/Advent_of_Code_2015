dimensions = []
paper_sqft = 0
ribbon_ft = 0

# loading in dimensions
with open('input.txt') as f:
  for line in f:
    split = line.strip().split('x')
    dimension = [int(split[0]), int(split[1]), int(split[2])]
    dimension.sort()
    dimensions.append(dimension)

# calculating box surface area
def surface_area(dim):
  return 2*(dim[0]*dim[1] + dim[0]*dim[2] + dim[1]*dim[2])

# calculating the shortest perimeter
def shortest_perim(dim):
  return 2*(dim[0] + dim[1])

# calculating total paper needed
for dim in dimensions:
  paper_sqft += surface_area(dim) + dim[0]*dim[1]
  ribbon_ft += shortest_perim(dim) + dim[0]*dim[1]*dim[2]

print('The elves require ' + str(paper_sqft) + ' sqft of paper!')
print('The elves require ' + str(ribbon_ft) + ' sqft of paper!')