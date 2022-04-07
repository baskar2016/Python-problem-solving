
def longestPalindrome(s):
 
    # base case
    if not s or not len(s):
        return ''
 
   
    freq = {}
 
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
 
    left = ''                   # stores left substring
    mid = ''
 
  
    for ch, count in freq.items():
 
        if count % 2 == 1:
            mid = ch            # stores odd character
 
        for i in range(count // 2):
            left += ch
 
  
    right = left[::-1]
 
    
    return left + mid + right
 
 
if __name__ == '__main__':
 
    s = input("enter a word :")
    print('The longest palindrome is', longestPalindrome(s))