import numpy as np


def DCG(score):
    return np.sum(
                np.divide(
                          np.power(2, score) - 1,
                          np.log(np.arange(score.shape[0], dtype=np.float32) + 2)
                         ), 
                dtype=np.float32)


def NDCG(relevance, rank_score):
    print('computing idcg')
    idcg = DCG(relevance)
    print('computing dcg')
    dcg = DCG(rank_score)

    if dcg == 0: return 0
    return dcg / idcg


def rank_score(rank_list, pos_item):
    relevance = np.ones_like(pos_item, dtype=np.float32)
    it2rel = {it : r for it, r in zip(pos_item, relevance)}
    
    rs = []
    for ranked_it in rank_list:
        if ranked_it in it2rel:
            rs.append(it2rel[ranked_it])
        else:
            rs.append(0.0)

    rs = np.array(rs, dtype=np.float32)
    return rs, relevance


if __name__ == "__main__":
    ## https://zhuanlan.zhihu.com/p/84206752
    rank_list = [1, 4, 5]
    item_list = [1, 2, 3]
    #
    rs, relevance = rank_score(rank_list, item_list)
    print('rank_score::',rs)
    print('relevance::', relevance)
    # 
    ndcg = NDCG(relevance, rs) 
    print(ndcg)