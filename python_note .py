Reading before start work
諾pycharm的import有問題，則到 File->Setting..->project:名稱->Project interpreter->右上小齒輪點add->選 Existing environment ->然號找Anaconda的python.exe檔即可。






***String***
ddd = 'python are greataa'
print(ddd.replace('a','x',3) ) #python xre grextxa ，後方第三個值為第幾個之後不改變

.capitalize() #字串轉為字首大寫
.find("string",開始位子,結束位子) #找索引值
.join("string) #加入字串(間格)

example:
newd = ":".join("python are greataa")
print(newd) #p:y:t:h:o:n: :a:r:e: :g:r:e:a:t:a:a

.split("",分割次數)
example:
ddd = 'python are greataa'
print(ddd.split())  #['python', 'are', 'greataa']

***list***

example: 同時印出索引值與內容
list1 = ['h','e','l','l','o']

for index,item in enumerate(list1):
    print(index,item) 

.pop()#刪除內容(使用索引值)，超出所引值會錯誤
.remove()#刪除內容(使用內容)，沒有內容會錯誤

.del  #刪除list內容，也可以直接刪除list
example:
list1 = ['h','e','l','l','o']
del list1[:3] #刪除索引3之前
print(list1) #['l', 'o']

排序:
方法一
list2 = [6,5,9,3,7,2,1,8,0,4] 

print(sorted(list2,reverse=True)) #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]大到小排序，reverse設為True
print(sorted(list2)) #[6,5,9,3,7,2,1,8,0,4]，原始位子不變

方法二
list2.sort(reverse=True)
print(list2) #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]，會直接改變list位子

***Dictionary***

若有重複的key值，則後方取代前方，不會依照順序排列

.keys() #找出所有的key值
.values() #找出所有的內容值
.update() #新增資料(加入一個Dic)
.clear() #清除所有內容

del #刪除一個key值
example:
dict = {'a':100,'b':200,'c':300}
del dict['c'] #刪除dict裡的c值

print('c' in dict.keys()) #判斷是否存在c值

sorted(dict.values()) #內容排列(小到大)
sorted(dict,key=dict.__getitem__) #(小到大)排列，但顯示key值(後方加入reverse=True變成大到小)

***函數呼叫***
後方加return為回傳值

函數的變數只在函數內產生效果。
函數內的變數若有任何操作，都與函數外無關
lambda 用法

sum = lambda s1,s2:s1+s2
print(sum(5,6)) #11

***物件導向***
呼叫父類別的方法
super(子類別,self).同名方法()

欄位前加__為私有欄位，方法內呼叫時用self.__私有欄位(外部不可使用)

方法前加__為私有方法，內部呼叫時用self.__私有方法(外部不可使用)


***例外處裡***(try:...except:...finally:...)<雲端輔助資料>

try...else... (沒有發生錯誤時執行，但若有錯誤一樣會有問題)

finally: (一定會執行)

raise:手動觸法(特殊用法)
example:
try:
    a = int(input("輸入正數:"))
    if a <= 0 :
        raise ValueError("Error,This is not positive number!") #自動[引發錯誤
except ValueError as ve: #將錯誤字串帶到訊息中
    print(ve)
------
example:
num1 = 10
num2 = 0
try:
    print(num1/num2)

except ZeroDivisionError as ex:
    print(ex)          #印出系統錯誤訊息
    print("錯誤發生")

自行定義例外:
example:
class Valuetoosmall(Exception): pass  #自行設計類別
class Valuetoolarge(Exception): pass

num_t = 10
try:
    num_i = int(input("輸入數字:"))
    if num_t > num_i:
        raise Valuetoosmall
    elif num_t < num_i:
        raise Valuetoolarge

except Valuetoosmall:
    print("值太小")
except Valuetoolarge:
    print("值太大")
finally:
    print("END")

***檔案存取***
file object = open(file_name,access_mode,buffering,encodind='utf-8')

file_name #文件名稱

access_mode#存取權限(r讀，w覆蓋，a加入)

buffering#緩衝(預設為0，1為開啟緩衝)

encodind='utf-8' #第四參數(中文文件使用，特殊文字

readline #逐行讀取

example:
flw = open('new.txt','w+',1,encoding='utf-8')
flw.write("測試\n")
flw.write("測試\n")
flw.close()

fla = open('new.txt','a+',1,encoding='utf-8')
fla.write("加入")
fla.close()

flr = open('new.txt','r+',1,encoding='utf-8')
a1 = flr.read()
print(a1)
flr.close()

***CSV***<雲端輔助資料>
工具:liberOffice(utf-8中文用) https://www.libreoffice.org/

reader() #依照序列號碼讀取
DictReader() #以字典概念讀取

example_1(讀取資料):
import csv
f=open('example.csv','r',encoding='utf-8') #打開一個excel檔，後方加入utf-8為中文使用(可不加)

for row in csv.DictReader(f): //讀取資料
 if float(row['欄位名稱'])>9.34： #若這個欄位的資料大於9.34
　　print(row['欄位名稱'])        #印出資料
f.close()

example_2(讀取資料):
import csv
f1=open('example.csv','r',encoding='utf-8') #打開一個excel檔，後方加入utf-8為中文使用(可不加)

for row in csv.DictReader(f1,['a','b','c','d','e','f']): //讀取資料，分別將文件中的欄位指定在各個值上(中文會有問題)
 if float(row['f'])>70： #若這個欄位的資料大於70
　　print(row['f'])        #印出資料
  else
    print("error")
f.close()

example_3(將值存到list):
import csv
f = open('example.csv','r',encoding='utf-8')
csv1 = csv.reader(f)
list1 = list(csv1 ) #將值存入list
print(list1)

f.close()
------------------------------------------
writer() #寫入資料
writerow() #進行特定的儲存格寫入

example_3(寫入資料):
import csv
f = open('output.cs','w',newline'')
outputwriter = csv.writer(f)
outputwriter.writerow(['spam','eggs','bacon','ham'])  #會將資料依序寫入，以一列一列的方式
outputwriter.writerow(['hello','eggs','bacon','ham'])  
outputwriter.writerow([1,2,3.141592,4]) 
f.close()

writer()進階用法

delimiter -> 這是代表分隔符號
quotechar -> 代表包住字串的符號
quoting -> 設定引用功能

csv.QUOTE_ALL  可用所有資料
csv.QUOTE_MINIMAL 引用特殊符號
csv.QUOTE_NONNUMERIC 引用所有不是數值的所有字串
csv.QUOTE_NONE 不要於輸出上引用任何資料

example_4(寫入資料):
import csv
f = open('example.csv','r',encoding='utf-8') 
reader = csv.reader(f)
ofile =open('ttest.csv','w',encoding='utf-8')
writer = csv.writer(ofile ,delimiter ='-',quotechar ='"',quoting= csv.QUOTE_ALL  ) #quoting可改不同用法
for row in reader :
    writer .writerow(row)
f.close()
ofile.close()
----
example_5(json應用):
import json
json1={'python':'google?','gjun':100}
json2= json.dumps(json1, ensure_ascii=False)#可讀取utf-8
print(json2)
json3 =json2.encode('utf-8') #以經是json格式，不用再作一次
print(json3)

example_6(json應用讀取):
import json
file =open('data.json','r',encoding='utf-8')#load讀取檔案
data = json.load(file)

for p in data['people']: #people為json檔的代表
       print('Name'+p['name']) #json的name欄位
       print('Website'+p['website'])#json的website欄位
       print('From'+p['from'])

***網頁擷取***
read()#讀取所有內容
decode()#編碼設定

example:
import urllib.request

x = urllib.request.urlopen('http://www.pcschool.com.tw')#巨匠網頁
html= x.read().decode('utf-8') #進行中文編碼，read()可以加數字
print(html)

進階用法:<雲端輔助資料>
from html.parser import HTMLParser #需要用到類別建立

request.get(網頁).text #取得網頁的文字，可以做查詢

POST 無限制資料大小 
GET  有限資料大小

可使用正規式尋找資料


***Numpy***<雲端輔助資料>

同型態的多為陣列

example_1:(陣列相加)
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
c = a+b
print(c)
c= a-b
print(c)
print(type(c))

example_2:
import numpy as np

a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(a[1,1:3]) #第二維的1和2
print(a[:,1])  #第二維取一
print("----------")
a[1,4] = 100 #改第一維和第二維的值
print(a)
a[:,0] = [0,0,0] #改所有第二維的值為0
print(a)
print(a[(0,1,2),(2,3,4)]) #[ 3  9 15] 以各個比對作輸出

example_3:
b = np.linspace(0,1,6) #數值0到1，切成6斷
print(b) #[0.  0.2 0.4 0.6 0.8 1. ]

***陣列應用***
example:(切割)
import numpy as np


a = np.arange(12).reshape(3,4)
print(a)                         #[[ 0  1  2  3]
                                   [ 4  5  6  7]
                                   [ 8  9 10 11]]
