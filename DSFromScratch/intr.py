import pprint
from collections import Counter, defaultdict

pp = pprint.PrettyPrinter(indent=4)

file = open("example.txt", "r")
all_words = file.read().split()


word_count = Counter(all_words)

pp.pprint(word_count.most_common(15))


item_list = set([1, 2, 3, 1, 2, 3])
num_items = len(item_list)
pp.pprint(item_list)
