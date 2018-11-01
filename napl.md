

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')
sns.set_style('whitegrid')
import warnings
warnings.filterwarnings('ignore')
```


```python
import numpy as np
```

- [1.语法示例](#1)
    - [1.1图片](#1.1)

#http://www.codedata.com.tw/database/mysql-tutorial-basic-query

pip install mysqlclient

import MySQLdb


    mydb = MySQLdb.connect(host='localhost',
        user='root',
        passwd='',
        db='mydb')
    cursor = mydb.cursor()


<h3 id="1">1.语法示例</h3>


```python
'''
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "192.168.1.2", user = "user", passwd = "password, db = "scripting_mysql")

# prepare a cursor object using cursor() method
cursor = connection.cursor ()

# execute the SQL query using execute() method.
cursor.execute ("select name_first, name_last from address")

# fetch all of the rows from the query
data = cursor.fetchall ()

# close the cursor object
cursor.close ()

# close the connection
connection.close ()
'''
```




    '\n# open a database connection\n# be sure to change the host IP address, username, password and database name to match your own\nconnection = MySQLdb.connect (host = "192.168.1.2", user = "user", passwd = "password, db = "scripting_mysql")\n\n# prepare a cursor object using cursor() method\ncursor = connection.cursor ()\n\n# execute the SQL query using execute() method.\ncursor.execute ("select name_first, name_last from address")\n\n# fetch all of the rows from the query\ndata = cursor.fetchall ()\n\n# close the cursor object\ncursor.close ()\n\n# close the connection\nconnection.close ()\n'



<h3 id="1.1">1.1图片</h3>

![pic](2018-10-30_222119.png)


```python
data = pd.read_csv('result資料.csv')
```


```python
data['ymd'] = pd.to_datetime(data['ymd'])
```


```python
data['first_ymd'] = data.groupby('billing_email')['ymd'].transform('min')
```


```python
before_2 = data.query('ymd <= "2016-02-28"')
before_3 = data.query('ymd <= "2016-03-31"')
before_4 = data.query('ymd <= "2016-04-30"')
before_5 = data.query('ymd <= "2016-05-31"')
before_6 = data.query('ymd <= "2016-06-30"')
```


```python
before_6.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>billing_address_1</th>
      <th>billing_email</th>
      <th>billing_last_name</th>
      <th>billing_phone</th>
      <th>billing_postcode</th>
      <th>cart_discount</th>
      <th>coupons</th>
      <th>customer_id</th>
      <th>date</th>
      <th>...</th>
      <th>month</th>
      <th>weekofyear</th>
      <th>dayofweek</th>
      <th>ymd</th>
      <th>time</th>
      <th>category</th>
      <th>merchant</th>
      <th>first_ymd</th>
      <th>new</th>
      <th>ym</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>新莊區中正路887之17號4樓</td>
      <td>ines88717@gmail.com</td>
      <td>陳美玲</td>
      <td>912419758</td>
      <td>242</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>2015-06-30 22:29:35</td>
      <td>...</td>
      <td>6</td>
      <td>27</td>
      <td>1</td>
      <td>2015-06-30</td>
      <td>22:29:35</td>
      <td>1211.0</td>
      <td>111.0</td>
      <td>2015-03-10</td>
      <td>old</td>
      <td>2015-06</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>新莊區中正路887之17號4樓</td>
      <td>ines88717@gmail.com</td>
      <td>陳美玲</td>
      <td>912419758</td>
      <td>242</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>2015-06-30 22:29:35</td>
      <td>...</td>
      <td>6</td>
      <td>27</td>
      <td>1</td>
      <td>2015-06-30</td>
      <td>22:29:35</td>
      <td>1211.0</td>
      <td>211.0</td>
      <td>2015-03-10</td>
      <td>old</td>
      <td>2015-06</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>台北市中正區羅斯福路一段6號12樓</td>
      <td>16659@ms.bli.gov.tw</td>
      <td>林宛蓁</td>
      <td>963144582</td>
      <td>100</td>
      <td>0</td>
      <td>NaN</td>
      <td>1498</td>
      <td>2015-06-30 19:10:37</td>
      <td>...</td>
      <td>6</td>
      <td>27</td>
      <td>1</td>
      <td>2015-06-30</td>
      <td>19:10:37</td>
      <td>52.0</td>
      <td>201506001.0</td>
      <td>2015-06-30</td>
      <td>new</td>
      <td>2015-06</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>礁溪鄉中山路一段190號5樓</td>
      <td>karen1125jam@gmail.com</td>
      <td>詹青蓉</td>
      <td>922681258</td>
      <td>262</td>
      <td>0</td>
      <td>NaN</td>
      <td>158</td>
      <td>2015-06-30 10:47:24</td>
      <td>...</td>
      <td>6</td>
      <td>27</td>
      <td>1</td>
      <td>2015-06-30</td>
      <td>10:47:24</td>
      <td>1212.0</td>
      <td>411.0</td>
      <td>2015-03-06</td>
      <td>old</td>
      <td>2015-06</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>新北市三重區進安街38號7樓</td>
      <td>ace0416@gmail.com</td>
      <td>蔡勳忠</td>
      <td>920900382</td>
      <td>241</td>
      <td>0</td>
      <td>NaN</td>
      <td>1020</td>
      <td>2015-06-30 09:46:19</td>
      <td>...</td>
      <td>6</td>
      <td>27</td>
      <td>1</td>
      <td>2015-06-30</td>
      <td>09:46:19</td>
      <td>1211.0</td>
      <td>211.0</td>
      <td>2015-02-26</td>
      <td>old</td>
      <td>2015-06</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 44 columns</p>
