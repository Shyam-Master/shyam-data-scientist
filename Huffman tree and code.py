import heapq
from collections import Counter

def huffman_tree(text):
    
    freq_table = Counter(text)

    priority_queue = [[weight, [char, ""]] for char, weight in freq_table.items()]
    heapq.heapify(priority_queue)


    while len(priority_queue) > 1:
        lo = heapq.heappop(priority_queue)
        hi = heapq.heappop(priority_queue)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(priority_queue, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    
    return dict(sorted(priority_queue[0][1:], key=lambda x: (len(x[-1]), x)))


text = "this is an example of a huffman tree"
codes = huffman_tree(text)
print(codes)

