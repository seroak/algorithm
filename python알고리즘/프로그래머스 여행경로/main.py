from collections import deque

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]


def solution(tickets):
    answer = []

    visited = [False] * len(tickets)

    def dfs(airport, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for idx, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[idx] == False:
                visited[idx] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[idx] = False

    dfs("ICN", ["ICN"])

    answer.sort()
    print(answer)
    return answer[0]
solution(tickets)