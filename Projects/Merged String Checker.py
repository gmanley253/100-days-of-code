s = 'codewars'
part1 = 'code'
part2 = 'wars'

def is_merge(s, part1, part2):
    #Declare initial boolean operators and pointer variable
    part1_order = True
    part2_order = True
    pointer = 0
    
    #If the two sorted strings added together = the starting string, continue.
    if ''.join(sorted(s)) == ''.join(sorted(part1 + part2)):
        
        #Iterate through the first list
        for i in range(len(part1)):
            
            #True and True = True. If a string is not found, the find function 
            #willl return -1. A True and False = False. If the letter in part1
            #is out of order, find will return -1 and a False will be returned
            #because the pointer is after index value of the next letter.
            part1_order = part1_order and (s.find(part1[i], pointer, len(s)) != -1)
            
            #If true move the pointer to the next letter
            if part1_order:
                pointer = s.find(part1[i], pointer, len(s))
        
        #Reset the pointer
        pointer = 0
        
        #Repeat the process
        for i in range(len(part2)):
            part2_order = part2_order and (s.find(part2[i], pointer, len(s)) !=-1)
            
            if part2_order:
                pointer = s.find(part2[i], pointer, len(s))
        
        #True and True is True
        return part1_order and part2_order
    
    #Else return false
    else: return False

          