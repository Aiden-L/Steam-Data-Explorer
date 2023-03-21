# steam统计数据

import re
import time
import urllib.request

# 从网站获取数据
data = urllib.request.urlopen('https://store.steampowered.com/stats/').read().decode("utf-8", "ignore")
game_name_pat = '<a class="gameLink".*?>(.*?)</a>'
current_servers_pat = '<span class="currentServers">(.*?)</span>'
# 数据处理
rst = re.compile(game_name_pat).findall(data)  # 取得游戏名
num_rst = re.compile(current_servers_pat).findall(data)  # 取得数值
date = time.strftime("%Y/%m/%d", time.localtime())  # 设置时间
num = 0  # 控制记录20条

print(date+"--正在记录数据")

for i in range(0, len(rst)):
    try:
        print(rst[i]+ "," + "Game" + "," + num_rst[2*i].replace(",","") + "," + date)
        fh = open("./example_day.csv", "a+")
        fh.write(rst[i] + "," + "Game" + "," + num_rst[2 * i + 1].replace(",", "") + "," + date + "\n")
        fh.close()
        num += 1
    except Exception as e:
        print(e)
    if num >= 20:
        break
