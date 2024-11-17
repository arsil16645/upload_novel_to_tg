import json
import os
from telegram import Bot
from telegram.ext import Application
import asyncio
import aiohttp


#建立书对象，将其添加进列表，以便写入json
#class book():
#    def __init__(self,name,author,web,path):
#        self.name=name
#        self.author=author
#        self.web=web
#        self.path=path

def paths():
    path='D:\\zxcs'
    li=[]
    paths=os.listdir(path)#全部web名字
    for web_name in paths:
        web_path=os.path.join(path,web_name)#web地址
        authors=os.listdir(web_path)#全部作者名字
        for author_name in authors:
            author_path=os.path.join(web_path,author_name)#作者地址
            books=os.listdir(author_path)#全部书名字
            for book_name in books:
                book_path=os.path.join(author_path,book_name)
                dit = {'name': 0, 'author': 0, 'web': 0, 'path': 0}
                dit['name']=book_name
                dit['author'] =author_name
                dit['web'] =web_name
                dit['path'] =book_path
                li.append(dit)
    mk_json(li)#写入文件

#    rd_json()#读取json文件

#建立json文件
def mk_json(object):
    json_path=''#要保存文件的位置
    if json_path==None:
        os.mkdir(json_path)
    with open(json_path,'w',encoding='utf-8') as f:
        json.dump(object,f,ensure_ascii=False, indent=4)

#读取json文件
#def rd_json():
#    json_path = ''
#    with open(json_path,'r',encoding='utf-8') as f:
#            novel=json.load(f)
#     for i in novel:
#         print(i)

#根据json上传文件
async def upload_novel():
    PROXY_URL = ''
    CHAT_ID = ''
    BOT_TOKEN = ''

    connector = aiohttp.TCPConnector(ssl=False)
    session = aiohttp.ClientSession(connector=connector)

    # 初始化 Application 并启用代理
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .proxy(PROXY_URL)  # 设置 SOCKS5 代理
        .build()
    )
    bot = application.bot

    # 读取 JSON 文件
    json_file_path = ''
    with open(json_file_path, 'r', encoding='utf-8') as f:
        books = json.load(f)

    # 遍历 JSON 文件中的书籍信息并上传
    for book in books:
        name = book["name"]
        author = book["author"]
        web = book["web"]
        path = book["path"]

        try:
            # 上传文件
            await bot.send_document(
                chat_id=CHAT_ID,
                document=open(path, 'rb'),
                caption=f"#{name}\n #{author}\n #{web}"
            )
            print(f"上传成功: {name}")
        except Exception as e:
            print(f"上传失败: {name}, 错误: {e}")

            #当上传报错时便写入新的json文件，以便重新上传
            fail_json_path = ''
            if fail_json_path == None:
                os.mkdir(fail_json_path)
            with open(fail_json_path, 'a', encoding='utf-8') as f:
                json.dump(book, f, ensure_ascii=False, indent=4)

    await session.close()


if __name__=="__main__":
    paths()
    asyncio.run(upload_novel())