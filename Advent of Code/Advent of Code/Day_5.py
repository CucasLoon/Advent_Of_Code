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
    counter = -2
    print(len(input))
    for x in range(len(input)):
        #print(x)
        if(str(input[x][0]).isalpha()):
            counter+=1
        elif(input[x] == "\n"):
            nums = 0
        else:
            temp = str(input[x]).replace(" ",",")
            temp = temp.replace("\n","")
            nums = temp
            nums=nums.split(",")
            print(input[x])
            print(temp)
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
        elif counter<0:
            pass

        else:
            print("whoopsie")
            return

def sort_mappings(test):
    source = []
    dest = []
    dist = []
    count = 0
    for x in range(len(test)):
        if count == 0:
            source.append(test[x])
            count +=1
        elif count == 1:
            dest.append(test[x])
            count +=1
        else:
            dist.append(test[x])
            count=0
    print(source,dest,dist)
    lister = [source,dest,dist]
    return list(lister)


seeds = find_seeds(input_buffer[0])
print(seeds)
find_mappings(input_buffer[0:])
for x in range(len(seeds)):
    seed_to_soil(seeds[x])

def convert(seed):
    
    for x in range(len(seed_to_soil_map[0])):
        print(seed_to_soil_map[0][x],":::",(int(seed_to_soil_map[0][x])+int(seed_to_soil_map[2][x])))
        if int(seed_to_soil_map[0][x])<=seed<(int(seed_to_soil_map[0][x])+int(seed_to_soil_map[2][x])):
            print("converting:",seed,"to:",seed+int(seed_to_soil_map[2][x]))
        else:
            print("No Change to:",seed)

## Updating Maps

print(seed_to_soil_map)
newer=sort_mappings(seed_to_soil_map)
seed_to_soil_map.clear()
seed_to_soil_map = newer

temp = sort_mappings(soil_to_fert_map)
soil_to_fert_map.clear()
soil_to_fert_map = temp

temp = sort_mappings(fert_to_water_map)
fert_to_water_map.clear()
fert_to_water_map = temp

temp = sort_mappings(water_to_light_map)
water_to_light_map.clear()
water_to_light_map = temp

temp = sort_mappings(light_to_temp_map)
light_to_temp_map.clear()
light_to_temp_map = temp

temp = sort_mappings(temp_to_humid_map)
temp_to_humid_map.clear()
temp_to_humid_map = temp

temp = sort_mappings(humid_to_location_map)
humid_to_location_map.clear()
humid_to_location_map = temp

for x in range(len(seeds)):
    convert(int(seeds[x]))

##Main will find the starting list of seeds, store that to the seeds location
##After seeds are stored, will walk through from seed down to location in the end
### will find look for the location of source, then match the destination



