import json, re, os

html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'market-competitor-intel-may-jul-2026.html')
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. D array still valid JSON?
match = re.search(r'var D=\[(.+?)\];$', content, re.DOTALL)
if match:
    D = json.loads('[' + match.group(1) + ']')
    print(f'OK D array valid: {len(D)} signals')
else:
    print('FAIL D array parse failed')

# 2. Check all patched sections
checks = [
    ('Date tag', 'May—Jul 2026'),
    ('Judgment#1', 'CNCA新政双重驱动'),
    ('Judgment#5', 'Workday(7/27)/Hone(7/28)'),
    ('Opp#1', '354条中换版/转版提及27次'),
    ('Opp#5', '成渝汽车8000亿集群'),
    ('Opp#6', '一证通全球'),
    ('Risk#4', 'Josh Bersin'),
    ('Risk#5', 'Anthropic 10城SMB巡讲'),
]
all_ok = True
for name, keyword in checks:
    ok = keyword in content
    print(f'{"OK" if ok else "FAIL"} {name}')
    if not ok:
        all_ok = False

# 3. HTML tag balance
ol_open = content.count('<ol>') + content.count('<ol ')
ol_close = content.count('</ol>')
ul_open = content.count('<ul>') + content.count('<ul ')
ul_close = content.count('</ul>')
balanced = ol_open == ol_close and ul_open == ul_close
print(f'{"OK" if balanced else "FAIL"} tag balance: ol {ol_open}/{ol_close} ul {ul_open}/{ul_close}')

print(f'File size: {len(content):,} bytes')
print(f'FINAL: {"ALL CHECKS PASSED" if all_ok and balanced else "SOME CHECKS FAILED"}')
