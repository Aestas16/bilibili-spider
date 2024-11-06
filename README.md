# bilibili-spider
直接调用 b 站旧 api（翻页 api）获取评论，但是限制最多 251 页。`main.py` 为该实现方案。

由于评论区是懒加载，requests 的爬虫方案较难实现，也许使用 selenium 会好一点。`main1.py` 为用 selenium ~~实现的半成品~~实现了一半感觉很麻烦，先不写了。

目前正在研究 b 站的新 api（懒加载 api）。

upd on 20241106：已实现懒加载 api 的评论爬取，代码在 `main2.py` 中。

但是感觉，251 页之后的评论，大概也不是高赞评论了吧（笑