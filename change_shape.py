# 배치단위의 학습을 할 때, 데이터를 1개만 추가하고 싶은 경우
# 음성인식 학습 하다가 데이터 1개만 추가적으로 넣어서 valid처럼 결과를 찍어보고자 했음.

# shape 맞춰주는 과정에서 차원 늘리기 & 줄이기 & 변경하기
# 차원 늘리기 : 원하는 차원에 newaxis 넣기 -> [np.newaxis, :, :] / [tf.newaxis, :, :]
# 차원 줄이기 : np.squeeze / tf.sqeeze (디폴트는 1차원인걸 없애준다)
# 차원 바꾸기 : np.reshape / tf.reshape

if m.shape == []: # hello 데이터 넣을 때, batch가 1이어서 shape이 안맞아서 추가함.
    m = tf.reshape(m, shape=(1,))

hinputs, htargets = train_examples[0] # train_examples[0]은 hello 데이터, 이미 array 상태임
hinputs = hinputs[array_ops.newaxis, :, :] # hello 데이터 넣을 때, batch가 1이어서 shape이 안맞아서 추가함.
htargets = htargets[array_ops.newaxis, :] # hello 데이터 넣을 때, batch가 1이어서 shape이 안맞아서 추가함.

# n = tf.squeeze(tf.reduce_sum(tf.cast(tf.not_equal(htargets, 0), tf.int32), 1, keepdims = True))
n = tf.reshape(n, shape=(1,)) # hello 데이터 넣을 때, batch가 1이어서 shape이 안맞아서 추가함.
