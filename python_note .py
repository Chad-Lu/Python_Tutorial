Reading before start work
��pycharm��import�����D�A�h�� File->Setting..->project:�W��->Project interpreter->�k�W�p�����Iadd->�� Existing environment ->�M����Anaconda��python.exe�ɧY�i�C






***String***
ddd = 'python are greataa'
print(ddd.replace('a','x',3) ) #python xre grextxa �A���ĤT�ӭȬ��ĴX�Ӥ��ᤣ����

.capitalize() #�r���ର�r���j�g
.find("string",�}�l��l,������l) #����ޭ�
.join("string) #�[�J�r��(����)

example:
newd = ":".join("python are greataa")
print(newd) #p:y:t:h:o:n: :a:r:e: :g:r:e:a:t:a:a

.split("",���Φ���)
example:
ddd = 'python are greataa'
print(ddd.split())  #['python', 'are', 'greataa']

***list***

example: �P�ɦL�X���ޭȻP���e
list1 = ['h','e','l','l','o']

for index,item in enumerate(list1):
    print(index,item) 

.pop()#�R�����e(�ϥί��ޭ�)�A�W�X�Ҥޭȷ|���~
.remove()#�R�����e(�ϥΤ��e)�A�S�����e�|���~

.del  #�R��list���e�A�]�i�H�����R��list
example:
list1 = ['h','e','l','l','o']
del list1[:3] #�R������3���e
print(list1) #['l', 'o']

�Ƨ�:
��k�@
list2 = [6,5,9,3,7,2,1,8,0,4] 

print(sorted(list2,reverse=True)) #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]�j��p�ƧǡAreverse�]��True
print(sorted(list2)) #[6,5,9,3,7,2,1,8,0,4]�A��l��l����

��k�G
list2.sort(reverse=True)
print(list2) #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]�A�|��������list��l

***Dictionary***

�Y�����ƪ�key�ȡA�h�����N�e��A���|�̷Ӷ��ǱƦC

.keys() #��X�Ҧ���key��
.values() #��X�Ҧ������e��
.update() #�s�W���(�[�J�@��Dic)
.clear() #�M���Ҧ����e

del #�R���@��key��
example:
dict = {'a':100,'b':200,'c':300}
del dict['c'] #�R��dict�̪�c��

print('c' in dict.keys()) #�P�_�O�_�s�bc��

sorted(dict.values()) #���e�ƦC(�p��j)
sorted(dict,key=dict.__getitem__) #(�p��j)�ƦC�A�����key��(���[�Jreverse=True�ܦ��j��p)

***��ƩI�s***
���[return���^�ǭ�

��ƪ��ܼƥu�b��Ƥ����ͮĪG�C
��Ƥ����ܼƭY������ާ@�A���P��ƥ~�L��
lambda �Ϊk

sum = lambda s1,s2:s1+s2
print(sum(5,6)) #11

***����ɦV***
�I�s�����O����k
super(�l���O,self).�P�W��k()

���e�[__���p�����A��k���I�s�ɥ�self.__�p�����(�~�����i�ϥ�)

��k�e�[__���p����k�A�����I�s�ɥ�self.__�p����k(�~�����i�ϥ�)


***�ҥ~�B��***(try:...except:...finally:...)<���ݻ��U���>

try...else... (�S���o�Ϳ��~�ɰ���A���Y�����~�@�˷|�����D)

finally: (�@�w�|����)

raise:���Ĳ�k(�S��Ϊk)
example:
try:
    a = int(input("��J����:"))
    if a <= 0 :
        raise ValueError("Error,This is not positive number!") #�۰�[�޵o���~
except ValueError as ve: #�N���~�r��a��T����
    print(ve)
------
example:
num1 = 10
num2 = 0
try:
    print(num1/num2)

except ZeroDivisionError as ex:
    print(ex)          #�L�X�t�ο��~�T��
    print("���~�o��")

�ۦ�w�q�ҥ~:
example:
class Valuetoosmall(Exception): pass  #�ۦ�]�p���O
class Valuetoolarge(Exception): pass

num_t = 10
try:
    num_i = int(input("��J�Ʀr:"))
    if num_t > num_i:
        raise Valuetoosmall
    elif num_t < num_i:
        raise Valuetoolarge

except Valuetoosmall:
    print("�ȤӤp")
except Valuetoolarge:
    print("�ȤӤj")
finally:
    print("END")

***�ɮצs��***
file object = open(file_name,access_mode,buffering,encodind='utf-8')

file_name #���W��

access_mode#�s���v��(rŪ�Aw�л\�Aa�[�J)

buffering#�w��(�w�]��0�A1���}�ҽw��)

encodind='utf-8' #�ĥ|�Ѽ�(������ϥΡA�S���r

readline #�v��Ū��

example:
flw = open('new.txt','w+',1,encoding='utf-8')
flw.write("����\n")
flw.write("����\n")
flw.close()

fla = open('new.txt','a+',1,encoding='utf-8')
fla.write("�[�J")
fla.close()

flr = open('new.txt','r+',1,encoding='utf-8')
a1 = flr.read()
print(a1)
flr.close()

***CSV***<���ݻ��U���>
�u��:liberOffice(utf-8�����) https://www.libreoffice.org/

reader() #�̷ӧǦC���XŪ��
DictReader() #�H�r�巧��Ū��

example_1(Ū�����):
import csv
f=open('example.csv','r',encoding='utf-8') #���}�@��excel�ɡA���[�Jutf-8������ϥ�(�i���[)

for row in csv.DictReader(f): //Ū�����
 if float(row['���W��'])>9.34�G #�Y�o����쪺��Ƥj��9.34
�@�@print(row['���W��'])        #�L�X���
f.close()

example_2(Ū�����):
import csv
f1=open('example.csv','r',encoding='utf-8') #���}�@��excel�ɡA���[�Jutf-8������ϥ�(�i���[)

for row in csv.DictReader(f1,['a','b','c','d','e','f']): //Ū����ơA���O�N��󤤪������w�b�U�ӭȤW(����|�����D)
 if float(row['f'])>70�G #�Y�o����쪺��Ƥj��70
�@�@print(row['f'])        #�L�X���
  else
    print("error")
f.close()

example_3(�N�Ȧs��list):
import csv
f = open('example.csv','r',encoding='utf-8')
csv1 = csv.reader(f)
list1 = list(csv1 ) #�N�Ȧs�Jlist
print(list1)

f.close()
------------------------------------------
writer() #�g�J���
writerow() #�i��S�w���x�s��g�J

example_3(�g�J���):
import csv
f = open('output.cs','w',newline'')
outputwriter = csv.writer(f)
outputwriter.writerow(['spam','eggs','bacon','ham'])  #�|�N��ƨ̧Ǽg�J�A�H�@�C�@�C���覡
outputwriter.writerow(['hello','eggs','bacon','ham'])  
outputwriter.writerow([1,2,3.141592,4]) 
f.close()

writer()�i���Ϊk

delimiter -> �o�O�N����j�Ÿ�
quotechar -> �N��]��r�ꪺ�Ÿ�
quoting -> �]�w�ޥΥ\��

csv.QUOTE_ALL  �i�ΩҦ����
csv.QUOTE_MINIMAL �ޥίS��Ÿ�
csv.QUOTE_NONNUMERIC �ޥΩҦ����O�ƭȪ��Ҧ��r��
csv.QUOTE_NONE ���n���X�W�ޥΥ�����

example_4(�g�J���):
import csv
f = open('example.csv','r',encoding='utf-8') 
reader = csv.reader(f)
ofile =open('ttest.csv','w',encoding='utf-8')
writer = csv.writer(ofile ,delimiter ='-',quotechar ='"',quoting= csv.QUOTE_ALL  ) #quoting�i�藍�P�Ϊk
for row in reader :
    writer .writerow(row)
f.close()
ofile.close()
----
example_5(json����):
import json
json1={'python':'google?','gjun':100}
json2= json.dumps(json1, ensure_ascii=False)#�iŪ��utf-8
print(json2)
json3 =json2.encode('utf-8') #�H�g�Ojson�榡�A���ΦA�@�@��
print(json3)

example_6(json����Ū��):
import json
file =open('data.json','r',encoding='utf-8')#loadŪ���ɮ�
data = json.load(file)

for p in data['people']: #people��json�ɪ��N��
       print('Name'+p['name']) #json��name���
       print('Website'+p['website'])#json��website���
       print('From'+p['from'])

***�����^��***
read()#Ū���Ҧ����e
decode()#�s�X�]�w

example:
import urllib.request

x = urllib.request.urlopen('http://www.pcschool.com.tw')#���K����
html= x.read().decode('utf-8') #�i�椤��s�X�Aread()�i�H�[�Ʀr
print(html)

�i���Ϊk:<���ݻ��U���>
from html.parser import HTMLParser #�ݭn�Ψ����O�إ�

request.get(����).text #���o��������r�A�i�H���d��

POST �L�����Ƥj�p 
GET  ������Ƥj�p

�i�ϥΥ��W���M����


***Numpy***<���ݻ��U���>

�P���A���h���}�C

example_1:(�}�C�ۥ[)
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
print(a[1,1:3]) #�ĤG����1�M2
print(a[:,1])  #�ĤG�����@
print("----------")
a[1,4] = 100 #��Ĥ@���M�ĤG������
print(a)
a[:,0] = [0,0,0] #��Ҧ��ĤG�����Ȭ�0
print(a)
print(a[(0,1,2),(2,3,4)]) #[ 3  9 15] �H�U�Ӥ��@��X

example_3:
b = np.linspace(0,1,6) #�ƭ�0��1�A����6�_
print(b) #[0.  0.2 0.4 0.6 0.8 1. ]

***�}�C����***
example:(����)
import numpy as np


