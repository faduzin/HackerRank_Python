if __name__ == '__main__' :
    score_list = []
    score_value_list = []
    n = int(input())
    for _ in range(n) :
        name = input()
        score = float(input())
        score_value_list.append(score)
        score_list.append((score,name))
    sorted_score = sorted(set(score_value_list))
    score_list = sorted(score_list, key=lambda a: a[1])
    for i in score_list:
        if i[0] == sorted_score[1]:
            print(i[1])