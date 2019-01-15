from bs4 import BeautifulSoup
import requests
import re


def szpt_worm():
    content = requests.get('http://www.szpt.edu.cn', proxies={'http': 'http://proxy.xxx.com:8080'}).content
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.title)  # 第一个title标签
    print(soup.title.name)  # 第一个 title 标签的标签名称
    print(soup.title.string)  # 第一个 title 标签的包含内容
    print(soup.title.parent.name) # 第一个 title 标签的父标签的标签名称
    print(soup.div) # 第一个div标签
    print(soup.div['id']) # 第一个div标签的id属性内容
    soup.div['href'] = 'http://www.baidu.com/' # 为第一个div标签添加href属性
    soup.div['name'] = 'first_div'  # 为第一个div标签添加name属性
    soup.div['name'] = 'first_div_mod' # 修改第一个div标签的name属性
    soup.div['class'] = 'testClass'  # 为第一个div标签添加class属性
    del soup.div['class'] # 删除第一个div标签的class属性
    print(soup.div.contents) # 第一个div标签的所有子节点
    print(soup.find_all('img')) # 所有img标签，以list形式显示
    print(soup.find('div',attrs={'class':'news2'})) # 第一个class等于news2的div标签
    print(soup.find_all('div', attrs={'class': 'news2'}))  # 所有class等于news2的div标签
    print(soup.get_text()) # 获取所有文字内容
    print(soup.div.attrs) # 第一个div标签的所有属性信息
    for img in soup.find_all('img'):
        print(img.get('src'))
        # 遍历所有img标签，循环输出所有标签的src属性

    for child in soup.div.children:
        print(child) #遍历输入第一个div标签的所有子节点

    for tag in soup.find_all(re.compile('b')):
        print(tag.name)
        # 遍历所有标签名带有‘b’的标签并输出他们的标签名


if __name__ == '__main__':
    szpt_worm()
