import os
import glob
import re

pattern = re.compile(r'(<div class="flex items-center gap-3 ml-4 2xl:ml-8">.*?</div>)\s*(<div class="flex gap-2 ml-3 2xl:ml-4 desktop-toggle-group">.*?</div>)', re.DOTALL)

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    def repl(m):
        g1 = m.group(1).replace('ml-4 2xl:ml-8', 'ml-3 2xl:ml-4')
        g2 = m.group(2).replace('ml-3 2xl:ml-4', 'ml-4 2xl:ml-8')
        return g2 + '\n\n                ' + g1

    new_content, count = pattern.subn(repl, content)
    if count > 0:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {f}')