</div>




```python
before_6['new'] = 'old'
before_6['new'][before_6['ymd'] == before_6['first_ymd']] = 'new'
```


```python
before_6['ym'] = before_6['ymd'].astype(str).str[:7]
```


```python
temp = before_6.drop_duplicates(subset=['billing_email','ymd'])
new_old_n = temp.groupby(['new','ym'])['billing_email'].count().reset_index()
```


```python

```


```python
new_old_m = before_6.groupby(['new','ym'])['order_total'].sum().reset_index()
```


```python

```


```python
new_old_average = before_6.groupby(['new','ym'])['order_total'].mean().reset_index()
new_old_average = new_old_average.rename(columns = {'order_total':'average_order_money'})
```


```python
new_old_merge = new_old_n.merge(new_old_m, on=['new','ym'], how='inner')
```


```python
new_old_merge = new_old_merge.merge(new_old_average, on=['new','ym'], how='inner')
```


```python
new_old_merge.to_csv('new_old.csv')
```


```python
new_old_merge
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>new</th>
      <th>ym</th>
      <th>billing_email</th>
      <th>order_total</th>
      <th>average_order_money</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new</td>
      <td>2015-01</td>
      <td>140</td>
      <td>295059</td>
      <td>1130.494253</td>
    </tr>
    <tr>
      <th>1</th>
      <td>new</td>
      <td>2015-02</td>
      <td>109</td>
      <td>281412</td>
      <td>1359.478261</td>
    </tr>
    <tr>
      <th>2</th>
      <td>new</td>
      <td>2015-03</td>
      <td>144</td>
      <td>366061</td>
      <td>1365.899254</td>
    </tr>
    <tr>
      <th>3</th>
      <td>new</td>
      <td>2015-04</td>
      <td>148</td>
      <td>328350</td>
      <td>1225.186567</td>
    </tr>
    <tr>
      <th>4</th>
      <td>new</td>
      <td>2015-05</td>
      <td>218</td>
      <td>534372</td>
      <td>1377.247423</td>
    </tr>
    <tr>
      <th>5</th>
      <td>new</td>
      <td>2015-06</td>
      <td>105</td>
      <td>228708</td>
      <td>1284.876404</td>
    </tr>
    <tr>
      <th>6</th>
      <td>new</td>
      <td>2015-07</td>
      <td>117</td>
      <td>214236</td>
      <td>1133.523810</td>
    </tr>
    <tr>
      <th>7</th>
      <td>new</td>
      <td>2015-08</td>
      <td>154</td>
      <td>400651</td>
      <td>1376.807560</td>
    </tr>
    <tr>
      <th>8</th>
      <td>new</td>
      <td>2015-09</td>
      <td>299</td>
      <td>1358008</td>
      <td>2029.907324</td>
    </tr>
    <tr>
      <th>9</th>
      <td>new</td>
      <td>2015-10</td>
      <td>170</td>
      <td>364051</td>
      <td>1189.709150</td>
    </tr>
    <tr>
      <th>10</th>
      <td>new</td>
      <td>2015-11</td>
      <td>773</td>
      <td>1253455</td>
      <td>1245.979125</td>
    </tr>
    <tr>
      <th>11</th>
      <td>new</td>
      <td>2015-12</td>
      <td>1077</td>
      <td>2953457</td>
      <td>1745.541962</td>
    </tr>
    <tr>
      <th>12</th>
      <td>new</td>
      <td>2016-01</td>
      <td>453</td>
      <td>1067702</td>
      <td>1363.604087</td>
    </tr>
    <tr>
      <th>13</th>
      <td>new</td>
      <td>2016-02</td>
      <td>1326</td>
      <td>3056625</td>
      <td>1489.583333</td>
    </tr>
    <tr>
      <th>14</th>
      <td>new</td>
      <td>2016-03</td>
      <td>1539</td>
      <td>4239971</td>
      <td>1289.528893</td>
    </tr>
    <tr>
      <th>15</th>
      <td>new</td>
      <td>2016-04</td>
      <td>1087</td>
      <td>2626994</td>
      <td>1531.774927</td>
    </tr>
    <tr>
      <th>16</th>
      <td>new</td>
      <td>2016-05</td>
      <td>1155</td>
      <td>3476941</td>
      <td>1711.093012</td>
    </tr>
    <tr>
      <th>17</th>
      <td>new</td>
      <td>2016-06</td>
      <td>1027</td>
      <td>2247328</td>
      <td>1261.834924</td>
    </tr>
    <tr>
      <th>18</th>
      <td>old</td>
      <td>2015-01</td>
      <td>19</td>
      <td>48851</td>
      <td>775.412698</td>
    </tr>
    <tr>
      <th>19</th>
      <td>old</td>
      <td>2015-02</td>
      <td>47</td>
      <td>119828</td>
      <td>1198.280000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>old</td>
      <td>2015-03</td>
      <td>85</td>
      <td>175687</td>
      <td>987.005618</td>
    </tr>
    <tr>
      <th>21</th>
      <td>old</td>
      <td>2015-04</td>
      <td>71</td>
      <td>173622</td>
      <td>1105.872611</td>
    </tr>
    <tr>
      <th>22</th>
      <td>old</td>
      <td>2015-05</td>
      <td>128</td>
      <td>312016</td>
      <td>1130.492754</td>
    </tr>
    <tr>
      <th>23</th>
      <td>old</td>
      <td>2015-06</td>
      <td>111</td>
      <td>207898</td>
      <td>862.647303</td>
    </tr>
    <tr>
      <th>24</th>
      <td>old</td>
      <td>2015-07</td>
      <td>76</td>
      <td>144937</td>
      <td>1081.619403</td>
    </tr>
    <tr>
      <th>25</th>
      <td>old</td>
      <td>2015-08</td>
      <td>82</td>
      <td>219620</td>
      <td>1494.013605</td>
    </tr>
    <tr>
      <th>26</th>
      <td>old</td>
      <td>2015-09</td>
      <td>137</td>
      <td>565099</td>
      <td>1686.862687</td>
    </tr>
    <tr>
      <th>27</th>
      <td>old</td>
      <td>2015-10</td>
      <td>109</td>
      <td>298563</td>
      <td>1199.048193</td>
    </tr>
    <tr>
      <th>28</th>
      <td>old</td>
      <td>2015-11</td>
      <td>234</td>
      <td>531507</td>
      <td>1376.961140</td>
    </tr>
    <tr>
      <th>29</th>
      <td>old</td>
      <td>2015-12</td>
      <td>504</td>
      <td>1886959</td>
      <td>2046.593275</td>
    </tr>
    <tr>
      <th>30</th>
      <td>old</td>
      <td>2016-01</td>
      <td>297</td>
      <td>900200</td>
      <td>1468.515498</td>
    </tr>
    <tr>
      <th>31</th>
      <td>old</td>
      <td>2016-02</td>
      <td>576</td>
      <td>1459251</td>
      <td>1498.204312</td>
    </tr>
    <tr>
      <th>32</th>
      <td>old</td>
      <td>2016-03</td>
      <td>695</td>
      <td>2453507</td>
      <td>1328.374120</td>
    </tr>
    <tr>
      <th>33</th>
      <td>old</td>
      <td>2016-04</td>
      <td>735</td>
      <td>3045080</td>
      <td>2084.243669</td>
    </tr>
    <tr>
      <th>34</th>
      <td>old</td>
      <td>2016-05</td>
      <td>933</td>
      <td>4005083</td>
      <td>2080.562597</td>
    </tr>
    <tr>
      <th>35</th>
      <td>old</td>
      <td>2016-06</td>
      <td>701</td>
      <td>2184088</td>
      <td>1482.748133</td>
    </tr>
  </tbody>
</table>
</div>




```python
def GetRFM(data):
    nowday = pd.to_datetime(data['ymd'].max())

    data['lastdate'] = pd.to_datetime(data.groupby('billing_email')['ymd'].transform('max'))

    data['R'] = nowday - data['lastdate']
    data['R'] = data['R'].astype('str').str.split('d').str[0].astype(int)
    data['M'] = data.groupby('billing_email')['order_total'].transform('sum')
 
    dailydate = data.drop_duplicates(subset=['billing_email', 'ymd'])
    dailydate['F'] = dailydate.groupby('billing_email')['ymd'].transform('count')
    
    return dailydate
