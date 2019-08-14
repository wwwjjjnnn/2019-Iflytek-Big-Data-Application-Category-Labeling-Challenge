# Iflytek-Big-Data-Application-Category-Labeling-Challenge
2019 iFLYTEK 大数据应用分类标注挑战赛

队伍编号：人工执杖


赛事概要

一、赛题背景
对应用的精准分类不仅有利于应用的管理，还有诸多用途，如竞品分析、市场行情分析、应用监管及反作弊等，但如何进行精准分类一直是业界难题，不仅涉及数据爬取、数据清洗、机器学习等多项技术，不同应用领域关注的应用分类类别也不尽相同，导致了当前业界还是以人工标注为主获取准确的应用分类信息。


二、赛事任务
选手基于提供的应用二级分类标签以及若干随机应用标注样本（加密的应用名称和应用描述及对应的分类标签）实现应用分类标注算法（每个应用一个标签，以应用最主要属性对应的标签为该应用的标签）。


三、评审规则
1. 初赛

a. 选手自行下载验证集（加密的应用名称和应用描述）并进行应用分类标注，并将标注好的数据（加密的应用名称和应用分类）上传服务器计算准确率，准确率高者获胜；
b. 除了提供的应用描述外，不可使用其他数据源，需要选手通过算法进行应用分类标注；

2. 复赛

a. 选手自行下载验证集（应用名称及报名）并进行应用分类标注，并将标注好的数据（应用名称、包名、应用分类）上传服务器计算准确率，准确率高者获胜；
b. 样本数据额外提供应用的真实名称和包名，选手可以爬取任意的网络数据资源（比如应用商店里的应用分类及描述都可以爬取，且不限于此），需要选手通过选择优质数据源并实现算法进行应用分类标注；

3.	决赛

选手需提交参赛项目介绍PPT。包括：开发团队简介（必选），爬取了哪些网络数据（复赛必选），数据清洗逻辑（必选），算法实现详情（必选），技术架构（可选），代码是否有开源下载地址（可选）。文档命名【队伍名+参赛作品名】


四、作品提交要求
文件格式： 以csv格式提交，编码为UTF-8，第一行为表头；
文件大小：大小统一为10万行，每行长度固定；
提交次数限制：初赛和复赛期间每天最多可提交3次结果；
提交文件详细说明：
a. 初赛：
文件名称：pre_test_(提交次数).csv ，如pre_test_1.csv
字段说明：app名称(密文)，app分类标签1，app分类标签2
字段命名：id，label1，label2
b. 复赛：
文件名称: final_test_(提交次数).csv，如final_test_1.csv
字段说明：app名称(密文)，app分类标签1，app分类标签2
字段命名：id，label1，label2
提交次数选手自己依次递增,并非每天清零，分类标签1和标签2均可以为空，结果只要有一个正确即判定分类正确；
可点击左侧导航“赛题数据”，下载相应的提交示例文件


五、奖项设置&赛程规则
1. 初赛

1) 初赛截止成绩以团队在初赛时间段内最优成绩为准（不含测试排名）；
2) 初赛作品提交截止日期为８月20日17:00；初赛名次公布日期为8月21日10:00；

2. 复赛

1) 排名前20%的团队晋级复赛，大赛官网将公示团队信息。选手通过大赛官网下载新增的训练集和开发集，本地调试算法，在线提交结果；
2) 复赛成绩以参赛团队在复赛时间段内最优成绩为准；
3) 复赛作品提交截止日期为９月20日17:00；复赛名次公布日期为９月21日10:00；

3.	决赛

1) 前三名团队将受邀参加科大讯飞全球1024开发者节并于现场进行决赛；
2) 决赛以答辩（10min陈述+5min问答）的形式进行；
根据复赛成绩和答辩成绩综合评分（复赛成绩占比70%，现场答辩分数占比30%）。
3) 各赛道TOP10选手将阶梯获得赛道奖金，第一名3万元、第二名2万元、第三名1万元、第四-第十名分别获得“算法菁英奖”2500元；

其他奖项

除对应奖金外，入围复赛的团队将获得定制Geek礼包、大赛入围证书、定制文化衫及科大讯飞全球1024开发者节通票等福利。




问题：

一、如何处理类别不平衡问题？【如类别为 ['140110', '140805', '140105'] 的数据一共有8条记录】
    
    1、可以另外添加特征列, 为大的类别, 特征值可以是对应的大类别下的小类别, 在文本中出现的次数
    2、归一化 
    3、对于Ridge没有提升
    
   
二、对于训练集中一条数据对应有两个类别的如何处理？
    1、可以进行拆分，拆成两条记录，对应两个不同的类别编号。  （提升0.2个百分点）


三、音乐对应 140208 与 140603？


四、如何考虑到大类别和小类别的关系？
    1、尝试看看 如果模型预测的排前的两个类别属于同一个大类别，则剃掉第二个，然后用排名第二的大类别对应的类别进行替换。
        【比如排名为 140110 140111 140805 则选取 140110 140805】  
        
五、词向量