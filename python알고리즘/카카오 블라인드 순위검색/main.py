from collections import defaultdict
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query =["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    hash = defaultdict(list)
    answer = []
    for i in info:
        data = i.split(' ')
        language = [data[0], '-']
        jobs = [data[1], '-']
        exps = [data[2], '-']
        foods = [data[3], '-']
        value = int(data[4])
        for lang in language:
            for job in jobs:
                for exp in exps:
                    for food in foods:
                        keydata = [lang, job, exp, food]
                        key = " ".join(keydata)
                        hash[key].append(value)
    print(hash)
    for key in hash:
        hash[key].sort()

    i = 0
    for q in query:
        data = q.split(' and ')
        target = int(data[3].split(' ')[1])
        data[3] = data[3].split(' ')[0]
        key = ' '.join(data)

        value_list = hash[key]
        st = 0
        ed = len(hash[key])

        while st < ed:
            mid = (st + ed) // 2
            if value_list[mid] >= target:
                ed = mid
            else:
                st = mid + 1
        answer.append(len(hash[key]) - st)

    return answer

solution(info, query)