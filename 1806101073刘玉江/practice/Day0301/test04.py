def rankTeams(votes):
    ansL = []
    a = sorted(votes[0])
    print(a)
    for i in a:
        count = 0
        for j in votes:
            for k in range(len(a)):
                if i == j[k]:
                    count -= 1 * (100 ** (len(a) - k))
        ansL.append(count)

    ansL, a = zip(*sorted(zip(ansL, a)))

    ans = ""
    for l in a:
        ans += l
    print(ans)
#rankTeams(["FVSHJIEMNGYPTQOURLWCZKAX","AITFQORCEHPVJMXGKSLNZWUY","OTERVXFZUMHNIYSCQAWGPKJL","VMSERIJYLZNWCPQTOKFUHAXG","VNHOZWKQCEFYPSGLAMXJIUTR","ANPHQIJMXCWOSKTYGULFVERZ","RFYUXJEWCKQOMGATHZVILNSP","SCPYUMQJTVEXKRNLIOWGHAFZ","VIKTSJCEYQGLOMPZWAHFXURN","SVJICLXKHQZTFWNPYRGMEUAO","JRCTHYKIGSXPOZLUQAVNEWFM","NGMSWJITREHFZVQCUKXYAPOL","WUXJOQKGNSYLHEZAFIPMRCVT","PKYQIOLXFCRGHZNAMJVUTWES","FERSGNMJVZXWAYLIKCPUQHTO","HPLRIUQMTSGYJVAXWNOCZEKF","JUVWPTEGCOFYSKXNRMHQALIZ","MWPIAZCNSLEYRTHFKQXUOVGJ","EZXLUNFVCMORSIWKTYHJAQPG","HRQNLTKJFIEGMCSXAZPYOVUW","LOHXVYGWRIJMCPSQENUAKTZF","XKUTWPRGHOAQFLVYMJSNEIZC","WTCRQMVKPHOSLGAXZUEFYNJI"])




class Solution:
    def rankTeams(self, votes):
        if len(votes)==1:
            return votes[0]
        n=len(votes[0])
        scor={}
        for i in range(len(votes)):
            for j in range(n):
                if votes[i][j] not in scor:
                    scor[votes[i][j]]=[0 for k in range(n)]
                    #[0,0,0]
                    scor[votes[i][j]][j]+=1
                else:
                    scor[votes[i][j]][j] += 1
        print(scor.items())

        scor=[p for p in sorted(scor.items(),key=lambda item:item[0])]
        print(scor)

        result_lis=[p for p in sorted(scor,key=lambda item:[-item[1][m] for m in range(n)])]
        print(result_lis)

        result=''
        for i in result_lis:
            result+=i[0]
        print(result)
        return result

a=Solution()
a.rankTeams(["ABC","ACB","ABC","ACB","ACB"])