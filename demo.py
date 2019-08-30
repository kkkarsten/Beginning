

 
 
   #-*- coding: utf-8 -*-
  """
  Created on Wed Aug 14 09:50:02 2019
  
  @author: Administrator
  """
  
  '123','4'
  num = '5'
  print "hello"+num+'fdkj'
  print num
  
  '''
  fdskjljflsl.
  'fdlkj',fdksjklfd
  fdsljfl'''
  
  "fdkgfkljfsdkjflsdjf\n"
  
  r'fjgl \n' 
  
  i='5'
  i=5
  print 'I repeat, the value is', i 
  
  -25.5%2.25
  
  3 or 7 
  
  a = int(raw_input("enter your data,"));
  
  a = input("enter your data: ")
  
  if a == 8:
      print "fdlsk" 
  elif a < 8:
      print "sss"
  else :
          print "fdsf"
          
          
          
  a = input();
  b=a;
  
  
  a = 20;
  b = 20;
  while b==a:
      b= input("enter your data:")
      if b==a:
          print "yeh,you\'ve got right"
          b=a-1
      elif b<a:
              print "got littel lower"
              b=a
      else:
          print "got littel higher"
          b=a
  else:
      print "no valid input"
      
  
  print 'done'
  
  
  for i in range(1,10):
      print i
  
  
  print 5
  
  
  
 
 def connec(x,y=1):
     print x*y
 
 connec('hello',5)
 
 
 def xdc(x,y,z=10):
     '''gjfkdljgkdlfjgk.
     
     fjklsfjslkj.'''
     a = x#fhdskjfhsdj
     b = y
     print "x is ",x, "y is", y,"z is ",z
     
 xdc(y=20,x=2)
 
 print xdc.__doc__
 
import sdf
dir(sdf)
 sdf.sdf()
 

import sys
print 'fhkjdshf'
for i in sys.argv:
    print i

print '\n\n The PYTHONPATH is',sys.path,'\n'



a = [1,2,3]
b = a;
b.append('ccc')
del b[2]
b.remove(2)
for item in b:
    print item,
b.append([3,4])
b.sort
b.insert(0,7)

print 'fdsj%sfgsjh%d%d%d'%(b[2],9,8,7)


a= 0
b=a
a = a+1

a=[1,2,3]
b=a[:]
a.remove(1)
print a,b

x='hjk'
y=x
x[0]='l'


class Ftgih:
    def __init__(self,name,b):
        self.name = name
    def say(self):
        print 'hello my name is %s'%self.name

p = Ftgih("LunChen","Zhang")
p.say()


class Person:
    popu = 0
    def __init__(self,name):
        self.name =  name
        print 'Initializing %s' %self.name
        
        Person.popu +=1
        
    def __del__(self):
        print '%s says bye.'%self.name
        
        Person.popu -=1
        
        if Person.popu ==0:
            print 'Last one'
        else:
            print '%d people left' % Person.popu
    
    def say(self):
        print 'my name is',self.name
    
    def howmany(self):
        if Person.popu ==1:
            print 'The only person'
        else:
            print 'we have %d persons herehgfhf' % Person.popu



Lun = Person('Lun')
Lun.say()
Lun.howmany()
Lun.popu
Person.popu
Zhang = Person('zhang')
Zhang.say()
Zhang.howmany()
Zhang.popu
Person.popu

Lun.say()
Lun.howmany()

dir(Lun)
Lun.popu=70
Zhang.popu
Person.popu  ######即 Person.popu 不能通过Lun.popu和Zhang.popu来改动

del Lun
del Zhang

class SchoolMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print 'Initialized SchM: %s' % self.name
    def tell(self):
        print 'Name: "%s" Age: "%d"'%(self.name,self.age)


class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print 'Initialized Tea: %s' % self.name
    def tell(self):
        SchoolMember.tell(self)
        print'Salary:"%d"'%self.salary
        
class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print 'Initialized Stu: %s' % self.name
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: %d' % self.marks
        
t = Teacher('Mrs.Shrividya',40,30000)
s = Student('Swaroop',22,75)
print
members = [t,s]
for member in members:
    member.tell()



ppp = 'fdhjkfhdskjfhfehtkjsfsdjhfkjdshfjkdhfjdhfjksdhfjksdhfjksdhfsjdkhfdsk\
jghkjghjkdshgkjdhghdgsjhkdsjhgjkshgsdj'
f = file('ppp.txt','w')
f.write(ppp)
f.close()

f = file('ppp.txt')
while True:
    line = f.readline()
    if len(line)==0:
        break
    print line
f.close()



import numpy
import cv2
#image = cv2.imread('C:/Users/Administrator/Desktop/KKK.png')
#image = cv2.imread('./KKK.png')
#image = cv2.imread('C:/Users/Administrator/Desktop/exampleaa.png')
#image = cv2.imread('../example.jpeg')
#image = cv2.imread('C:/Users/Administrator/Desktop/example.jpeg',cv2.IMREAD_GRAYSCALE)
#cv2.imwrite('C:/Users/Administrator/Desktop/exam.jpeg',image)
#cv2.imwrite('C:/Users/Administrator/Desktop/KKK.png',image)
img = cv2.imread("C:/Users/Administrator/Desktop/example.jpeg",0)
cv2.imwrite('canny.jpg',cv2.Canny(img,200,300))
cv2.imshow("canny",cv2.imread('canny.jpg'))


#cv2.imshow('imshow',image)
cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import numpy as np

img = np.zeros((200,200),dtype=np.uint8)
img[50:150,50:150]=255

ret, thresh = cv2.threshold(img, 127, 255, 0)
image, contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color,contours,-1,(0,255,0),2)
cv2.imshow("contours",color)
cv2.waitKey()
cv2.destroyAllwindows()



import numpy as np

x= np.ones((100,100),np.uint8)
y= np.zeros((100,100),np.uint8)
z= np.ones((100,100),np.uint8)

a = np.array[x,y,z]




