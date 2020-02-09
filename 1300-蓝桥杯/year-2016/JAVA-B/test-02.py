for age in range(200):
    all = 0
    for year in range(age,200):
        all += year
        if all>236:
            continue
        elif all == 236:
            print(age)
            break



