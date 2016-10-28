
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
sns.set_style('whitegrid') 

import warnings
warnings.filterwarnings('ignore')


# In[3]:

bid = pd.read_stata('../論文csv/0722競標紀錄.dta',encoding='utf-8')
mer = pd.read_stata('../論文csv/0722商品資訊.dta',encoding='utf-8')


# In[4]:

def bid_counts(bid,mer):
    # 競標內下標次數
    bid_tp1 = bid.copy()
    bid_tp1['bids_in_auction'] = bid_tp1.groupby(['mer_id','name'])['bid_price'].transform('count')
    
    # 競標內自動下標次數
    bid_tp1['auto_tp'] = '自動'
    bid_tp1['auto_dummy'] = 0
    bid_tp1['auto_dummy'][bid_tp1['auto'] == bid_tp1['auto_tp']] = 1
    bid_tp1['auto_in_auction'] = bid_tp1.groupby(['mer_id','name'])['auto_dummy'].transform('sum')
    
    # 與商品資訊合併
    bid_tp2 = bid_tp1[['mer_id','name','bids_in_auction','auto_in_auction']]
    bid_merge = bid_tp2.drop_duplicates(subset=['mer_id','name'])
    data = pd.merge(mer,bid_merge,on='mer_id',how='outer')
    
    data = data[data.mer_id <= 18212]
    data = data.drop(data.columns[0], axis=1)
    
    return data


# In[5]:

def data_process(data_1): 
    # 計算競標利潤
    data_1.loc[:,'auction_profit'] = 0
    data_1['auction_profit'][data_1['winner'] == data_1['name']] = data_1['suggested_price'] - data_1['bids_in_auction']*25 - data_1['final_price'] -100
    data_1['auction_profit'][data['winner'] != data_1['name']] = - data_1['bids_in_auction']*25
    
    # 96,93折
    data_1['auction_profit96'] = data_1['auction_profit']
    data_1['auction_profit96'][(data_1['winner'] == data_1['name'])] = data_1['suggested_price'] - data_1['bids_in_auction']*24 - data_1['final_price'] -100
    data_1['auction_profit96'][(data_1['winner'] != data_1['name'])] = - data_1['bids_in_auction']*25*0.96   # (data_1['diff_type'] != 1

    data_1['auction_profit93'] = data_1['auction_profit']
    data_1['auction_profit93'][(data_1['winner'] == data_1['name'])] = data_1['suggested_price'] - data_1['bids_in_auction']*23.25 - data_1['final_price'] -100
    data_1['auction_profit93'][(data_1['winner'] != data_1['name'])] = - data_1['bids_in_auction']*25*0.93
    
    # 持續期間
    data_1['max'] = data_1.groupby('name')['date'].transform('max')
    data_1['min'] = data_1.groupby('name')['date'].transform('min')
    data_1['max'] = pd.to_datetime(data_1['max'])
    data_1['min'] = pd.to_datetime(data_1['min'])
    data_1['duration'] = (data_1['max']-data_1['min']) / np.timedelta64(1, 'D')
    data_1['int_duration'] = data_1['duration'] + 1
    
    return data_1     


# In[6]:

def personal_info(data_1): 
    #只取正規競標
    data_person = data_1.copy()
    data_person = data_person[data_person.new > 0]

    # 個人贏得次數
    data_person['win_dummy'] = 0
    data_person['win_dummy'][data_person['winner'] == data_person['name']] = 1
    data_person['win_number'] = data_person.groupby('name')['win_dummy'].transform('sum')

    data_person = data_person.drop_duplicates(subset=['mer_id','name'])
    data_person['total_profit'] = data_person.groupby('name')['auction_profit'].transform('sum')
    data_person['total_profit96'] = data_person.groupby('name')['auction_profit96'].transform('sum')
    data_person['total_profit93'] = data_person.groupby('name')['auction_profit93'].transform('sum')

    data_person['totalreg_auctions'] = data_person.groupby('name')['mer_id'].transform('count')
    data_person['totalreg_bids'] =  data_person.groupby('name')['bids_in_auction'].transform('sum')
    
    data_person2 = data_person.drop_duplicates(subset='name')
    data_person2 = data_person2[['name','total_profit','total_profit96','total_profit93','totalreg_auctions','totalreg_bids','win_number']]
    person = data_person2.dropna()
    
    return person


# In[7]:

