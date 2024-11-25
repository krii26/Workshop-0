def generate_permutations(s):
    if len(s) == 1:
        return [s]
    
    permutations = set()
    
    for i in range(len(s)):
        current_char = s[i]
        remaining_str = s[:i] + s[i+1:]
        
        for perm in generate_permutations(remaining_str):
            permutations.add(current_char + perm)
    
    return list(permutations)

print(generate_permutations("abc"))
print(generate_permutations("aab"))