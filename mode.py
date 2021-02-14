# 正式编写程序
import random
import akshare as ak

# class get_data():

#     def __init__(self):

#     def 

def list_randomNum(num):
    # 生成num个介于0-1425个不重复的整数

    return random.sample(range(0,1485),num)



def sampling(randomNum,m,n):
    # 抽取固定跨度为m，共n个数据点，组成dataframe
    # m为时间跨度一般为22个工作日
    # n为周期数，取12个月
    list_index = list(range(randomNum,randomNum+m*(n-1)+1,30))
    pd_sampling = stock_zh_index_daily_df.iloc[list_index]
    pd_sampling['index_randomNum'] = randomNum                          #标记抽样样本
    pd_sampling['index_n'] = list(range(1,n+1))                         #标记样本内序号
    pd_sampling['avg']= pd_sampling.apply(lambda x: (x['high']+x['low'])* 0.5, axis=1)
    # pd_sampling['cost'] = 10 * pd_sampling['avg']

    return pd_sampling



def dif(df):
    revenue = []    #--收益
    rise = []       #--涨幅 %
    for i in range(0,len(df)):
        cost_all = sum(df['avg'].iloc[0:i])
        cost_now = df['avg'].iloc[i]*i
        revenue.append(cost_now - cost_all)
        rise.append((cost_now - cost_all) / cost_all * 100)

    df['revenue'] = revenue
    df['rise'] = rise



def proceeds(x)
