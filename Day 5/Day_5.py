##Day 5 Advent of Code:

input_file = "real.txt"

input_buffer = []

with open(input_file) as f:
    for lines in f:
        input_buffer.append(lines)

#print(input_buffer)


##Mapping
seed_to_soil_map        = []
soil_to_fert_map        = []
fert_to_water_map       = []
water_to_light_map      = []
light_to_temp_map       = []
temp_to_humid_map       = []
humid_to_location_map   = []

def find_seeds(seed_row):
    #print("look for seeds")
    temp = str(seed_row)
    temp=temp.replace("\n","")
    split = temp.split(":")
    num = split[1].split(" ")
    num.remove("")
    return(num)

def seed_to_soil(seed):
    output=seed
    #print("output: ", output)

def find_mappings(input):
    counter = -2
    ##print(len(input))
    for x in range(len(input)):
        ##print(x)
        if(str(input[x][0]).isalpha()):
            counter+=1
        elif(input[x] == "\n"):
            nums = 0
        else:
            temp = str(input[x]).replace(" ",",")
            temp = temp.replace("\n","")
            nums = temp
            nums=nums.split(",")
            ##print(input[x])
            ##print(temp)
            ##print(nums)
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
            #print("whoopsie")
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
    ##print(source,dest,dist)
    lister = [source,dest,dist]
    return list(lister)


# ## NEED TO WRITE TO A SEPERATE TEXT FILE, AND THEN READ EACH ONE INDIVUALLY
# def new_seed(seed1,length):
#     #print(seed1,length)
#     new_list = []
#     for x in range(int(length)):
#         new_list.append(int(seed1)+x)
#     return(new_list)


seeds = find_seeds(input_buffer[0])
seed_store = 0
seed_list = []
# while seed_store<len(seeds):
#     temp = new_seed(seeds[seed_store],seeds[seed_store+1])
#     seed_store+=2
#     for x in range(len(temp)):
#         seed_list.append(temp[x])

# seeds.clear()
# seeds=seed_list
find_mappings(input_buffer[0:])
for x in range(len(seeds)):
    seed_to_soil(seeds[x])

def convert(seed,map):
    
    for x in range(len(map[0])):
        #print(map[1][x],":::",(int(map[1][x])+int(map[2][x])))
        if int(map[1][x])<=int(seed)<(int(map[1][x])+int(map[2][x])):
            # #print((int(seed_to_soil_map[1][x])))
            # #print((int(seed_to_soil_map[1][x])+int(seed_to_soil_map[0][x])))
            #print("converting:",seed,"to:",seed+(int(map[0][x])-int(map[1][x])))
            return(seed+(int(map[0][x])-int(map[1][x])))
        else:
            pass
            ##print("No Change to:",seed)
    return seed

## Updating Maps

#print(seed_to_soil_map)
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


final_maps = [seed_to_soil_map,soil_to_fert_map,fert_to_water_map,water_to_light_map,light_to_temp_map,temp_to_humid_map,humid_to_location_map]
#print(final_maps[1])
final_output = 0
for x in range(int(seeds[0]),int(seeds[1])):
    #print(x)
    initial_input = int(x)
    for y in range(len(final_maps)):
        if y == 0:
            input=convert(int(initial_input), final_maps[y])
            final_output=input
        else:        
            input=convert(input, final_maps[y])
            if input<final_output:
                final_output=input
    

print(final_output)
##Main will find the starting list of seeds, store that to the seeds location
##After seeds are stored, will walk through from seed down to location in the end
### will find look for the location of source, then match the destination



