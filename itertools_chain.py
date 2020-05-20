import nltk

character_freq = nltk.FreqDist(itertools.chain(*[ch for ch in raw_characters]))
sorted_characters = sorted(character_freq.items(), key = lambda x: (x[1], x[0]), reverse = True)
# 정렬 기준 : 빈도수가 가장 높은 것 먼저, 그 다음은 가나다라 순 오름차순 정렬
