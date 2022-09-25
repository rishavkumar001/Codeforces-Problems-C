s=input()
p=0
l=[]
for i in range(26):
    l.append([])
for i in range(1,len(s)-1):
    l[ord(s[i])-97].append(i+1)
    if ord(s[0])<ord(s[-1]):
        for j in range(ord(s[0]),ord(s[-2])):
            p=p+len(l[chr(j)])
        print(ord(s[-1])-ord(s[0]),end=" ")
        print(p+2)
        print(1,end=" ")



   for(int i=1;i<s.size()-1;++i)
      Q[s[i]].push_back(i+1);
   if(s[0]<s[s.size()-1]) {
      for(char i=s[0];i<=s[s.size()-1];++i)
         P+=Q[i].size();
      cout << s[s.size()-1]-s[0] << ' ' << P+2 << endl;
      cout << 1 << ' ';
      for(char i=s[0];i<=s[s.size()-1];++i)
         for(int j:Q[i])
            cout << j << ' ';
      cout << s.size() << endl;
      
   } else {
      for(char i=s[0];i>=s[s.size()-1];--i)
         P+=Q[i].size();
      cout << s[0]-s[s.size()-1] << ' ' << P+2 << endl;
      cout << 1 << ' ';
      for(char i=s[0];i>=s[s.size()-1];--i)
         for(int j:Q[i])
            cout << j << ' ';
      cout << s.size() << endl;
      
   }
}

for _ in range(int(input())):