a = np.arange(12).reshape(3,4)
print(a)                         #[[ 0  1  2  3]
                                   [ 4  5  6  7]
                                   [ 8  9 10 11]]
print(np.split(a,3,axis=0))      #[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]�A����3�����Aaxis=0����������

print(np.split(a,2,axis=1))      #[array([[0, 1],
                                          [4, 5],
                                          [8, 9]]), array([[ 2,  3],
                                          [ 6,  7],
                                          [10, 11]])]      ����2���Aaxis=1���a�V����

print(np.vsplit(a,3))    #[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]�A��3��(����)
print(np.hsplit(a,2))    #[array([[0, 1],
                                 [4, 5],
                                 [8, 9]]), array([[ 2,  3],
                                 [ 6,  7],
                                 [10, 11]])] �A������2��  


np.array_split(a,2,axis=1) #���������
np.array_split(a,2,axis=0) #���������

example:(�X��)
import numpy as np

np.concatenate((a,b))  #�����X��(�w�]0)
np.concatenate((a,b),axis = 1) #�����X��

np.hstack((?,?)) #�����X��
np.vstack((?,?)) #�����X��


np.reshape(?,?) #�N�}�C�ഫ�A�����������j�p�A�e�᤺�e�ȷ|�@�_�ܰ�
np.resize(arr?,(?,?)) #�|�۰ʸɭ�(�H�쥻����)��}�C�A�e�᤺�e�Ȥ��|�@�_�ܰ�
 
