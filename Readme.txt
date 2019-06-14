#文件包含4个python包
    1.第一个python包sourcedata，包含原始数据(b6bce3abb838406daea9af48bf059c633.txt)，对于原始数据的预处理python文件（preprocess.py），
以及产生的用于第三个问题的用户余额文件(xdata)。
    2.第二个python包firstquestion，是针对第一个问题，包含一个预处理文件（dataprocess.py)，以及其产生的两个统计数据文件（perdayISIR.csv），
（perdayQRTA.csv）。还有两个模型训练的文件（isirtrain.py），（qrtatrain.py），其产生最终结果。
    3.第三个python包secondquestion，是针对第二个问题，包含一个预处理文件（preprocess.py)，以及其产生的一个统计数据文件（perdayvolume.csv）。
还有一个个模型训练的文件（volumetrain.py）其产生最终结果。
    4.第四个python包(thirdquestion)，是针对第三个问题，包含五个模型训练文件：
第一个模型（sta_validation.py）利用prophet框架，规定了验证集进行验证的实验模型，调节各种参数；
第二个模型（sta_pro_withlimit.py）利用prophet框架，对其未来预测的上下界进行限定；
第三个模型（sta_pro_without_limit.py）利用prophet框架，对其未来预测的上下界不进行限定；
第四个模型（sta_pro_withyear.py）利用prophet框架，加入以年为周期的趋势因素；
第五个模型（sta_xiangxingtu.py）利用箱型图原理对数据进行预处理，然后带入prophet框架，减少异常值的影响。

说明：
    1.针对第三个问题，每个模型都有自己的特点，单个模型所能到达的效果都不如人意，如何选择是关键。
对用户余额的变化趋势画图可以看到，用户之间的行为习惯差异巨大，周期不明显，用户之间几乎没有联系，无法用一个单一的模型对所有用户预测，都得到
一个很好的预测效果。所以针对以上问题，我采用先初选出部分可能性高的用户（60个左右），然后对每个用户单独调参，即一个用户，一个单独的模型，
进行调参，然后得到结果。因为用户比较多，所以没有保存所有参数。只给出了各个基本模型。
    2.我将逐个用户调参得到的结果写入（beixuandata.csv）中的b列(a列是用第二个单模型注释掉的代码跑出来的结果，效果并不好)。然后排序输出对应用户名。
    2.由于版本管理的问题，个别代码不是最优成绩代码，望谅解。


