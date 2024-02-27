word_list = []
alphabet = ['A', 'E', 'I', 'O', 'U']

def dfs(i, word):
    
    word_list.append(word)
    if i == 5:
        return

    for j in range(5):
        dfs(i+1, word + alphabet[j])
        
        
def solution(word):
        
    dfs(0, '')
    
    return word_list.index(word)