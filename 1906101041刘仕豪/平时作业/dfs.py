def iter_dfs(G,s):
    S,Q = set(),[]   #访问集合和队列
    Q.append(s)      #我们计划访问s
    while Q:
        u = Q.pop()  #使程序进展
        if u in S:continue  #是否访问过？跳过
        S.add(u)
        Q.extend(G(u))
        yield u             #u就是我们要的
