#similarity checking
from itertools import combinations
from collections import defaultdict
from difflib import SequenceMatcher
from functools import lru_cache

tags = 'python pythonista developer development'.split()

for i in combinations(tags, 2):
    similarity = SequenceMatcher(None, *i).ratio()
    print(similarity, i)


# O/P:
# 0.75 ('python', 'pythonista')
# 0.13333333333333333 ('python', 'developer')
# 0.23529411764705882 ('python', 'development')
# 0.10526315789473684 ('pythonista', 'developer')
# 0.19047619047619047 ('pythonista', 'development')
# 0.8 ('developer', 'development')