print(np.split(a,3,axis=0))      #[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]，切成3部分，axis=0為水平切割

print(np.split(a,2,axis=1))      #[array([[0, 1],
                                          [4, 5],
                                          [8, 9]]), array([[ 2,  3],
                                          [ 6,  7],
                                          [10, 11]])]      切成2份，axis=1為縱向切割

print(np.vsplit(a,3))    #[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]，切3份(水平)
print(np.hsplit(a,2))    #[array([[0, 1],
                                 [4, 5],
                                 [8, 9]]), array([[ 2,  3],
                                 [ 6,  7],
                                 [10, 11]])] ，垂直切2份  


np.array_split(a,2,axis=1) #水平切兩份
np.array_split(a,2,axis=0) #垂直切兩份

example:(合併)
import numpy as np

np.concatenate((a,b))  #垂直合併(預設0)
np.concatenate((a,b),axis = 1) #水平合併

np.hstack((?,?)) #水平合併
np.vstack((?,?)) #垂直合併


np.reshape(?,?) #將陣列轉換，但須有對應大小，前後內容值會一起變動
np.resize(arr?,(?,?)) #會自動補值(以原本的值)到陣列，前後內容值不會一起變動
 
np.append(arr,[[需有對印的數]],axis=0) #後面0為第一維，以此類推

