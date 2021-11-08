import json
from constants import NUM_OF_SEATS
from constants import PARTIES_DIC


def print_party(chairs_dic: dict):
    for k, v in chairs_dic.items():
        print(k, " ", chairs_dic[k])


class Seats:

    def __init__(self, party_dic: dict):
        self.parties_dic = party_dic
        self.num_of_voters = sum(self.parties_dic.values())
        self.vote_threshold = 3.25 / 100
        self.min_voters = self.num_of_voters * self.vote_threshold
        self.parties_dic_with_vote_threshold = self.vote_threshold_handler()

    def vote_threshold_handler(self):
        parties_dic_with_vote_threshold = {}
        for k, v in self.parties_dic.items():
            if v >= self.min_voters:
                parties_dic_with_vote_threshold[k] = v
        return parties_dic_with_vote_threshold

    def save_to_file(self, filename: str, chair_dic: dict):
        with open(filename, 'w') as file:
            json.dump(chair_dic, indent=4, fp=file, ensure_ascii=False)

    def jefferson_method(self, vote_threshold: bool):
        dic = self.parties_dic_with_vote_threshold.copy() if vote_threshold else self.parties_dic.copy()
        chair_dic = {}
        for k, v in dic.items():
            chair_dic[k] = 0
        for i in range(NUM_OF_SEATS):
            for k in dic.keys():
                dic[k] = self.parties_dic[k]/(chair_dic[k]+1)
            biggest_party = max(dic.items(), key=lambda key: key[1])[0]
            chair_dic[biggest_party] += 1
        print("------------Jefferson Method------------")
        self.save_to_file("Jefferson Method.txt", chair_dic)
        print_party(chair_dic)

    def adams_method(self, vote_threshold: bool):
        dic = self.parties_dic_with_vote_threshold.copy() if vote_threshold else self.parties_dic.copy()
        chair_dic = {}
        for k, v in dic.items():
            chair_dic[k] = 1
        for i in range(NUM_OF_SEATS-len(dic)):
            for k in dic.keys():
                dic[k] = self.parties_dic[k] / chair_dic[k]
            biggest_party = max(dic.items(), key=lambda key: key[1])[0]
            chair_dic[biggest_party] += 1
        print("------------Adams Method------------")
        self.save_to_file("Adams Method.txt", chair_dic)
        print_party(chair_dic)

    def webster_method(self, vote_threshold: bool):
        dic = self.parties_dic_with_vote_threshold.copy() if vote_threshold else self.parties_dic.copy()
        chair_dic = {}
        for k, v in dic.items():
            chair_dic[k] = 0
        for i in range(NUM_OF_SEATS):
            for k in dic.keys():
                dic[k] = self.parties_dic[k] / (chair_dic[k] + 0.5)
            biggest_party = max(dic.items(), key=lambda key: key[1])[0]
            chair_dic[biggest_party] += 1
        print("------------Webster Method------------")
        self.save_to_file("Webster Method.txt", chair_dic)
        print_party(chair_dic)


if __name__ == '__main__':
    seats = Seats(PARTIES_DIC)
    seats.jefferson_method(True)
    seats.adams_method(True)
    seats.webster_method(True)
