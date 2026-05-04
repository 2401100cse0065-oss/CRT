def Reverse_String(s:str) -> str:
   a=""
   for i in range(len(s)-1,-1,-1):
       a+=s[i]
   return a
   pass
if __name__ == "__main__":
    s = input()
    print(Reverse_String(s))
