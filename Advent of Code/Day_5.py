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

def seed_to_soil(seed):
    output=seed
    print("output: ", output)

def find_mappings(input):
    counter = -1
    print(input)
    for x in range(len(input)):
        if(str(input[x][0]).isalpha):
            counter+=1
            break
        elif(input[x] == "\n"):
            break
        else:
            temp = str(input[x]).replace("",",")
            nums = temp
            print(nums)
        if counter ==0:
            try:
                for y in range(len(nums)):
                    seed_to_soil_map.append(nums[y])
            except:
                pass
        elif counter == 1:
            try:
                for y in range(len(nums)):
                    soil_to_fert_map.append(nums[y])
            except:
                pass
        elif counter == 2:
            try:
                for y in range(len(nums)):
                    fert_to_water_map.append(nums[y])
            except:
                pass
        elif counter == 3:
            try:
                for y in range(len(nums)):
                    water_to_light_map.append(nums[y])
            except:
                pass
        elif counter == 4:
            try:
                for y in range(len(nums)):
                    light_to_temp_map.append(nums[y])
            except:
                pass
        elif counter == 5:
            try:
                for y in range(len(nums)):
                    temp_to_humid_map.append(nums[y])
            except:
                pass
        elif counter == 6:
            try:
                for y in range(len(nums)):
                    humid_to_location_map.append(nums[y])
            except:
                pass
        else:
            print("whoopsie")
            return

seeds = find_seeds(input_buffer[0])
print(seeds)
find_mappings(input_buffer[0:])
for x in range(len(seeds)):
    seed_to_soil(seeds[x])
print(humid_to_location_map)
##Main will find the starting list of seeds, store that to the seeds location
##After seeds are stored, will walk through from seed down to location in the end
### will find look for the location of source, then match the destination



