def main():
    with open('input.txt') as file:
        lines = file.readlines()
    
    nums = [s.strip('\n') for s in lines]
    nbits = len(nums[0])
    bc = [[0]*2 for i in range(nbits)]

    print(nums, nbits, bc)

    for n in nums:
        for i in range(0, nbits):
            if n[i] == '0':
                bc[i][0] = bc[i][0] + 1
            else:
                bc[i][1] = bc[i][1] + 1

    gamma, epsilon = "",""
    for b in bc:
        if b[0] > b[1]:
            gamma+='0'
            epsilon+='1'
        else:
            gamma+='1'
            epsilon+='0' 
        
    print(bc, gamma, epsilon)
    print(int(gamma, 2), int(epsilon, 2))
    print(int(gamma, 2)*int(epsilon, 2))

    o2, co = "", ""
    o2l = nums.copy()
    col = nums.copy()
    for i in range(0, nbits):
        a = list(filter(lambda x: (x[i] == '0'), o2l)) 
        b = list(filter(lambda x: (x[i] == '1'), o2l)) 

        if len(a) + len(b)==0:
            o2+='0'
        elif (len(a) > len(b) and len(a) > 0) or len(b)==0:
            o2+='0'
            o2l=a.copy()
        else:
            o2+='1'
            o2l=b.copy()

        a = list(filter(lambda x: (x[i] == '0'), col)) 
        b = list(filter(lambda x: (x[i] == '1'), col)) 
        
        if len(a) + len(b)==0:
            co+='0'
        elif (len(a) <= len(b) and len(a) > 0) or len(b)==0:
            co+='0'
            col=a.copy()
        else:
            co+='1'
            col=b.copy()
        
    print(o2, co)
    print(int(o2, 2), int(co, 2))
    print(int(o2, 2)*int(co, 2))


        
                



   
   

if __name__ == "__main__":
    main()