```


```python
def RepPeriod(data):
    repurchase = data.query('F > 1')
    repurchase = repurchase.sort_values(by=['billing_email', 'ymd'])
    repurchase['lastymd'] = repurchase.groupby('billing_email')['ymd'].shift().fillna(repurchase['ymd'])
    repurchase['repurchase_period'] = pd.to_datetime(repurchase['ymd']) - pd.to_datetime(repurchase['lastymd'])
    repurchase['repurchase_period'] = repurchase['repurchase_period'].astype('str').str.split('d').str[0].astype(int)
    
    RepPeriod = repurchase.query('repurchase_period > 0')
    return RepPeriod['repurchase_period'].mean() * 3
```


```python
def GetNAPL(data):
    data['Frequent'] = data['F'].apply(FreqType)
    data['napl'] = data.apply(lambda x: Grouped(x['R'], x['F']), axis=1)
    money = data.groupby(['napl'])['M'].sum()
    people = data.groupby(['napl'])['billing_email'].count()
    return (data, money, people)
```


```python
def FreqType(x):
    if x == 1:
        return '1'
    if x == 2:
        return '2'
    if x > 2:
        return '3 up'
```


```python
def Grouped(x, y):
    if y > 1:
        if x > 169:
            return 'potential'
        else:
            return 'active'
    else:
        if x > 169:
            return 'lost'
        else:
            return 'new'
