# coding=utf-8

'''
第三题：字母阵列
题目描述
仔细寻找，会发现：在下面的8x8的方阵中，隐藏着字母序列："LANQIAO"。

SLANQIAO
ZOEXCCGB
MOAYWKHI
BCCIPLJQ
SLANQIAO
RSFWFNYA
XIFZVWAL
COAIQNAL
我们约定: 序列可以水平，垂直，或者是斜向；
并且走向不限（实际上就是有一共8种方向）。
上图中一共有4个满足要求的串。

下面有一个更大的（100x100）的字母方阵。
你能算出其中隐藏了多少个“LANQIAO”吗？
请提交一个整数，不要填写任何多余的内容。
(注：答案为41)
'''
l='''
FOAIQNALWIKEGNICJWAOSXDHTHZPOLGYELORAUHOHCZIERPTOOJUITQJCFNIYYQHSBEABBQZPNGYQTCLSKZFCYWDGOAIADKLSNGJ
GSOZTQKCCSDWGUWAUOZKNILGVNLMCLXQVBJENIHIVLRPVVXXFTHQUXUAVZZOFFJHYLMGTLANQIAOQQILCDCJERJASNCTLYGRMHGF
TSDFYTLVIBHKLJVVJUDMKGJZGNNSTPVLCKTOFMUEUFSVQIAUVHNVFTGBDDARPKYNNCUOYUAZXQJNOEEYKLFRMOEMHUKJTPETHLES
FKVINSLWEVGAGMKVFVIUBMYOIAFHLVNKNTYKTZWVXQWRWIGPENFXYDTKRVPKRTHMGHVYOCLDCKMEKRLGEKBYUCLOLYPAKPFSOREH
KWPUOLOVMOFBIXYACWRDYBINTMPASPCEOKHXQIGBQQMCEOIVULIEOPFSCSIHENAJCVDPJDOIWIIULFDNOZOFVAMCABVGKAKCOZMG
XWMYRTAFGFOCNHLBGNGOXPJSTWLZUNNAGIRETGXFWAQSSJPFTQAXMTQWMZWYVEPQERKSWTSCHSQOOBGXAQTBCHOEGBDVKGWJIFTG
ZWWJEIISPLMXIMGHOOGDRZFTGNDDWDWMNUFWJYJGULPHNUFSAQNNIUVAAFZIAZKFXXNWCEABGJAUMGYEIEFVQXVHHHEDYUITRCQB
XZHDPZQTOBECJVBZLACVXACZEDYOGVAVQRNWEOWGRAQYUEUESTEDQTYJUTEFOOITSHDDZHONJGBRCWNEQLZUTBNQIADKNFIOMWZR
EBFKCVNLURZSNPOLTISRPDTNUMCDGKTYRGIOVEPTUTSBAWQKWWEUWIWHAANUZUADGZEATZOQICWFUJTWNZDBKLQNELWVTBNDLNFH
PESISEATZNCDFRMXBQUKBFTIGYSFCWVHPMSUSDKPSCOMVLDOHYQVFHAJKRDTAVLIMNZBZSMLMRTLRPSLAHXDBASDMWAAYBPYVJZF
SCCWYHLQOUKBMCEYENQNJXFOMOOJMTKDSHJJOHDKEGATFZHGWJJAZJROWHAZUFGEQKPYXLCAAXHHQBDALPYUDWZQHBASBBCFGQCQ
ZKNXUBRYZVSPQHOVLAEUAUITMPWXNXJQVIBJVBCSVXKWFAFRPRWOLYVSDVTGGOFFMNQJZOBUDJLFHJTCYMPNOBHQJHGKLIKLZMLA
POCKVEQXUAVHERIAQLGJHYOOVOMTXQFRTBFSETOZICPCHZHFBWNESVJJLSVSVOOGYYABFESWNWDNYBGBNAKRCFQMTCUMIFTESVIN
JCAULIQRYUMAMAOVVWSEUTMECXSDTONRMMROQUISYEURSAYNZUVOPXLIFBDOHPXMABBLEQZGLJXQJOEYYRRRCFTEZQAOIWKRJQDL
ZNUUDWZXZZURPMHGXQGNQBIQWWNERZWULSAPIBODBFFQQIHEQKCKLJYQNXQUTAAYGRBXSLLQNOQPZJEWHETQHPXJANMJFOHINWOW
KJGAWWFSVIZHFNUWBLWYVPIWAEICCAHOEIWRADSLOZGPSVGPUBUUQAVYCHOIGINKYKJABWAQCZCXOBKTNJZQRHLUFKQLACAAOIWJ
SIKWLXQHKDFJVGBVXWDWJKUSFRQRTDJYQMNFOQQALHRLMHSDMCFLAOVKDMTKMTPVTLAZLYJNJXZCFRHHSDIXYUUSVIMIICLUJHFW
JHWUSMCFYHPIXHAPBBSHYDQCKVGQFTENLVERFVOVDCLSTQFUSEPUMTFODLZLYQXDOXAEPONIQWTDWSAWBNSZYACGSJQSHAUMIKXT
MVBNFXMFNPAYSODPXEAYNRKTEZJWMUACSIUYPIORUFPMXAOZZJPJXPFLNSKNIAMETMOVULZPQIJJIRCSYQXOEVRHCNACSBRHKYNW
KGKBTBHGWKVJYZCOVNSKUREKZEIWVLOHAMUAYKLUGHEUESICBZAHURNTJAECTHRNKSIJQFIPVZANSZYSPJWHPKHCAPEYWNXUYQSD
RRRFYQFIQSWYRQTSNGNUFOBMSLGAFWPJGYEHGASFKTJCCZPXFIQLSXNKNWCYVTETOAPCOZJNHEWOCCAWVDEZUQCLLAVUQJJTQCKJ
NMBKMUENVGXXVMQCLXPJDQIQCFWYADIFDSGINGZDJYHPUPXVRMWDIPJRWPNRYOFGYYPEAVKDEMLYRRRMNCRQXPTDSQIVKKGJWDEF
SBAEKIFZCKDOMIQKBDWVQGBYWPDIBOLQUGAQRXLJDAZMXVZXYSNWEWTNZKYREMBEUHOTFOCKEJSXCMUBCKXNGQXTQJRCRCLWJTOI
YXBFBIBRAAFNPKBLTSMCFERZURZNWHMOEHIHNQTBWXNPJGIDYDPRGEWACCBULJRACOFLANQIAOIHMYCNQHVKXSIGAMWAHUSNBBTD
QDGPTRONXHAZWOUPNBFJFEWAMFZUQZFDKAPNJUBQPWBPYGPZHKUDZZDLCCWHGAUKJCSLLFWGPYJKJQBNLCZESOGXXSQCVVKVRVAW
NXPGQOUEFLUZHHSAODIWEPZLXVQLYGVOOVCCREDJZJOMCSCFFKEIEAVCTPUZOWNOLJHGBJHJFBFFORGXOXXFOCAGBWEFCIDEKDLB
PTXSUINQAJURNFQPMMSPLZTQAHCIOFJUEFFZGIHTSJNIEXQLLHRQUXXLLORJEHGQJOXSLIAVFPEJNGMMVAXDDMPXLOSTRLLFLYRM
JQNCLENGTROIKDWBMXRNJYPGZRQOREPJJPTXKVVKPYYZENEOIQKZOPXAYGFXORXRIDGATHMZFDJIOIOKVDJBHSXQMYCBYFGXWHLH
CITGTILGPGBHZMNWWHXEFPGDPJUVFBJKAQWACZHPRPJYCOLGZTBDCVHNRSUAJUQAWAPMQJDQIFPZQZEONWHIYKMXDZOMVETEFJRB
RDOTIDCFEESOKYPYCGQQKOGPMGJRITSVTKOKDSXLRLJRRHNFRFXCMDNQMCEGZFJWHZOAFBQXXPXNBSWTSUYPAWQRHAUGLNPBRSJT
HOWRIUGMOQTUYIHDWJRFBWWKWYKCICSVBVKTBIIWGFSVIFCTUKIHHUUISCOTEOYRWQXTAEBXQQOLLMOALNIYVCCHNSWIKHMYYNZO
OFRIYYXPPSRTPAYMUJSSDILKIZAYSEIOLANQIAOVKARDPGVFCSYBSNHAPGTIKLAWTTKOEADWRLAACAAFYTBTNSGFTYLYUHJXBMMA
NJFTMLUIBKDPWBXQOMBVQXCZOIREHRSZCSJOIVBXWQIBUTYBQNTZRVROHGOIZYAJWXLEATLOZJIKJMIHSLGSVTCXJWIOOGWSERRQ
DBQJNGBLRIYFIKHBEYOZQBOAGGNIZKFDHWXCFNJLBQXVLHIQNIBZSDLTTRERHNWCMLJCVBBGGAQTPUQHIRABXPQSYGSDVMBNNDFG
KPLFUYXHYGOCZPPXMWCZYNKCYBCRZVKFBHQXPGPBZFTTGEPQTJMOFHAYSQQZDMQECGXOXADYHNNXUKNBXZBYHBOULXNBJZKIZREF
LVHAMSNXJOCVRPVGJUWXFVOCUCLCZDXRPBBDRLRAVVNLOZWOHWMXYSNMXAKJYWYGILNGUJGIPKAUDVANZLFWKUWWUSQYBRCBVDIJ
QCXPLOTPPGXCUZOUSSTXHVMLHVMJTUSSOPLRKEBQSGWNGVHKANVZWYQHSHLIPWSYCPKTUKPMWPLVFLLAHXZQANFXHFNYHIQVIOYN
ZPTJJCBHXPSUPOMNRVCKXSUFCNRCRNCPTPGIDQOEQUDFNUNMJPOEKVIMUJAJZOUKMAFSLDWYMCHTSNJYUDJAHQOIXPYSRHVAFFCR
DCGMEEWXWMNOSSJNIZCINRHENPPPCYVFWYCONOPKXMFZXXIHNXIGAHAMHSBRESOETGVXWDNQLGCEOUDDJXHQIVCHRNKBFFEWILGY
SOAIQNALXRBSGAQIDQVMVDKVZCPMJNXKXRXPFZAUVQPBHHQKTPDSQROLQTUGMFQRWGVEWCYPDYDZGNNNUFKJUEHJKPLIQNRQYXHU
GKGWUCJXUKAEHLRLNDFUQPSJAZTVJRXWXQVBMRJXULEMJJPDCVTOWVFDBVLSBHZRRQUVMUQYKTJCLSGGHGCPHPHMWYAECLJIZUWV
QQNKPQRJMSOCEAYDNKPHVEGKAGCKAPDXTGVXULHUXHJPDXCSKQTCJENVTZTMRUENCSWHBEORALSREBWAJEMQDXMRKGHJGICDHKHY
YNSDSWDRLBBFUFVVICMGUCGBSVDLJNXGKXNFGVLKAVBJRRRUHKRXTPBJAKIEBAVMDIOJLIUDABCGNPNJIYBCXMOOWKRPHPYSWRDC
BORWTNBISSLTVKBRTLWKRNCEDCNEGCIYJIPDICFAVNOISYAHWBLGMNFKXZYTTWJOBEPNMSJEJMHXVPGOJOLQQQVXFGEULANQIAOD
OQETOJHCZXGTUKIWGMEVVMXCURISUOFQSAWZWDMZWVYHZMPEIMWKJDGERODVVUXYRTYLCRGYQQOIOFZSSZRAIESWBQOAIQNALJNR
HEYWHPLLPCUEOCBAOWGAYEJZQJHLVNMVQNSQQGGUBOIMDPFLOVSQGBLYAMBRYJDVOXOQINLJAVYALAKHPKOYNKGXIISSJNGKHYMS
IQVRYKXCUFIRNENEXFJTMOTJWYXSMTDHHPRHWIXETWVVIXZELKLLWRWQYGBCGJNYSUQEFCOUDNIJMLJNLAWSYJGULKBCFPYVSSMW
WQHGWRQFWFOTGPBBSJBDUKOMBXNRPIMCGPGVZFADWTBVIEMVTBXVAFQDDMJALCOMZTXUFFKBQQZDFAMTFWEXTHBKNWRLUVITQXLN
OPPJQKNGHWWPENVQIABJCQNKXNPWOWRFEOKQPQLANQIAORGGOLAYCEGZBHZVLPBERWYIJNJUNXKULUQOJLTNRDZDEYWEMYCHJLLB
LJISOAQLXJEFXVTOZSICOLQIJEXUANJWIFSIMGUQWHBXUDWOEILYFUZTGDZDSPLZPDPXBLFAXLEFQFEPDSJQWEQMXKKHCXHMSATM
UMUJENPBYKZLWAJAXJKDIYCBREBPOETQHMRHLKSEZUIPRGWIZDDQLSJAPKPBWMJMPZWLNFLFCQOCDBMLIHIYCXUJLFLPZVGWBKMY
WHZJLKEWUPETVUREKVKCLBNYFLWCERVIPUDINNWGQTUHWXCTDVTMYATYUZLMVLOHKBOGIZCQDOWFBCWJAVUXYUEVRKPOXCKHAWZC
RPLNLCUHJRADHJNSDPZXIKXGUKEJZCFJQASVUBSNLXCJXVCJZXGMRYRLOBCNGPDUJQVEFKMYHNZGZOAIQNALQDHTBWJXPKJLFXJY
MKCEZEDAFGSOCORWJGMOKWPVVBVDYZDZHPXFWJBDELHPGOQHMBAHUUUJMGXAEKZCTQTBXNVYUIQUVZGXSKQXJWRUPSFIJDYIAORC
GKFKQNXPJWOPPBTUKTHUBIROSYOVFEMJBRREWICJPCIOSTWPAUSKTRQULXPWRSXHSRYBCWYCYOTCTPFSQLDIILIGMEVZKYSOYRPH
SFDSCSMLLNARCCGCBJOGZAEQTGNGSFAQIXLPDBSWZDTYVASYYPVBRFBTIAGGWONGSVKCJDBBLYKAIOXUATGMALZXFOHZFTXALCFU
CUSSTLCRYPDTFSFJFENKJWTEBOBEPLSNXLALQWCKSLVMZQDJITHZKVCCQXTEXOSVAUFYAZXJUOAPPVEEWOIIMOSZZMCOQBRUXWKG
PDOFSCKKJJTRYRWGLEZODQTJSIMXIAOLNMLPHBAYLPTTLPYWILSEIIQVSXNHIJEORVCNJHYXRBIZZJTADGMRTSXVRXYGVQQNUEIC
IHNJOQXUXTXFPALCHOELNVMWDWQTEARUKPIFWXJSMWZLMNLAODUTKNZDYRFRLGBLIBGIBXJBOYMLYLANQIAORORYKSJPOOOAMVRN
IWIUHLYJKTQGVJBDPROSRGZUFITDIBCDPICNEFIGHWGSROWBYKUCLCQYLJXLHLXSCTJWKDLHHMLDBZCVDKPXYYASHUUMUJMVSXAD
GXOYXQFEBFIEJJLHBNGSYALOUXNQBXXZAAZJXENJJVVGFVHOTKSLEGLJVSJCQHSSZFEIOGBOGWSPIRENQAAWRQFBEFEXBKGMSTRC
PYIANSGMNKBCDPHWDUPKICQEUDNZPNGRUJYSZIRLXGXXITAFBCANGDLVAQLDPVTJNSAUZMBBNOBBOERSHQIOLBVTSPPJKVCMXUBS
IKMDIYSNCJZKJKJQMTIKEPRUNAHJUSWJHSLWIVWHYAYLOIOGSZVWKQWXZDBPHWZRAIPMXDJHBIISVJWVEVZAEGAKCYYMNZARBZPC
DLDFVQDFDMVHYVOWEKMFKWUXLTPWIVKPRZZXOLMDAPAIQEKJHCHYAGJDBOFWDGNEGQGOOKWSKLTLREMGGTVJFHAIBCQKNZVRCZYS
FBQASGNCCBBGNKJHCDBTGBIIWKMPHDABKEWDEPYEAVKNMPATUZZUOEHGUGAZNECSGUCIIJPMMRAMTVADMTCRJCBWDLWWFNFOWMVZ
XFJFBGDAVGGAIZHAUIYENDZTRUWHPQUFWCHOXNCWYNAWVPLBLNQKQDTKQQKXNFXCTBGRWUZFHNRBDNLNKQVOLLGBBJQIYOBCEIKO
CURAGWXMLYBSIZLAXFONZZMQMRNNSRQKRHQGFGZUTLONAYRKSSOWAMKZBSGOOYQDPTBHGPBNQEDCZHRTOXREOFJEKJVIZXZBCJPN
KGYBZTZRKOGBETJRUWRNUCIFKIMCZGYTZLCZYGCGKVZRJIFZQIQPTCPPUHYWIXBOFFGSGSAIMNGKKUUROAVNJUQQNSWJRZIZEHAF
DDAOBVCPOVODVJFLSNPJXHWQBHILWZAHQQMTQASNADZLZNXJLJMFCOUWOZJCMVVTYCKTUBABWLCEBNYWAMOLNBQQYBRUJCQCZALE
TVVRPMYFIKINHIUEJBDLTCUMMUWICIUVCZNIQIUEWVAHLANQIAONMEYJWPDAFXVNOSOFDOCESSLGZPTJINBUAFWWWMPTYALZIGVD
DCZGKILMBFXIQQFEKJBIUDEMIFCANVGNYZAYSQFMNNQFEPZFUUVGTBKSMDXITBLANQIAOQUKTPNYPOWSQQYWWMJHSDYVFDJYXBAF
VGYXAMDRRZWVIHNQPZZWRNWBTROOJOLNUGXBILZKQEGIQSYGKZGODPWBJSCMRRWSSQURUFIAFQGEZLGZNOEQMNQEYUKPEQPPVAMO
SYSFUAJFKIPUJVQSZRWQCJYAUMLDDNOKODDXIEQIFLANQIAOZFUNKUBVDBLMJOAUTVCZVLKJRQIORQPGAVCEYVNYUZHXILHERYEC
GJEKWEKIJNIWUXZNVIWIAANHIOSOLATSQFSSCTAKESUTSPPYFHEHLVLIBJZEEBCOWMNHFTZMAPKFUPNFLTFFJQRVJHAKDVMGGUIX
KAKXXNKSOAIQNALLWKWGVACYWBQEVTFSEUCYRORQTHWFUJFLQHONWZEKPLSNPRPBOMOFFCPMKXFZBKIERBKDYFKYUEYVYRPMOAQI
WNICDLQKZXGTKDLIEFBGELGJOAIQNALXZLGGDQIBVEULDPBWUJNTYOKFBPGMAWRRUJPPIGYCNYURNOSQRIRBAZAGWWDUHAAZQWPT
KFXZQXRMKSBUXWOUVVHSJWTLKZELGXMMAIDSJIWGCJPCBWZIEKMNUPUAFHTUMOZKJWVTIAQNOHELEMWGKJHKPNJVSRVHAUFXBUOU
XOWCZJYQLXJRUOOYSKDLDXKWTTJBYBTLKSWRUYPOYTPBGUJXBMRWNELBWADCSZDAEEFGPVRHNNLBFDDXNPDXLKQUSJAZDEUDBMBD
QIKYEKMVUHGGWZDKXFVQQNECZOAWCFUBHQMEPEPKEFSDBAYJQOSGAIHRBRAUKLQRANKMTTIOJDDXAEWTQHIYSGRRMEFTNNWCLZSI
ZFUQAQCSFNVUQMKUQWBWFQIEQVVXPOSVIDTUOBLLTGHQKEMSUWWHWRISLGRDPPQPZBANSGDWXKNYTKMWECPMPDYSCJZXPUKPWGYI
CNGVLBSCBHRLJARWSRENGHYYQDKRATERCPEAOPAJZUMOYIDHVPDMQPKKHCBAMRBGEIEXXJALMCXKPUGXYVINRORFYURXAMOJCBZQ
YJHHAWESCLMDIHVYMLAJZQSYTDEURWYPOLJCAKIKSATGVIALBLWPPKDEGSPMRLDBQNVPPCLQXKUQLQJERMYFGAETUATEBQZUMGUN
NBWUBVXYDFPLPJYLIDFVTVKKGFWMXVINLJUDUPABTSBJAJENZSXIMUJQWPEZTAVDMBBHFYTJKYFXIXQTBTTQIKQXQDPWYNMXRQDJ
OGWLZQUBJJHAQNPVRGHGPNMMJPIDGANYEEDWYPOLKLNEPYSRTQYCJLSWFRJRRGGSNSDHIXYYSNAKKBWQDDGYYMOGPUXQEUSAPSOU
CLLSELRVFZUFYVTJQKCQHNICMERWQFQNPVRPIIYKHZWJYJAFCLNSZXUHSPOZWQUMJHLKKYJENVZOCSWCTPYWIZONUUCLSUROGAYS
AZGNIMXPLPCEPULRRBHHQOBELHJZPUQAMWUASVKDXVEWAOFMAYSJFXHCNEUXUQWUESFBRUFZQLKKWHCHKOPLECCBYSLECAEZIMMI
TUUEOCEBAUKWLTSYJJPLZTIARAOZXKYYWIOXBBTZZCSAULKNEJWVQXIKUWBIWVHGNTHVBAWAVPGLHSDJDLPVHHHUNVSFKXARXLVQ
EMVDFSLANQIAOPTLFLFRKGNUZCTXWCAXHECTZFHWUFENRGQICHTYLSHZWIEGLNVDJZOMTKAAUWOHVOVOCTUKOSINSAYIAEUYORNA
VGPRMLCAQZIPRFQOZMEFTQZYVOTVFNVOIQSJCIPPQXQKJIXICUIGMHAJJMSXENCBQFIJHNZXIQMWACKDKQSEWWKMLOAUPFHAZGRY
SQWQMRSQBGGKYKGWEZYRIHWGNXRPOUMFSFGTYDLUDWPWAVQORTMQUXWKUQVNMDPWQFIZPOIHCJATODRQGZDMQXZVNXXVEJNGWZOM
PVBGZSQPCELDIWDHOQWAUHILGLPYRIICTLFSOYKQZYZOCIZPTECSWOODGGBDTSGIMYGMVPJPRPEVWOOKYFWRGXHWUCRQNYJEMSYL
XWOFXFVDXPTHYTCEGMODCILAHYBREZVVHOUPZKCNHUEVPMKHUBNRPFMWXVQACVZCALZLYMZSBLCEASPMIEFOTGKMPGWYQADSNDPR
QPHAVLZDZLKIEISFLLVWXAVBZLZIJRHGROUVGXRDLUJAXNHBBZYNCVERJGSKLWZEKGJBCWMSMLYIHZFFMIOGVIMZQBSRHQWAADYN
MNXEGTDXCDKIUDOISQXEUJWETPELKBCYFSDNJQWNNBPYMWBUPQBAAINMYZOYCEGNLFNNHZFEMSQVXJJGWBCRAVKZFWFBKMBRVBFD
HKACSZIUWUXLWKFPKOCUQJEPQDZCMUJFLVCLIOQQRVKSWFIAKNHMRLNJTKGVNTGLCVPVMBLJANOBCXUGVWBJYSIXZQVAVFWILWFB
QWNLTPMCYHRSKVHXLONRANWKWXUTHYQLIOFKGDBMSWDRCYRKVSAGGRJMWQYQFLMUIGGCLAUQAACTYLPZEOJBHMWRKHCRXGTGRMUP
CPQKJRBLYDNPUGHCRBVYBAIRVCAWLBWVWCMKNBIRKJOUGYQEBQRHDSTWXDIWGRVMLIJFBWHLHCDAAVUDLZSCGQNOUXVUIVIZZZMD
NMHGYPFUUDWKQGTAKKGCDFJFYJFNRZVXDPGZEAMWQVQZODKTXHIYFVKJSSAWVHYCUCZMLLBPXTILDYJQEMWDRUFKISOUVPUDTYPB
FDAQUBXHUJYTAYNWVIJNUSQDTQDEMUAPWXRYUWONTBDZCHZOUEGPMWEZTQWWSHAYOBWVTDIMZYNVNZKUHOFCQKPHJXWNRCGUJEKO
WSDAUGUTVWCVHEMOIRJJGTANUWTSAIXXEVZTBDHPGSRHHVWCDZVZYRJTLONIJVXEATHQXOUKBIGZONFRSZIOGWNTYAJYLQCGEOWY
'''
# (思路：使用暴力的解法，直接遍历所有的，找L开头的然后看它八个方向的字母，看是否合格，但似乎比答案少了几个，不知道是那里错了)
a1,b1,c1,d1,e1,f1,g1,h1=0,0,0,0,0,0,0,0

