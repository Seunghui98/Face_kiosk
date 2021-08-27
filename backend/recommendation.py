import pandas as pd
import numpy as np
from random import shuffle
from sklearn.metrics.pairwise import cosine_similarity

class recommendation():

    def rere(best_menu):
        data = pd.read_csv("log.csv", sep=",")
        new_menu = pd.DataFrame(columns=["menu", "new_menu"])
        new_menu["menu"] = data.menu.unique()
        new_menu["new_menu"] = range(data.menu.nunique())
        data = data.merge(new_menu, on="menu")

        data2 = data.sort_values(["id"])
        train = data2[:int(len(data)*0.7)]
        test = data2[int(len(data)*0.7):]

        score = np.zeros((train.id.nunique(), data2.new_menu.nunique()))
        traim_item_list = train.groupby("id").new_menu.apply(list)

        score = np.zeros((train.id.nunique(), data2.new_menu.nunique()))
        traim_item_list = train.groupby("id").new_menu.apply(list)

        print(traim_item_list)
        train_item_lst = traim_item_list


        train_item_lst = train_item_lst.tolist()
        for ix, item_lst in enumerate(train_item_lst):
            for item in item_lst:
                score[ix, item] = 1.0

        score_t = score.T
        cosine_sim = cosine_similarity(score_t, score_t)
        # 자기자신에 대한 유사도는 1.0 가끔 0.99997이 있기 때문에 사전 처리
        for i in range(data2.new_menu.nunique()):
            cosine_sim[i,i] = 1.0
        cosine_sim_data = pd.DataFrame(cosine_sim)

        print(cosine_sim_data)

        print(best_menu)
        rec_lst = list(cosine_sim_data[best_menu].sort_values(ascending=False)[1:4+1].index)
        return rec_lst