mp.insert(arr,index,[值],axis = ?) #a = np.insert(a,2,[9,9,99,999],axis=0)，預設1維表示

np.delete(arr,index,axis=0) #a = np.delete(a,3,axis=0)

example:(獨特)
import numpy as np

a = np.array([2,5,9,3,6,4,7,2,1])
print(a)
b,inidices = np.unique(a,return_index=True) #後方可不加，return_index=True回傳索引值(一般值當索引)，return_inverse=True回傳索引值(以唯一值當作索引)，return_counts=True回傳出現數量
print(b)
print("index:")
print(inidices)

example:(陣列大小值)
import numpy as np

a = np.array([2,5,9,3,6,4,7,2,1])
print(a)

b = np.clip(a,4,7)
print(b)  #[4 5 7 4 6 4 7 4 4]

example:(反轉)
import numpy as np

a = np.array([[2,5,9,3],[4,7,2,1],[3,6,9,4]])
print(a)
print(a.T) #print(np.transpose(a))反轉

example:(平坦化)
import numpy as np

a = np.array([[2,5,9,3],[4,7,2,1],[3,6,9,4]])
print(a.flatten(order='F')) #F為一行
print(a.flatten(order='C')) #C為一列(預設)

for item in a.flat: #依序取值用法
    print(item)

***numpy數值運算***

add(a,b) #加(+)
subtract(a,b) #減(-)
multiply(a,b) #乘(*)
divide(a,b) #除(/)

power(a,n) #a的n次方
reciprocal(a) #倒數計算，例如a*b=1，輸入a求b

mod(a,b) #餘數 == remainder(a,b)
around(a,decimals=位數) #四捨五入(預設0)
floor(a) #回傳不大於輸入參數的最大整數
ceil() #回傳大於輸入參數的最小整數

example:
a = y.array([-1.7,0.3,7.8,9])
print(a)
b = y.floor(a)
print(b) #[-2.  0.  7.  9.] 不大於a陣列
b = y.ceil(a)
print(b) #[-1.  1.  8.  9.] 要大於a陣列

sum(a,axis=) #陣列值總和(可指定軸)
min(a,axis=) #找最小值(可指定軸)
max(a,axis=) #找最大值(可指定軸)

ptp(a,axis=) #可取指定軸的範圍(最大減最小)
precentile(a,0~100,axis=) #統計數據的度量指標

median(a,axis=) #找出中間值(可指定軸)
mean(a,axis=) #平均值(可指定值)
average(a,weights =) #與mean類似，但可加權重計算
average([1,2,3,4],weights=[4,3,2,1],returned=True) #後方加 True，可以印出被除的權重值
公式: (1*4+2*3+3*2+4*1)/(4+3+2+1) = 20/10 = 2

var(a) #取得變異數
std(a) #取得標準差

cumsum(a,axis=) #內容進行累加(持續相加)
diff(a,axis=) #內容累差(兩值做比較)

dot(a,b) #陣列相乘(數學式)
inner(a,b) #一維陣列相乘，乘法非一般(須注意)

where(條件) #會回傳滿足條件的索引值
extract(條件,陣列) #回傳滿足條件的內容