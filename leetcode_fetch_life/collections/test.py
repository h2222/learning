




def test(p='the sky is blue'):
    p = p.strip()
    start = p.split(' ')[0]
    s = [i for i in reversed(p)]

    r = []
    rs =''
    for i in s:
        if i != ' ':
            rs += i
        elif i == ' ':
            r.append(''.join([i for i in reversed(rs)]))
            rs = ''
            r.append(i)
    print(''.join(r)+s[-1])



def max_length(nums=[10,9,2,5,3,7,101,18]):
    max = 0

    for i in nums:
        count = 0
        start = nums.index(i)+1
        for j in nums[start:]:
            if j > i:
                count +=1
        print('i:', i, 'count:', count)
        if count > max:
            max = count
    print('max', max)
    return max


class Root:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def ml(nums=[10,9,2,5,3,7,101,18], ):
    if nums == None:
        return 

    troot = Root(nums[0], None, None)
    
    if troot.value > nums[1]:
        troot.left = ml(nums=nums[1:])
    else:
        troot.right = ml(nums=nums[1:])
    




    return 



if __name__ == "__main__":
    max_length()