```


```python
data2 = GetRFM(before_2)
data3 = GetRFM(before_3)
data4 = GetRFM(before_4)
data5 = GetRFM(before_5)
data6 = GetRFM(before_6)
```


```python
rep_mean = RepPeriod(data3)
print(int(rep_mean))
```

    169
    


```python
data2_unique = data2.drop_duplicates(subset='billing_email')
data3_unique = data3.drop_duplicates(subset='billing_email')
data4_unique = data4.drop_duplicates(subset='billing_email')
data5_unique = data5.drop_duplicates(subset='billing_email')
data6_unique = data6.drop_duplicates(subset='billing_email')
```


```python
data2, money2, people2 = GetNAPL(data2_unique)
data3, money3, people3 = GetNAPL(data3_unique)
data4, money4, people4 = GetNAPL(data4_unique)
data5, money5, people5 = GetNAPL(data5_unique)
data6, money6, people6 = GetNAPL(data6_unique)
```


```python
ymd = pd.Series(np.zeros(money2.shape[0]), name='ymd')
df = money2.to_frame().join(ymd).join(people2).reset_index()
df['ymd'] = '2016-02'
df['M_percentage'] = df['M'] / df['M'].sum() * 100
df['N_percentage'] = df['billing_email'] / df['billing_email'].sum() * 100
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>napl</th>
      <th>M</th>
      <th>ymd</th>
      <th>billing_email</th>
      <th>M_percentage</th>
      <th>N_percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>active</td>
      <td>9710486</td>
      <td>2016-02</td>
      <td>1150</td>
      <td>49.521052</td>
      <td>22.209347</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lost</td>
      <td>1417314</td>
      <td>2016-02</td>
      <td>666</td>
      <td>7.227947</td>
      <td>12.862109</td>
    </tr>
    <tr>
      <th>2</th>
      <td>new</td>
      <td>7568428</td>
      <td>2016-02</td>
      <td>3219</td>
      <td>38.597091</td>
      <td>62.166860</td>
    </tr>
    <tr>
      <th>3</th>
      <td>potential</td>
      <td>912576</td>
      <td>2016-02</td>
      <td>143</td>
      <td>4.653910</td>
      <td>2.761684</td>
    </tr>
  </tbody>
