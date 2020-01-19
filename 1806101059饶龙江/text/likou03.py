
class Solution:
    def suggestedProducts(self, products, searchWord) :
        l = []
        for i in range(len(searchWord)):
            li = []
            for j in range(len(products)):
                if   i<len(products[j]) and searchWord[i]==products[j][i]:
                    li.append(products[j])
            l.append(li)
        print(l)

if __name__ =='__main__':
    solution = Solution()
    products=['moua','mousy','moustaaa','moutsa','moustsasasf']
    searchWord = 'mousts'
    print(solution.suggestedProducts(products,searchWord))





