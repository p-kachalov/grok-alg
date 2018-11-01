from collections import deque


def find_seller(graph, start, predicat):
    search_queue = deque()
    search_queue += graph[start]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if predicat(person):
                print('{} is a mango seller!'.format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == 'm'


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

find_seller(graph, 'you', person_is_seller)
