# -*- coding: utf-8 -*-  
import re,time,requests,urllib.request,pymysql

# weibo_id = input('输入单条微博ID：')
weibo_id = '4198945548742549'
url='https://m.weibo.cn/single/rcList?format=cards&id=' + weibo_id + '&type=comment&hot=1&page={}' #爬热门评论
# url='https://m.weibo.cn/api/comments/show?id=' + weibo_id + '&page={}' #爬时间排序评论
headers = {
    'User-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Host' : 'm.weibo.cn',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Referer' : 'https://m.weibo.cn/status/' + weibo_id,
    'Cookie' : 'Login cookie session',
    'DNT' : '1',
    'Connection' : 'keep-alive',
    }
i = 1
comment_num = 1
conn =pymysql.connect(host='127.0.0.1',user='root',password='',charset="utf8",use_unicode = False)    #连接服务器
cur = conn.cursor()
while i == 1:
    if i==1:     #爬热门评论
        r = requests.get(url = url.format(i),headers = headers)
        comment_page = r.json()[1]['card_group']
    else:
        r = requests.get(url = url.format(i),headers = headers)
        comment_page = r.json()[0]['card_group']
    # r = requests.get(url = url.format(i),headers = headers)  #爬时间排序评论
    # comment_page = r.json()['data']
    # comment_page = comment_page['data']
    if r.status_code ==200:
        try:
            print('正在读取第 %s 页评论：' % i)
            for j in range(0,len(comment_page)):
                print('第 %s 条评论' % comment_num)
                user = comment_page[j]
                comment_id = user['user']['id']
                print(comment_id)
                user_name = user['user']['screen_name']
                print(user_name)
                created_at = user['created_at']
                print(created_at)
                text = re.sub('<.*?>|回复<.*?>:|[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]','',user['text'])
                print(text)
                likenum = user['like_counts']
                print(likenum)
                source = re.sub('[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]','',user['source'])
                print(source + '\r\n')
                sql = "insert into sinaweibo.macomment(comment_id,user_name,created_at,text,likenum,source) values(%s,%s,%s,%s,%s,%s)" #格式是：数据名.表名(域名)
                param = (j,user_name,created_at,text,likenum,source)
                try:
                    A = cur.execute(sql,param)
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()
                comment_num+=1
            i+=1
            time.sleep(3)
        except:
            i+1
            pass
    else:
        conn.close()
        break
conn.close()