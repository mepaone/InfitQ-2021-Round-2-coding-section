"""
Consider a non-zero positive decimal number, innum, an integer inbase greater than 1 and print outnum, the maximum number of consecutive set of zeroes after converting innum to its inbase notation.

Print -1 if there exists no zero after conversion of innum.

Input format:

First line contains innum

Second line contains inbase

Read the input from the standard input stream

Output format:

Print outnum or -1 to the standard output stream

I/P==>68         O\P--->3
      2
explanation:
For the given inputs, innum & inbase, 68 and 2 respectively:

Converting 68 to base 2 yields 1000100. The maximum number of consecutive set of zeroes '1000100' is 3 and hence
the output.
"""
#CODE:2
N=int(input())
B=int(input())
bnum = ""
while N>0:
      di = int(N%B)
      if di<10:
            bnum += str(di)
      else:
            bnum += chr(ord('A')+di-10)
      N //= B
bnum = bnum[::-1]
if(bnum.count('0')==0):
      print(-1)
else:
      t = 0
      m = 0
      for i in range(len(bnum)):
            if (bnum[i] == '0'):
                  t += 1
            else:
                  if (m < t):
                        m = t
                  t = 0
      print(m)