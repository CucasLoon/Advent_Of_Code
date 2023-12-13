input_file = "Example.txt"
#input_file = r"C:\Users\rd00lcc\Desktop\Advent of Code\Day 8\example_2.txt"
#input_file = r"C:\Users\rd00lcc\Desktop\Advent of Code\Day 8\real.txt"

input_buffer = []

with open(input_file) as f:
    for lines in f:
        input_buffer.append(lines)


test = ((str(input_buffer[2]).replace(" ",",")).replace("\n","")).split(",")
print(test)


##Run through find arithmatic
##If no identical pattern,return new list of data
##Rerun until arithmatic pattern is found



def find_arithmatic_pattern(input,levels,matching):
    global depth
    if matching == True:
        print(levels)
        depth = levels
        return()
    else:
        sequence.append([])
        levels+=1
        print(sequence)
        for x in range(1,len(input)):
            sequence[levels].append(int(input[x])-int(input[x-1]))
        
        find_arithmatic_pattern(sequence[levels],levels,len(set(sequence[levels]))==1)
    pass

depth = 0
sequence = []
find_arithmatic_pattern(test,-1,False)
print(sequence)
print(depth)