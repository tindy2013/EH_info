# EH_INFO

## INTRO

是一个简简单单的小爬虫程序，只是用来方便获得e站漫画的信息的。

## USAGE

如果你也想使用，只需要下载 `main.py` 和 `requirements.txt` 即可。下载 `Python3.6+` 编译器然后在终端执行：

```bash
# 安装依赖
pip3 install -r requirements.txt
# 执行程序
python3 main.py -u 'https://example.com'
```

程序将会返回一个含有漫画基础信息的字典

## TODO

- [x] 爬取基本信息

- [ ] 爬取封面页

- [ ] 过滤TAG信息
