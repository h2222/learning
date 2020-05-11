# coding=utf-8


import pandas as pd






def eval(out_true, predicts):
    '''
    out_true: the true labels (list)
    predicts: the predicted results (list)
    '''
    categories = set(out_true)
    evald = {}
    for c in categories:
        evald[c] = {}
        TP, FP, TN, FN = 0, 0, 0, 0
        for ot, pd in zip(out_true, predicts):
            if ot == c and pd == c:
                TP += 1
            elif ot == c and pd != c:
                FP += 1
            elif ot != c and pd != c:
                TN += 1
            elif ot != c and pd == c:
                FN += 1
        accuracy = (TP + TN) / (TP + FP + TN + FN)
        precision = TP / (TP + FP)
        reacall = TP / (TP + FN)
        F1 = precision * reacall * 2 / (precision + reacall)
        evald[c]['size'] = TP + FN
        evald[c]['accuracy'] = accuracy
        evald[c]['precision'] = precision
        evald[c]['recall'] = reacall
        evald[c]['F1-score'] = F1
    print(evald)


        
    
if __name__ == "__main__":

    out_true = [1, 1, 1, 1, 5, 5, 1, 5, 1, 1, 5, 5, 5, 5, 1, 5, 3, 3, 5, 1, 1, 5, 5, 5, 5, 1, 5, 1, 1, 5, 5, 5, 1, 3, 1, 1, 1]
    predicts = [1, 1, 1, 1, 1, 5, 1, 5, 1, 1, 1, 5, 5, 5, 1, 5, 3, 3, 5, 1, 1, 5, 5, 5, 5, 1, 5, 1, 5, 5, 5, 5, 1, 3, 1, 1, 1]
    print('1 munber:', out_true.count(5))
    # eval(out_true, predicts)



