# a) Write a Python program to store roll numbers of student in
# array who attended training program in random order. Write
# function for searching whether particular student attended
# training program or not, using Linear search and Sentinel
# search.
# b) Write a Python program to store roll numbers of student
# array who attended training program in sorted order. Write
# function for searching whether particular student attended
# training program or not, using Binary search and Fibonacci
# search.

class Students:
    def linear_search(self,li):
        n=len(li)
        print("Enter the roll no. to search:")
        num = int(input())
        index=-1

        for i in range(0,n):
            if(num==li[i]):
                print("\nRoll no. ",num," attended the training. Present at index : ",i)
                index=i
                break
        if(index==-1):
            print("Roll no. ", num, " did not attend the training")
        print("===========================================================================")


    def binary_search(self,li):
        e= n = len(li)
        li=self.sort_list(li)
        print("Enter the roll no. to search:")
        num = int(input())
        index = -1
        i=0
        s=0
        while(s<=e):
            m=int((s+e)/2)
            print("\ni=",++i,"m=",m,"s,e=",s,e)
            if li[m]==num:
                index=m
                break
            elif li[m]<num:
                s=m+1
            elif li[m]>num:
                e=m-1

        if(index==-1):
            print("Roll no. ", num, " did not attend the training")
        else:
            print("Roll no. ", num, " attended the training present at index : ",index)

    def sentinel_search(self,li):
        print("Enter the roll no. to search:")
        key = int(input())
        index=-1
        last=li[-1]
        i=0
        
        while(li[i]!=key):
            i+=1
        
        li[-1]=last
        
        if(i<(n-1) or (li[n-1]==key)):
            print(key," is present at index ",i)
        else:
            print("Element not found")

    def fibo_search(self):
        pass

    def sort_list(self,li):
        # for i in range(0,len(li)-1):
        #     if(li[i]>li[i+1]):
        #         temp=li[i]
        #         li[i]=li[i+1]
        #         li[i+1]=temp
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if li[j] > li[j + 1]:
                # Swap if the element found is greater than the next element
                    li[j], li[j + 1] = li[j + 1], li[j]

        print("Sorted list: ",li)
        return li

print("Enter number of students: ")
n=int(input())
student=[]
print("Enter their roll no.s:")
for i in range(0,n):
    a=int(input())
    student.append(a)

print("Students:",student)
obj=Students()

c='y'
while(c=='y' or c=='Y'):
    print("Enter the search algorithm \n1.Linear Search\n2.Binary search\n3.Sentinel search\n4.Fibonacci search\n")
    ch=int(input())

    if(ch==1):
        obj.linear_search(student)
    elif(ch==2):
        obj.binary_search(student)
    elif(ch==3):
        obj.sentinel_search(student)
    elif(ch==4):
        obj.fibo_search()

    c=input("Do you want to continue(Y for Yes):")

else:
    print("Thank you")