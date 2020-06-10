import numpy as np
import matplotlib.pyplot as plt
import random as rad
#------------------------------
def t_rule(arr,r1,r2,r3,r4,r5,r6,r7,r8):


	t1=[1,1,1]
	t2=[1,1,0]
	t3=[1,0,1]
	t4=[1,0,0]
	t5=[0,1,1]
	t6=[0,1,0]
	t7=[0,0,1]
	t8=[0,0,0]
    
	for i in range(1,998-200):                        #yeah yeah, change the 200, 400 etc for tweaking frame size
		for j in range(1,996+400):
			temp=arr[i:i+1,j:j+3]                     #the 99.. numbers are adjusted
			if (temp==t1).all():                      #add/remove nines for grossly increasing/decreasing no of steps, 
				#mcell=r1                             #98 is fast, 998 is slow and 9998 takes forever...  
				arr[i+1,j+1]=r1
			
			
			elif (temp==t2).all():
				#mcell=r2
				arr[i+1,j+1]=r2
			
			elif (temp==t3).all():
				#mcell=r3
				arr[i+1,j+1]=r3

			elif (temp==t5).all():
				#mcell=r5
				arr[i+1,j+1]=r5

			
			elif (temp==t4).all():
				#mcell=r4
				arr[i+1,j+1]=r4

			elif (temp==t6).all():
				#mcell=r6
				arr[i+1,j+1]=r6

			elif (temp==t7).all():
				#mcell=r7
				arr[i+1,j+1]=r7

			else:
				#mcell=r8
				arr[i+1,j+1]=r8
	return(arr)
#--------------------------------------
arr1=np.zeros(shape=(999-200,999+400))                       #and also tweak here
arr1[1,500+198]=1
#--------------------------------------
n=int(input("enter the wolfram code: "))
a=bin(n)[2:len(bin(n))]
if len(a)<8:
	i=8-len(a)
	while i!=0:
		a="0"+a
		i=i-1
else:
	a=a
#a="11100001"
#--------------------------------------
arr=t_rule(arr1,int(a[0]),int(a[1]),int(a[2]),int(a[3]),int(a[4]),int(a[5]),int(a[6]),int(a[7]))
plt.imshow(arr,cmap="Greys")
plt.show()
#--------------------------------------