users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
nomi = []
def dfs(cur, end, sale, tmp):
    if cur == end:
        nomi.append(tmp[:])
        return
    for i in sale:
        tmp.append(i)
        dfs(cur+1, end, sale, tmp)
        tmp.pop()
def solution(users, emoticons):
    sale = [10, 20, 30, 40]
    tmp = []
    dfs(0, len(emoticons), sale, tmp)

    answer = [0,0]
    for i in nomi:
        sale_emoticons = [[0, 0] for _ in range(len(emoticons))]
        for idx in range(len(i)):
            # 이모티콘에 할인률 설정하기
            sale_emoticons[idx][1] = emoticons[idx]-(i[idx] * emoticons[idx] // 100)
            sale_emoticons[idx][0] = i[idx]

        # 이모티콘 플러스 가입자, 총 구매 비용
        board= [0,0]
        # 이모티콘을 구매할 사용자의 구매기준 할일률과  구매기준 가격
        for stand_sale, stand_money in users:
            buy_price = 0
            buy_number = 0
            emoticon_plus = 0
            # 이모티콘의 할인률과 할인된 가격
            for emo_sale, sale_price in sale_emoticons:
                # 이모티콘의 할인률이 사용자의 기준 할인률보다 많으면 구매한다
                if emo_sale >= stand_sale:
                    buy_price += sale_price
                    buy_number += 1
            # 산 비용이 사용자의 구매 비용보다 높다면 산 비용을 전부 취소하고 이모티콘 플러스 가입
            if buy_price >= stand_money:
                buy_price = 0
                buy_number = 0
                emoticon_plus = 1
            board[0] += emoticon_plus
            board[1] += buy_price

        if board[0] > answer[0]:
            answer[0] = board[0]
            answer[1] = board[1]
        elif board[0] == answer[0] and board[1] > answer[1]:
            answer[0] = board[0]
            answer[1] = board[1]

    print(answer)
    return answer
solution(users, emoticons)