np.append(arr,[[�ݦ���L����]],axis=0) #�᭱0���Ĥ@���A�H������

mp.insert(arr,index,[��],axis = ?) #a = np.insert(a,2,[9,9,99,999],axis=0)�A�w�]1�����

np.delete(arr,index,axis=0) #a = np.delete(a,3,axis=0)

example:(�W�S)
import numpy as np

a = np.array([2,5,9,3,6,4,7,2,1])
print(a)
b,inidices = np.unique(a,return_index=True) #���i���[�Areturn_index=True�^�ǯ��ޭ�(�@��ȷ����)�Areturn_inverse=True�^�ǯ��ޭ�(�H�ߤ@�ȷ�@����)�Areturn_counts=True�^�ǥX�{�ƶq
print(b)
print("index:")
print(inidices)

example:(�}�C�j�p��)
import numpy as np

a = np.array([2,5,9,3,6,4,7,2,1])
print(a)

b = np.clip(a,4,7)
print(b)  #[4 5 7 4 6 4 7 4 4]

example:(����)
import numpy as np

a = np.array([[2,5,9,3],[4,7,2,1],[3,6,9,4]])
print(a)
print(a.T) #print(np.transpose(a))����

example:(���Z��)
import numpy as np

a = np.array([[2,5,9,3],[4,7,2,1],[3,6,9,4]])
print(a.flatten(order='F')) #F���@��
print(a.flatten(order='C')) #C���@�C(�w�])

for item in a.flat: #�̧Ǩ��ȥΪk
    print(item)

***numpy�ƭȹB��***

add(a,b) #�[(+)
subtract(a,b) #��(-)
multiply(a,b) #��(*)
divide(a,b) #��(/)

power(a,n) #a��n����
reciprocal(a) #�˼ƭp��A�Ҧpa*b=1�A��Ja�Db

mod(a,b) #�l�� == remainder(a,b)
around(a,decimals=���) #�|�ˤ��J(�w�]0)
floor(a) #�^�Ǥ��j���J�Ѽƪ��̤j���
ceil() #�^�Ǥj���J�Ѽƪ��̤p���

example:
a = y.array([-1.7,0.3,7.8,9])
print(a)
b = y.floor(a)
print(b) #[-2.  0.  7.  9.] ���j��a�}�C
b = y.ceil(a)
print(b) #[-1.  1.  8.  9.] �n�j��a�}�C

sum(a,axis=) #�}�C���`�M(�i���w�b)
min(a,axis=) #��̤p��(�i���w�b)
max(a,axis=) #��̤j��(�i���w�b)

ptp(a,axis=) #�i�����w�b���d��(�̤j��̤p)
precentile(a,0~100,axis=) #�έp�ƾڪ��׶q����

median(a,axis=) #��X������(�i���w�b)
mean(a,axis=) #������(�i���w��)
average(a,weights =) #�Pmean�����A���i�[�v���p��
average([1,2,3,4],weights=[4,3,2,1],returned=True) #���[ True�A�i�H�L�X�Q�����v����
����: (1*4+2*3+3*2+4*1)/(4+3+2+1) = 20/10 = 2

var(a) #���o�ܲ���
std(a) #���o�зǮt

cumsum(a,axis=) #���e�i��֥[(����ۥ[)
diff(a,axis=) #���e�֮t(��Ȱ����)

dot(a,b) #�}�C�ۭ�(�ƾǦ�)
inner(a,b) #�@���}�C�ۭ��A���k�D�@��(���`�N)

where(����) #�|�^�Ǻ������󪺯��ޭ�
extract(����,�}�C) #�^�Ǻ������󪺤��e