</table>
</div>




```python
tempdf = money6.to_frame().join(ymd).join(people6).reset_index()
tempdf['ymd'] = '2016-06'
tempdf['M_percentage'] = tempdf['M'] / tempdf['M'].sum() * 100
tempdf['N_percentage'] = tempdf['billing_email'] / tempdf['billing_email'].sum() * 100
tempdf
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>napl</th>
      <th>M</th>
      <th>ymd</th>
      <th>billing_email</th>
      <th>M_percentage</th>
      <th>N_percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>active</td>
      <td>23907603</td>
      <td>2016-06</td>
      <td>2336</td>
      <td>54.304388</td>
      <td>23.264615</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lost</td>
      <td>4718568</td>
      <td>2016-06</td>
      <td>2101</td>
      <td>10.717885</td>
      <td>20.924211</td>
    </tr>
    <tr>
      <th>2</th>
      <td>new</td>
      <td>12334822</td>
      <td>2016-06</td>
      <td>5173</td>
      <td>28.017655</td>
      <td>51.518773</td>
    </tr>
    <tr>
      <th>3</th>
      <td>potential</td>
      <td>3064184</td>
      <td>2016-06</td>
      <td>431</td>
      <td>6.960072</td>
      <td>4.292401</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.concat([df, tempdf], axis=0)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>napl</th>
      <th>M</th>
      <th>ymd</th>
      <th>billing_email</th>
      <th>M_percentage</th>
      <th>N_percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>active</td>
      <td>9710486</td>
      <td>2016-02</td>
      <td>1150</td>
      <td>49.521052</td>
      <td>22.209347</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lost</td>
      <td>1417314</td>
      <td>2016-02</td>
      <td>666</td>
      <td>7.227947</td>
      <td>12.862109</td>
    </tr>
    <tr>
      <th>2</th>
      <td>new</td>
      <td>7568428</td>
      <td>2016-02</td>
      <td>3219</td>
      <td>38.597091</td>
      <td>62.166860</td>
    </tr>
    <tr>
      <th>3</th>
      <td>potential</td>
      <td>912576</td>
      <td>2016-02</td>
      <td>143</td>
      <td>4.653910</td>
      <td>2.761684</td>
    </tr>
    <tr>
      <th>0</th>
      <td>active</td>
      <td>13070547</td>
      <td>2016-03</td>
      <td>1518</td>
      <td>49.435377</td>
      <td>22.415830</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lost</td>
      <td>2168870</td>
      <td>2016-03</td>
      <td>816</td>
      <td>8.203092</td>
      <td>12.049616</td>
    </tr>
    <tr>
      <th>2</th>
      <td>new</td>
      <td>10030950</td>
      <td>2016-03</td>
      <td>4265</td>
      <td>37.939024</td>
      <td>62.979917</td>
    </tr>
    <tr>
      <th>3</th>
      <td>potential</td>
      <td>1169296</td>
      <td>2016-03</td>
      <td>173</td>
      <td>4.422507</td>
      <td>2.554637</td>
    </tr>
    <tr>
      <th>0</th>
      <td>active</td>
      <td>17079146</td>
      <td>2016-04</td>
      <td>1839</td>
      <td>53.186615</td>
      <td>23.399924</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lost</td>
      <td>2332333</td>
      <td>2016-04</td>
      <td>914</td>
      <td>7.263179</td>
      <td>11.629978</td>
    </tr>
    <tr>
      <th>2</th>
      <td>new</td>
      <td>11417292</td>
      <td>2016-04</td>
      <td>4913</td>
      <td>35.554888</td>
      <td>62.514315</td>
    </tr>
    <tr>
      <th>3</th>
      <td>potential</td>
      <td>1282966</td>
      <td>2016-04</td>
      <td>193</td>
      <td>3.995318</td>
      <td>2.455783</td>
    </tr>
    <tr>
      <th>0</th>
      <td>active</td>
      <td>22191641</td>
      <td>2016-05</td>
      <td>2218</td>
      <td>56.048328</td>
      <td>24.606168</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lost</td>
      <td>2948761</td>
      <td>2016-05</td>
      <td>1376</td>
      <td>7.447540</td>
      <td>15.265143</td>
    </tr>
    <tr>
      <th>2</th>
      <td>new</td>
      <td>12747666</td>
      <td>2016-05</td>
      <td>5161</td>
      <td>32.196148</td>
      <td>57.255381</td>
    </tr>
    <tr>
      <th>3</th>
      <td>potential</td>
      <td>1705693</td>
      <td>2016-05</td>
      <td>259</td>
      <td>4.307984</td>
      <td>2.873308</td>
    </tr>
    <tr>
      <th>0</th>
      <td>active</td>
      <td>23907603</td>
      <td>2016-06</td>
      <td>2336</td>
      <td>54.304388</td>
      <td>23.264615</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lost</td>
      <td>4718568</td>
      <td>2016-06</td>
      <td>2101</td>
      <td>10.717885</td>
      <td>20.924211</td>
    </tr>
    <tr>
      <th>2</th>
      <td>new</td>
      <td>12334822</td>
      <td>2016-06</td>
      <td>5173</td>
      <td>28.017655</td>
      <td>51.518773</td>
    </tr>
    <tr>
      <th>3</th>
      <td>potential</td>
      <td>3064184</td>
      <td>2016-06</td>
      <td>431</td>
      <td>6.960072</td>
      <td>4.292401</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python

```


```python
df.to_csv('trytry.csv')
```


```python

```


```python

```
