l = ['','+','-']
for aa in l:
    a = '1'+aa+'2'
    for bb in l:
        b = a+bb+'3'
        for cc in l:
            c = b+cc+'4'
            for dd in l:
                d = c+dd+'5'
                for ee in l:
                    e = d+ee+'6'
                    for ff in l:
                        f = e+ff+'7'
                        for gg in l:
                            g = f+gg+'8'
                            for hh in l:
                                h = g+hh+'9'
                                if eval(h) == 110:
                                    print(h,end='\n')