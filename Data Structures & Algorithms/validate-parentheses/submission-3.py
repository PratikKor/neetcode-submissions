class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        dir={"}":"{","]":"[",")":"("}
        ok=True
        for ch in s:
            if ch in dir:
                if st and st[-1]==dir[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
        return True if not st else False