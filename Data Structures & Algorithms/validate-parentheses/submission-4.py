class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range(len(s)):
            if not st and  s[i] in '}])':
                return False
            else:
                if s[i] in "{([":
                    st.append(s[i])
                elif s[i]==")" and st[-1]=="(":
                    st.pop()
                elif s[i]=="]" and st[-1]=="[":
                    st.pop()
                elif s[i]=="}" and st[-1]=="{":
                    st.pop()
                else:
                    return False
        return len(st)==0

