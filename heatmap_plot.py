# 행렬 값의 크기를 색으로 표현하고 싶을 때,(logit, pred등)
# plt.imshow
# plt.matshow
# 둘 다 되는데, x축이 아래쪽이 아닌 위쪽으로 올라가는 문제가 있었음.
# imshow는 ax.xaxis.tick_bottom()하면 깔끔하고, matshow는 여전히 여백이 남아서 더 수정이 필요했음. -> plt.imshow 사용함

def heatmap_plot(name,title):
    plt.figure(figsize = (10, 6))
    plt.imshow(name, cmap = plt.cm.jet, aspect = 'auto')
    plt.colorbar()    
    ax = plt.gca()
    ax.invert_yaxis()
    ax.xaxis.tick_bottom()
    plt.title(title, fontsize=18)
    plt.show()
