"""
In the <adjective1> land of <place>, a <animal> was feeling <emotion>. The <animal> lost its <object>.

Suddenly, a <character> appeared. 'I will help you find your <object>, <animal>’ - he said'.

Together, they journeyed through <terrain> and faced the <weather_condition>. Finally, they
found the <object> in a <place2>. The <animal> was so <emotion2> and thanked the
<character>. They lived <adverb> ever after.
"""

import re

with open("story.txt", 'r') as f:
    story = f.read()

print("\nNow we going to create a story. For this we need to replace tags.\n")

tags = sorted(set(re.findall(r'<\w+>', story)))

for i in tags:
    story = re.sub(i, input(f"Enter {i}: "), story)

print(f"\nHere's your story:\n{story}")
