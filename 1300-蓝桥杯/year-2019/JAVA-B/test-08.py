def find(K,S):
    conut=0
    for i in range(len(S)-5):
        if S[i:i+5]=='Alice' or S[i:i+5]=='Bob':
            conut+=1
    return conut

print(find(20,'ThisisastoryaboutAliceandBob.AlicewantstosendaprivatemessagetoBob'))
