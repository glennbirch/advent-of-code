def main():
    with open('input.txt') as file:
        lines = file.readlines()
    
    nums = [int(s) for s in lines]
    
    prev = float('inf')
    count = 0
    for s in lines:
        if int(s) > prev:
            count = count + 1
        prev = int(s)

    print( count )

    count=0
    for i in range(4, len(nums)):
        if nums[i] > nums[i-3]:
            count = count + 1

    print( count )

if __name__ == "__main__":
    main()