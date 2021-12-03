import sys

def get_rating(nums, zeros, ones, rate_type):
    ox_zero = {'ox': '0', 'co2': '1'}
    ox_one = {'ox': '1', 'co2': '0'}

    for i in range(12):
        next_ones = 0
        next_zeros = 0
        if ones >= zeros:
            j = 0
            while j < len(nums):
                if nums[j][i] == ox_zero[rate_type]:
                    nums.pop(j)
                    j -= 1
                elif i < 11:
                    if nums[j][i+1] == '0':
                        next_zeros += 1
                    else:
                        next_ones += 1
                j += 1
        else:
            j = 0
            while j < len(nums):
                if nums[j][i] == ox_one[rate_type]:
                    nums.pop(j)
                    j -= 1
                elif i < 11:
                    if nums[j][i+1] == '0':
                        next_zeros += 1
                    else:
                        next_ones += 1
                j += 1
        if len(nums) == 1:
            return nums[0]

        ones = next_ones
        zeros = next_zeros
        

def main():
    zeros = 0
    ones = 0
    bin_nums = []
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            bin_nums.append(line.strip())
            if line[0] == '1':
                ones += 1
            else:
                zeros += 1

    ox_rate = int(get_rating(bin_nums.copy(), zeros, ones, 'ox'), 2)
    co2_rate = int(get_rating(bin_nums.copy(), zeros, ones, 'co2'), 2)

    print(ox_rate * co2_rate)

                
main()
