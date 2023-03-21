# steam统计数据

import urllib.request, re, time

'''
headers=("User-Agent", "Mozilla/5.0 (Linux; <Android Version>; <Build Tag etc.>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev>")
my_opener=urllib.request.build_opener()
my_opener.addheaders=[headers]
#安装opener到全局
urllib.request.install_opener(my_opener)
'''

# 从网站获取数据
data = urllib.request.urlopen('https://store.steampowered.com/stats/').read().decode("utf-8","ignore")
game_name_pat = '<a class="gameLink".*?>(.*?)</a>'
current_servers_pat = '<span class="currentServers">(.*?)</span>'
# 数据处理
rst = re.compile(game_name_pat).findall(data)  # 取得游戏名
numrst = re.compile(current_servers_pat).findall(data)  # 取得数值
# date = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())  # 设置时间
date = time.strftime("%Y/%m/%d %H", time.localtime())
num = 0  # 控制记录20条
print(date+"--正在记录数据")
for i in range(0, len(rst)):
    try:
        # print(rst[i]+ "," + "Game" + "," + numrst[2*i].replace(",","") + "," + date)
        fh = open("examplehour.csv","a+")
        fh.write(rst[i]+ "," + numrst[2*i+1].replace(",","") + "," + numrst[2*i].replace(",","") + "," + date + ":00\n")
        fh.close()
        num+=1
    except Exception as e:
        print(e)
    if(num>=20):
        break

# urllib.request.urlretrieve("https://store.steampowered.com/stats/","data.html")


