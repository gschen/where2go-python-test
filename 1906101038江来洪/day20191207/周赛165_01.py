def jiang(moves):
    a = len(moves)
    sa,lax,lay = 0,[],[]
    sb,lbx,lby = 0,[],[]
    if a < 5:
        return 'Pending'
    else:
        for i in range(a):
            if i%2 == 0:
                lax.append(moves[i][0])
                lay.append(moves[i][1])
            else:
                lbx.append(moves[i][0])
                lby.append(moves[i][1])
        sax,say = sum(lax),sum(lay)
        sbx,sby = sum(lbx),sum(lby)
        if sax == say == 3 or 0:
            sa += 1
        elif sbx == sby == 3 or 0:
            sb += 1
        if a == 9:
            if sa == 1:
                return 'A'
            elif sb == 1:
                return 'B'
            else:
                return 'Draw'
        else:
            if sa == 1:
                return 'A'
            if sb == 1:
                return 'B'
            else:
                return 'Pending'




