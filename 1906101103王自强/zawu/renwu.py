'''现有的100w条字符串数据的txt文
件，怎么用java语言创建数组用冒
泡法对它进行排序，并统计它的时
间'''
from datetime import datetime
def fun(ls):
    starttime=datetime.now()
    n=len(ls)
    k=0
    for j in range(n):
        for i in range(n - j - 1):
            l,m=len(ls[i]),len(ls[i+1])
            while ord(ls[i][k])==ord(ls[i + 1][k])and k<=l and k<=m:
                k+=1
            if ord(ls[i][k])<ord(ls[i + 1][k]):
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
    return ls
ls=['t', 'k', 'h', 'W', 'p', 'h', 'H', 'j', 'f', 'C', 's', 'C', 'e', 'V', 'G', 'm', 'n', 'b', 'M', 't', 'we', 'EG', 'DX', 'RN', 'TD', 'gk', 'nl', 'pE', 'WU', 'El', 'Js', 'uI', 'Qr', 'ke', 'un', 'Ek', 'GR', 'OB', 'JY', 'Xf', 'mAs', 'ACe', 'aoM', 'tkl', 'kXR', 'aFE', 'ixr', 'jTy', 'DrH', 'eSR', 'mZl', 'KXu', 'yZg', 'Ttg', 'bLC', 'Hce', 'Mco', 'ItI', 'nYs', 'TQX', 'CErJ', 'MuUH', 'gywk', 'iIkY', 'OdVk', 'ASnl', 'ONwU', 'IhwN', 'anLG', 'gDLL', 'cEgI', 'WLfx', 'RUEE', 'fKRp', 'UxtQ', 'QKqY', 'mIKd', 'IVVY', 'iTJe', 'kFry', 'geMtg', 'cZnYE', 'pDADc', 'Xjast', 'tXxhw', 'PpyRJ', 'bufWW', 'VYkrX', 'KrDsF', 'pMiNg', 'PKiRJ', 'tHLxp', 'QQHkl', 'xuoRP', 'ipOSQ', 'LmyOA', 'teJzs', 'Mvzdu', 'gLfHK', 'huurg', 'nwmjqE', 'HHIAuK', 'TgrssP', 'lEGmpN', 'JvKAfT', 'mlQoEh', 'BeoIfH', 'BOGUij', 'hpUCxX', 'EFqYJY', 'uHeOHk', 'eannYQ', 'QwmOwR', 'rRYLdp', 'VdtPnK', 'ULtLiR', 'ZWMSJd', 'yPrzQt', 'BFhWyq', 'tBINHg', 'qIwoAzn', 'xTfDDyg', 'YSstteZ', 'GdrmUNx', 'rIdGUTu', 'apzofsi', 'FLDzIsU', 'oSIIFQD', 'fbZRRcZ', 'jdPgXiT', 'MBULJNy', 'QSPRYEW', 'CHrNXOs', 'SfZIjaP', 'kUPsMPU', 'MiiJwHc', 'TfXBmMP', 'YnVcppz', 'hWUBeqw', 'UQBBejf', 'RWVEOusR', 'TrtIoaGv', 'AVlIpMFP', 'tARMxsqn', 'hPvSLPsp', 'GHBnKhzH', 'RqEVrGCb', 'zgQLFqnZ', 'mIJOKOyd', 'JonyhUKb', 'zklxqilV', 'FngawKNt', 'aowSHbLa', 'WRshImlm', 'rAhiEfpK', 'wAkPZCYr', 'adbVQLXv', 'MdqpZoAL', 'UCFePcia', 'XGoNXeHx', 'VlzelAGbU', 'bRcXycmPQ', 'QeENwaMsp', 'dtDdUJdSd', 'acNqjvydr', 'cUGWzImlD', 'VAvxQJSAX', 'DzeAxrdCN', 'ndNYTtYHt', 'xfilqdwwz', 'cmwqsXLtv', 'uRPXxPaNo', 'NAOOHQXzp', 'lxivsTzky', 'tDOdNERpk', 'lXidyxXRd', 'MwPxXyyhi', 'nRORqbqPF', 'PPFkYHlxi', 'cruplCKcl']
ls1=fun(ls)
print(ls1)