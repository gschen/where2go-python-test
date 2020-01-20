def jia(count, a):
    if 0 <= a + 1 < 12 and a != 3 and a != 7:
        count.add(a + 1)
    if 0 <= a - 1 < 12 and a != 4 and a != 8:
        count.add(a - 1)
    if 0 <= a + 4 < 12:
        count.add(a + 4)
    if 0 <= a - 4 < 12:
        count.add(a - 4)
    return


class test1:
    all = 0
    for i in range(2**12):
        test = "{:0>12}".format(bin(i)[2:])
        test0 = 0
        for t in test:
            test0 += int(t)
        if test0 != 5:
            continue
        bs = str(test)

        count = {-1}
        where = []
        for a in range(12):
            if bs[a] == '1':
                jia(count,a)
                where.append(a)
                for b in range(12):
                    if b in count and bs[b] == '1' and b not in where:
                        jia(count,b)
                        where.append(b)
                        for c in range(12):
                            if c in count and bs[c] == '1' and c not in where:
                                jia(count,c)
                                where.append(c)
                                for d in range(12):
                                    if d in count and bs[d] == '1'and d not in where:
                                        jia(count, d)
                                        where.append(d)
                                        for e in range(12):
                                            if e in count and bs[e] == '1' and e not in where:
                                                all+=1
                                                where.append(e)
                                                break
                                            else:
                                                continue
                                        break
                                    else:
                                        continue
                                break
                            else:
                                continue
                        break
                    else:
                        continue
                break
            else:
                continue
    print(all)