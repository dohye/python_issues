import numpy as np

# numpy에서도 vstack, hstack, dstack, stack이 있지만 append사용이 가능함.
# 근데 array_ops.append는 작동하지 않았음.
# 아래 예시는 train_examples에 두개의 리스트가 있고, 각각의 리스트에는 input array, target array가 들어 있음
# 그때 input따로 붙이고, target따로 붙이고자 아래의 코드를 이용함

hinputs = numpy.append(train_examples[0][0][numpy.newaxis,:,:], [train_examples[1][0]], axis=0)
htargets = numpy.append(train_examples[0][1][numpy.newaxis,:], [train_examples[1][1]], axis=0)
