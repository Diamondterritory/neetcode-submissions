class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = []
        for i in s:
            if (ord('a') <= ord(i) <= ord('z')) or (ord('A') <= ord(i) <= ord('Z')) or (ord('0') <= ord(i) <= ord('9')):
                cleaned_s.append(i.lower())

        print(''.join(cleaned_s))
        
        clean_len = len(cleaned_s)
        for j in range(clean_len):
            if cleaned_s[j] != cleaned_s[clean_len-j-1]:
                return False
        
        return True