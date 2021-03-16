## 一、简介

该仓库存储了一些日常学习中的使用的代码，包括但不限于算法、ML、NLP、DL、知识图谱、工具研发等，开发语言为python，有直接可运行的python文件，也有jupyter notebook文件，大家随意品尝，不吝赐教。由于个人认为项目规模、实用性不大的项目，暂时没有独立出去，后续应该会有独立出去的计划。

## 二、文件介绍

* [utils/file_tool.py](https://github.com/CAKGOD/myCode/blob/master/utils/file_tool.py)

  包括一些使用os模块进行一些文件、路径等操作的函数。

* [utils/knowledge_graph.py](https://github.com/CAKGOD/myCode/blob/master/utils/knowledge_graph.py)

  包括一些使用networkx进行图谱节点、关系提取的函数，以及图谱存储读取的函数。

* [utils/nlp.py](https://github.com/CAKGOD/myCode/blob/master/utils/nlp.py)

  手动实现tf-idf（待完善）

* [utils/rust_tool.py](https://github.com/CAKGOD/myCode/blob/master/utils/rust_tool.py)

  进行rust洞察时使用到的函数。

* [utils/scraper.py](https://github.com/CAKGOD/myCode/blob/master/utils/scraper.py)

  * 基本的爬虫访问读取
  * 调用github api进行爬取
  * 调用crates.io进行爬取
  * 爬取github页面并解析
  * 提取github项目贡献者排名（半衰期）
  * 多进程爬取
  * 等等

* [examples/dash-pivottable](https://github.com/CAKGOD/myCode/tree/master/examples/dash-pivottable)

  开源智能装备舆情监控项目，爬取美国智库列表，进行关键词提取，并根据每日提及数量进行触发监控。监控结果通过plotly进行图标绘制，生成前端页面并部署到云服务器上，可以访问http://119.23.223.90:8000/查看效果。

* [examples/github](https://github.com/CAKGOD/myCode/tree/master/examples/github)

  爬取github个人主页和项目主页，下载仓库使用git命令进行commit信息提取，构造用户和项目画像。

* [examples/knowledge_graph](https://github.com/CAKGOD/myCode/tree/master/examples/knowledge_graph)

  该项目中包括多个知识图谱小项目，主要用来巩固知识图谱的相关知识。

  * facebook用户图谱
  * 标签传播算法实现
  * 阳光保险车保知识图谱
  * rust贡献者github follow图谱

* [examples/machine_learning](https://github.com/CAKGOD/myCode/tree/master/examples/machine_learning)

  * GBDT
  * LightGBM
  * XGBoost
  * ridge

* [examples/nlp](https://github.com/CAKGOD/myCode/tree/master/examples/nlp)

  * HMM
  * LDA
  * word2vec
  * 分词
  * 文本分类
  * tfidf
  * 诛仙续写
  * 文本向量化

* [examples/resume](https://github.com/CAKGOD/myCode/tree/master/examples/resume)

  该处项目理性食用

  * 51job
  * lagou
  * boss

* [examples/text_summary_and_resoning](https://github.com/CAKGOD/myCode/tree/master/examples/text_summary_and_reasoning)

  汽车大师文本摘要和推理

* [examples/zulip](https://github.com/CAKGOD/myCode/tree/master/examples/zulip)

  zulip聊天记录爬取

