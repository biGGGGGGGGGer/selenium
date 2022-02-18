# 导入浏览器
import encodings
from tkinter import N
from xml.etree.ElementTree import Comment
from selenium.webdriver import Chrome
import time

# 账号密码
account = '15839109193'
password = '04056014.l'

# 滚动到浏览器顶部
js_top = "var q=document.documentElement.scrollTop=0"

# 创建浏览器
web = Chrome()
# 打开浏览器，请求到拉勾
web.get("https://www.douban.com/")

web.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[2]/a').click()
web.switch_to.window(web.window_handles[-1])
# 点击影评
web.find_element_by_xpath('//*[@id="db-nav-movie"]/div[2]/div/ul/li[6]/a').click()
# 输进去 《水门桥》
web.find_element_by_id('inp-query').send_keys('水门桥')
# 点击搜索
web.find_element_by_class_name("inp-btn").click()
# 点击第一个水门桥
web.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/a').click()
web.find_element_by_xpath('//*[@id="hot-comments"]/a').click()
# 点击 最新
web.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/div/a').click()

comment_items = web.find_elements_by_class_name('comment')

n = 1
for i in comment_items:
    comment_info = i.find_element_by_class_name('comment-info').text
    comment = i.find_element_by_class_name('short').text
    f = open(f'D:\python_workplace\爬拉钩\informations_{n}.txt',mode = 'w',encoding = 'utf-8')
    f.write(comment_info)
    f.write('\n')
    f.write(comment)
    f.close()
    n += 1

m = 40
while m != 0:
    web.find_element_by_xpath('//*[@id="paginator"]/a[3]').click()
    web.execute_script(js_top)
    time.sleep(1)
    comment_items = web.find_elements_by_class_name('comment')
    for a in comment_items:
        comment_info = a.find_element_by_class_name('comment-info').text
        comment = a.find_element_by_class_name('short').text
        f = open(f'D:\python_workplace\爬拉钩\informations_{n}.txt',mode = 'w',encoding = 'utf-8')
        f.write(comment_info)
        f.write('\n')
        f.write(comment)
        f.close()
        n += 1
    m -= 1







