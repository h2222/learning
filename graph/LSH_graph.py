# coding = utf-8




'''
LSH locality sentitive hash 

P(similar) = 1 - (1 - S^r)^b   

S : similarity of two items
r : rows per band
b : bands per signature matrix
'''


import numpy as np
from matplotlib import pyplot as plt
import matplotlib 

def lsh_graph():
    r_b = [(3, 10), (5, 20), (5, 50)]
    s = np.arange(0.01, 1, 0.001)

    for r, b in r_b:
        p = 1 - (1 - s**r)**b
        plt.title('LSH probability S_curve')
        plt.plot(s, p)
        plt.show()
                


if __name__ == "__main__":
    lsh_graph()
