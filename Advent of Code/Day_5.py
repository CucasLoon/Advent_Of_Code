##Day 5 Advent of Code:

input_file = "example.txt"

input_buffer = []

with open(input_file) as f:
    for lines in f:
        input_buffer.append(lines)

print(input_buffer)


##Mapping
seed_to_soil_map        = []
soil_to_fert_map        = []
fert_to_water_map       = []
water_to_light_map      = []
light_to_temp_map       = []
temp_to_humid_map       = []
humid_to_location_map   = []

def find_seeds(seed_row):
    print("look for seeds")
    temp = str(seed_row)
    temp=temp.replace("\n","")
    split = temp.split(":")
    num = split[1].split(" ")
    num.remove("")
    return(num)

def seed_to_soil():
    output=0
    print("output: ", output)

def seed_to_soil():
    pass


seeds = find_seeds(input_buffer[0])
print(seeds)

##Main will find the starting list of seeds, store that to the seeds location
##After seeds are stored, will walk through from seed down to location in the end
### will find look for the location of source, then match the destination



