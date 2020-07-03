#! python
# coding = utf-8







def exam(K, N):
    if N == 2:
        return 2 
    elif K == 0:
        return 1

    x = N // 2
    return x * exam(K-1, N-x)



import array
a =  [[1,2,3],[4,5,6],[7,8,9]]

class Solution:
    def find_best_path_cost(self , A ):
        ave_c_l = []
        ave_r_l = []
        for r_index in A.shape[0]:
            num = (sum(A[r_index, :]))/A.shape[0]
            ave_r_l.append(num)
        
        for c_index in A.shape[1]:
            num = (sum(A[:, c_index]))/A.shape[1]
            ave_c_l.append(num)
        



        





if __name__ == "__main__":

    print(125 //2)
    while True:
        try:
           K, N = input().split(' ')
           K = int(K)
           N = int(N)
           print(exam(K, N))
        except:
           break