for i in range(len(l)):
    if l[i]=='L':
        # print(i)
        for k in range(len(l)):
            if l[k]=='O':
                # print(k)
                if (i+6)==k:
                    a=l[i:i+7]
                    if a=='LANQIAO':
                        a1+=1
                elif (i+600)==k:
                    b=l[i]+l[i+100]+l[i+200]+l[i+300]+l[i+400]+l[i+500]+l[i+600]
                    if b=='LANQIAO':
                        b1+=1
                elif (i+606)==k:
                    c=l[i]+l[i+101]+l[i+202]+l[i+303]+l[i+404]+l[i+505]+l[i+606]
                    if c=='LANQIAO':
                        c1+=1
                elif (i+99*6)==k:
                    d=l[i]+l[i+99]+l[i+99*2]+l[i+99*3]+l[i+99*4]+l[i+99*5]+l[i+99*6]
                    if d=='LANQIAO':
                        d1+=1
                elif (i-6)==k:
                    e=l[i-6:i+1]
                    if e=='OAIQNAL':
                        e1+=1
                elif (i-606)==k:
                    f=l[i]+l[i-101]+l[i-202]+l[i-303]+l[i-404]+l[i-505]+l[i-606]
                    if f=='LANQIAO':
                        f1+=1
                elif (i-600)==k:
                    g=l[i]+l[i-100]+l[i-200]+l[i-300]+l[i-400]+l[i-500]+l[i-600]
                    if g=='LANQIAO':
                        g1+=1
                elif (i-99*6)==k:
                    h=l[i]+l[i-99]+l[i-99*2]+l[i-99*3]+l[i-99*4]+l[i-99*5]+l[i-99*6]
                    if h=='LANQIAO':
                        h1+=1

print(a1+b1+c1+d1+e1+f1+g1+h1)