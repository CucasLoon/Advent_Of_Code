input_file = "real.txt"

input_buffer = []

with open(input_file) as f:
    for lines in f:
        input_buffer.append(lines)



direction = list(input_buffer[0])
direction.pop()
Left = [7,10]
Right = [12,15]
step_count = 0
current_location = "AAA"


def find_location(input):
    x=0
    for lines in input_buffer:
        x+=1
        if lines[:3] == input:
            return(x)

def choose_next(You_are_here,current_direction):
    print(current_location,"Choosing",current_direction)
    if(current_direction == "L"):
        print(You_are_here)
        print(input_buffer[You_are_here][Left[0]:Left[1]])
        return(input_buffer[You_are_here][Left[0]:Left[1]])
    else:
        print(input_buffer[You_are_here][Right[0]:Right[1]])
        return(input_buffer[You_are_here][Right[0]:Right[1]])


while current_location!="ZZZ":
    step_count+=1
    current_line = find_location(current_location)-1
    #print(len(direction))
    #print(direction)
    #print(step_count%(len(direction)))
    current_location=choose_next(current_line,direction[(step_count%(len(direction)))-1])
    

print("FINISHED WITH: ",step_count)