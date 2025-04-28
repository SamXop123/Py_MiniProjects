
import emoji

print("Output: ", emoji.emojize(input("Input: ").strip(), language="alias"))

# ============================================

# OR if you are having trouble understanding above code :

import emoji  

user_input = input("Input: ").strip()  

output = emoji.emojize(user_input, language="alias")  

print("Output:", output)  
