tg_upload.py文件用于上传大量本地小说文件至tg群，其他类型文件如视频音乐的没有尝试过。

流程是将本地文件的书名，作者，网站，书的路径记录到json文件里，再根据json文件上传至tg，并添加标签，如果上传失败的话会记录到新的json文件里，再手动更改代码上传

使用的话需要赋值paths()里的path，mk_json(object)里的json_path，rd_json()里的json_path，upload_novel()里的PROXY_URL，CHAT_ID，BOT_TOKEN，json_file_path，fail_json_path

chatid和bottoken谷歌搜索就有

因为我的本地文件是按书库——首发网站——作者——小说这样的结构保存，如zxcs\豆瓣\雨楼清歌\天下刀宗.rar,在写入json文件里面没有使用适合其他文件结构的代码，有需求的可自行更改（我也不会，想不出是哪个函数能自动读取所有文件）

总的来说还是太菜了，没能写出一键上传的代码，要手工更改的地方比较多
