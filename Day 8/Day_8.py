#input_file = "Example_3.txt"
input_file = r"C:\Users\rd00lcc\Desktop\Advent of Code\Day 8\example_2.txt"
#input_file = r"C:\Users\rd00lcc\Desktop\Advent of Code\Day 8\real.txt"

input_buffer = []

with open(input_file) as f:
    for lines in f:
        input_buffer.append(lines)



direction = list(input_buffer[0])
direction.pop()
Left = [7,10]
Right = [12,15]
step_count = 0
#current_location = "AAA"

def count_starts():
    x = 0
    y=0
    starting_locations = []
    for lines in input_buffer:
        y+=1
        if lines[2:3] == "A":
            starting_locations.append(y-1)
            x+=1
    print(x)
    return(starting_locations)

current_lines = count_starts()
current_location = []
for x in range(len(current_lines)):
    local = input_buffer[current_lines[x]]
    current_location.append(local[:3])


print(current_location)
def find_location(input):
    x=0
    for lines in input_buffer:
        x+=1
        if lines[:3] == input:
            return(x)

def choose_next(You_are_here,current_direction):
    #print(current_location,"Choosing",current_direction)
    if(current_direction == "L"):
        #print(You_are_here)
        #print(input_buffer[You_are_here][Left[0]:Left[1]])
        return(input_buffer[You_are_here][Left[0]:Left[1]])
    else:
        #print(input_buffer[You_are_here][Right[0]:Right[1]])
        return(input_buffer[You_are_here][Right[0]:Right[1]])

done = False
counter = 0
while done==False:
    step_count+=1
    for x in range(len(current_lines)):
        current_lines[x] = find_location((current_location[x]))-1
    #print(len(direction))
    #print(direction)
    #print(step_count%(len(direction)))
        current_location[x]=choose_next(current_lines[x],direction[(step_count%(len(direction)))-1])
    for lines in current_location:
        temp = lines
        if(temp[2:]=="Z"):
            counter+=1
    if counter == len(current_lines):
        done = False
    else:
        counter = 0
        
    

print("FINISHED WITH: ",step_count)