def save_check(data):
    # 檢查一下 save 與 profit 是否相同
    data_check = data[data['winner'] == data['name']]
    data_check['check'] = data_check['save'] - data_check['auction_profit']
    data_wonder = data_check[(data_check['check'] != 0) & (data_check['save'] > 0)]
      
    return data_wonder


# In[8]:

def profit_dist(person):
    # 競標利潤分配
    reg_profit_quan = person['total_profit'].quantile([.01,.1,.3,.5,.7,.9,.99,])
    reg_profit_quan96 = person['total_profit96'].quantile([.01,.1,.3,.5,.7,.9,.99,])
    reg_profit_quan93 = person['total_profit93'].quantile([.01,.1,.3,.5,.7,.9,.99,])
    
    table = reg_profit_quan.to_frame()
    table = table.join(reg_profit_quan96)
    profit_table = table.join(reg_profit_quan93)
    
    return profit_table


# In[9]:

def stat_descibe(data_1):
    data2 = data_1.copy()
    data2 = data2.dropna()
    
    # 三項指標
    data2['auction'] = data2.groupby('name')['mer_id'].transform('count')
    data2['bids'] = data2.groupby('name')['bids_in_auction'].transform('sum')   
    data3 = data2.drop_duplicates(subset='name')
    
    auction = data3['auction'].quantile([.5,.75,.9,.95,.99])
    bids = data3['bids'].quantile([.5,.75,.9,.95,.99])
    duration = data3['int_duration'].quantile([.5,.75,.9,.95,.99])
    
    table2 = auction.to_frame()
    table2 = table2.join(bids)
    stat_table = table2.join(duration)
    
    return stat_table


# In[10]:

def threegroup(x):
    if x <= 12:
        return 'fleet'
    if 12 < x < 42:
        return 'moderate'
    if x > 41:
        return 'persist'

def make_three_group(person):
    # 將玩家分成三群
    person['totalreg_auctions'] = person['totalreg_auctions'].astype(int)
    person['three_group'] = person['totalreg_auctions'].apply(threegroup)    
    
    return person


# In[11]:

def three_group_stat(person):
    # 分群人數
    people = person.groupby('three_group')['name'].count()
    # 下標次數
    ttbids = person.groupby('three_group')['totalreg_bids'].sum()
    # 分群得標數
    ttwins = person.groupby('three_group')['win_number'].sum()
    # 分群利潤
    ttprofit = person.groupby('three_group')['total_profit'].sum()
    ttprofit96 = person.groupby('three_group')['total_profit96'].sum()
    ttprofit93 = person.groupby('three_group')['total_profit93'].sum()
    
    df = people.to_frame()
    df = df.join(ttbids)
    df = df.join(ttwins)
    df = df.join(ttprofit)
    df = df.join(ttprofit96)
    three_group_df = df.join(ttprofit93)
    
    three_group_df['pro_per_bid'] = three_group_df['total_profit'] / three_group_df['totalreg_bids']
    
    return three_group_df


# In[17]:

def strategy_variable(data_1):
    data = data_1.copy()
    data['autorate'] = data['auto_in_auction'] / data['bids_in_auction']
    data['bid_allplayer'] = data.groupby('mer_id')['bids_in_auction'].transform('sum')
    data['enough'] = data['bids_in_auction'] / data['bid_allplayer']
    data['person_autorate'] = data.groupby('name')['autorate'].transform('mean')
    data['person_enough'] = data.groupby('name')['enough'].transform('mean')
    
    data_merge = data[['name','person_autorate','person_enough']]
    data_merge = data_merge.drop_duplicates(subset='name')
    
    return data_merge


# In[12]:

data = bid_counts(bid,mer)
data_1 = data_process(data)
person = personal_info(data_1)
person = make_three_group(person)


# In[14]:

profit_table = profit_dist(person)
profit_table


# In[15]:

stat_table = stat_descibe(data_1)
stat_table


# In[16]:

three_group_df = three_group_stat(person)
three_group_df


# In[21]:

data_merge = strategy_variable(data_1)
strategy_df = pd.merge(person,data_merge,on='name',how='outer')
strategy_df = strategy_df.dropna() #去除無正規競標的人


# In[23]:

strategy_df.groupby('three_group')['person_autorate'].mean()


# In[24]:

strategy_df.groupby('three_group')['person_enough'].mean()


# In[ ]:




# In[ ]:

data_1.to_csv('../論文csv/0722競標整理.csv',encoding='utf-8')
person.to_csv('../論文csv/0723個人整理.csv',encoding='utf-8')


# In[ ]:



