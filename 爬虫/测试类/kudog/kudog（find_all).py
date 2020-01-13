import requests
from bs4 import BeautifulSoup
import time
import datetime
import csv
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
    return ""



def get_infos(html,length):
    '''
    提取数据
    '''
    html = BeautifulSoup(html,'lxml')
    # 排名
    ranks = html.find_all('span',class_='pc_temp_num')
    # 歌手 + 歌名
    names = html.find_all('a',class_='pc_temp_songname')
    # 播放时间
    times = html.find_all('span',class_='pc_temp_time')

    # 打印信息
    la=[]
    for r,n,t in zip(ranks,names,times):
        r = r.get_text().replace('\n','').replace('\t','').replace('\r','')
        n = n.get_text()
        t = t.get_text().replace('\n','').replace('\t','').replace('\r','')
        la.append([r,n,t])
        data = {
            '排名': r,
            '歌名-歌手': n,
            '播放时间': t
        }
        print(data)

    file = r'E:\Python包\爬虫\测试类\kudog.csv'
    title = ["排名", "歌手-歌手", "播放时间"]
    with open(file, 'a', encoding="utf_8_sig") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(title)
        for i in range(22):
            e=la[i]
            csvwriter.writerow(e)


def main():
    '''主接口'''
    # urls=r'https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i) for i in range(1,3))
    # for url in urls:
    #     html=getHTMLText(url)
    #     get_infos(html)
    #     # time.sleep(1)
    start=datetime.datetime.now()
    length = 10
    for i in range(1,length):
        url = r'https://www.kugou.com/yy/rank/home/'+str(i)+'-8888.html?from=rank'
        html = getHTMLText(url)
        get_infos(html,length)

    end=datetime.datetime.now()
    print('爬取的时间是：{}'.format((end-start)))

if __name__ == '__main__':
    main()