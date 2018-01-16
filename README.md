# Python coding style 規範
目錄
 1. coding style
 2. function 與迴圈複雜度
 3. 檢驗工具
___
## coding style
網頁版：https://www.openfoundry.org/tw/tech-column/9179-python-

#### 以下整理一些我覺得比較重要的規則, 有其他想法歡迎一起討論

**1. 基本語法**
- 縮排使用四個空白格,不要用 tab（各個 IDE 都可以設定）
- 每一行長度最多 79 個字元之內
- class 內的 method 間以一個空白行分隔  

- 以下情況避免使用額外空白<br />  
1. 緊連在圓括號、方括號、大括號之內
```python
#good
spam(ham[1], {eggs: 2})
```
```python
#bad
spam( ham[ 1 ], { eggs: 2 } )
```
2. 逗號( , )、冒號( : )前<br /> 
```python
#good
if x == 4: 
    print x, y
```
```python
#bad
if x == 4 :
    print x , y
```
3. [ ]與( )前<br />  
```python
#good
spam(1)
dict['key'] = list[index]
```
```python
#bad
spam (1)
dict ['key'] = list [index]
```
4. 當 '=' 符號是用在關鍵字參數或預設參數值時<br />
```python
#good
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```
```python
#bad
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```

- 以下情況必須使用空白
1. 在二元運算子**前後**加上一個空白：賦值（=）、增量賦值（+=, -= 之類）、比較（==, ＜, ＞, !=, ＜＞, ＜=, ＞=, in, not in, is, is not）、邏輯（and, or, not）
```python
#good
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```
```python
#bad
i=i+1
submitted +=1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```
2. 逗號後( , )
```python
#good
spam(ham[1], {eggs: 2})
```
```python
#bad
spam(ham[1],{eggs: 2})
```

**2. 註解**
- 有 function, class, method 就要有文件字串 docstring
- 永遠將更新註解列為優先事項

**3. 命名慣例**
- class 名稱使用字首大寫慣例。僅供內部用的 class，名稱前會加一個底線
- single_trailing_underscore_ 結尾單一底線：慣例上用於避免和 Python 關鍵字衝突
- 不要用難以理解或閱讀的詞當變數名稱
```python
#good
signal_data = pd.read_csv('.....')
max_pnl = max(pnl_list)
min_pnl = min(pnl_list)
```
```python
#bad
df = pd.read_csv('.....')
aa = max(pnl_list)
bb = min(pnl_list)
```

**4. 程式撰寫建議**
- 捕捉 exception 時，盡可能註明特定的 exception 而不要只用空的 'except:' 子句
```python
#good
try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None
```
```python
#bad
try:
    import platform_specific_module
except:
    pass
```
- 對於所有 try/except 子句，將 'try' 子句的程式碼數量限制在所需的最少數量。如此也能避免掩飾住 bug
```python
#good
try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)
```
```python
#bad
try:
    # Too broad! （太廣！）
    return handle_value(collection[key])
except KeyError:
    # Will also catch KeyError raised by handle_value()
    # （也會捕捉到 handle_value() 發出的 KeyError）
    return key_not_found(key)
```
- 用 ''.startswith() 和 ''.endswith() 比對字串的字首和字尾，而不要用字串 slice，更清楚明白且不容易出錯
```python
#good
if foo.startswith('bar'):
```
```python
#bad
if foo[:3] == 'bar':
```
- 比較物件型別應該永遠用 isinstance() 而不要直接比較型別
```python
#good
if isinstance(obj, int):
```
```python
#bad
if type(obj) is type(1):
```
- 對於序列（string, list, tuple），利用空序列代表 false 的特性
```python
#good
if not seq:
if seq:
```
```python
#bad
if len(seq)
if not len(seq)
```
- 不要將邏輯值用 == 去和 True 或 False 比較
```python
#good
if greeting:
```
```python
#bad
if greeting == True:
if greeting is True:
```
- 迴圈內不重要的疊代變數以_命名,若是有意義的則要額外命名
```python
#good
for _ in range(10):
    print('Hello World')
    _ += 1

for (idx, value) in enumerate(pnl_list):
    print(idx, value)
```
```python
#bad
for n in range(10):
    print('Hello World')
    n += 1

for (i, j) in enumerate(pnl_list):
    print(i, j)
```

___
## function 與迴圈複雜度
- 這部分先跳過, 等 coding style 熟習後再來規範

___
## 檢驗工具
- 可以使用 pylint 檢驗 coding style  https://www.pylint.org/
- 或使用 coala https://coala.io/#/coalaonline

#### pylint 報表
