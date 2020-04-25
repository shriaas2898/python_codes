''' function returns unique letters in sring s1 and s2
'''
unique_letters(s1,s2):
      return (set(s1)|set(s2)) - (set(s1)&set(s2))
