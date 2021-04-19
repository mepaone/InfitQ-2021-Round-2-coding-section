"""
#QUESTION 1:(Identify Pairs)
Consider two non-empty input lists inlistt and inlist2 each containing unique integers!
Identify and print outlist based on the logic below:

-->Check the sum of elements of each of the input lists inlist1 and inlist2. If their
	sums are not equal then:
  >Identify pair(s) of numbers, (num1, num2) where num is from inlist1 and
      num2is from inlist2 such that when swapped between inlist1 and inlist2,
      the sum of elements in each of the lists, inlist1 and inlist2 is equal.
  >Find the product of num1 and num2 for each of the identified pairs.
  >Add the numbers, num1 followed by num2, in the pairs (num1, num2) to
      outlist in their ascending order of even product (if any) followed by the
      numbers in the pairs with odd products (if any) in decreasing order
  >Print -1 if no such pair of number exists or the given input lists already have the same sum.

Note: Consider ‘zero’ as an even number
Input format:
First line will contain inlist1 elements separated by a space

Second line will contain inlist2 elements separated by a space

Read the input from the standard input stream
 I/P:  9,2,4,14,5,1,3
        1,12,7,9,2,3
 O/P:  4,2,14,12,9,7,5,3,3,1
     Explanation:
     For the given inputs, inlist1 is 19, 2, 4, 14, 5, 1, 3]& inlist2 is [1, 12, 7,9, 2, 31].
     The sum of elements of inlist1 i.e. 38 is not equal to the sum of elements of inlist2 i.e. 34

    The pair of numbers (9,7) where 9 from inlist1 and 7 from inlist2, when swapped the sum of elements of inlist1
    is 36 and sum of elements of inlist2 is 36 which is equal.
    Similarly, the following pairs of numbers when swapped, the sum of elements of168
    num1= 5, num2=3; prod=15 ; num1-3, num2=1; prod=3

     Even products are 8 and168. Adding the pairs to outlist.based on the increasing order
     of even products results in 4,2,14,12.
     Odd products are 63,15 and 3. Adding the corresponding pairs to outlist based on the decreasing order
    of odd products result in 4,2,14,12,9,7,5,3,3,1.

"""
#code
N1=list(map(int,input().split()))
N2=list(map(int,input().split()))
out=[]
for i in range(len(N1)):
    for j in range(len(N2)):
        t=N1[i]
        N1[i]=N2[j]
        N2[j]=t
        if(sum(N1)==sum(N2)):
            out.append([N2[j],N1[i]])
        t=N1[i]
        N1[i]=N2[j]
        N2[j]=t
even={}
odd={}
for i in out:
    if((i[0]*i[1])%2==0):
        even[i[0]*i[1]]=i
    else:
        odd[i[0]*i[1]]=i
E=list(even.keys())
O=list(odd.keys())
E.sort()
O.sort(reverse=True)
l=[]
for i in E:
    l+=even[i]
for i in O:
    l+=odd[i]
if(len(l)==0):
    print("-1")
else:
    print(*l,sep=",")