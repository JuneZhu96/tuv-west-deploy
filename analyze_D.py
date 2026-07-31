import json, re, os
from collections import Counter

# Read D array from the same directory as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'D_array_raw.json')

with open(json_path, 'r', encoding='utf-8') as f:
    D = json.loads(f.read())

print(f'Total signals: {len(D)}')

# Date stats
dates = [s['date'] for s in D if s.get('date')]
dates_sorted = sorted(set(dates))
print(f'Date range: {dates_sorted[0]} to {dates_sorted[-1]}')

# Latest month
latest = max(dates)
latest_year = latest[:4]
latest_month_num = int(latest[5:7])
months_en = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
latest_month_name = months_en[latest_month_num]
print(f'Latest month: {latest_month_name} {latest_year}')

# By type
types = Counter(s.get('type', 'unknown') for s in D)
print(f'By type: {dict(types)}')

# By theme
themes = Counter(s.get('primary_theme', 'unknown') for s in D)
print(f'By theme: {dict(themes)}')

# By month
months = Counter(s['date'][:7] for s in D if s.get('date'))
print(f'By month: {dict(sorted(months.items()))}')

# Competitor signals details
comp = [s for s in D if s.get('type') == 'competitor']
print(f'\nCompetitor signals: {len(comp)}')
for c in sorted(comp, key=lambda x: x['date']):
    print(f"  {c['date']} | {c.get('title', '')[:100]}")

# ISO mentions
iso_9001 = sum(1 for s in D if '9001' in s.get('content', '') or '9001' in s.get('title', ''))
iso_14001 = sum(1 for s in D if '14001' in s.get('content', '') or '14001' in s.get('title', ''))
print(f'\nISO 9001 mentions: {iso_9001}')
print(f'ISO 14001 mentions: {iso_14001}')

# AI/Agent mentions  
ai_agent = sum(1 for s in D if 'Agent' in s.get('content', '') or '智能体' in s.get('content', '') or 'Agent' in s.get('title', '') or '智能体' in s.get('title', ''))
print(f'Agent/智能体 mentions: {ai_agent}')

# Key competitor mentions
for comp_name in ['SGS', 'BV', 'Bureau Veritas', 'Intertek', 'LRQA', '南德', 'DEKRA', 'Workday', 'Hone', 'HolonIQ', 'D2L']:
    c = sum(1 for s in D if comp_name in s.get('content', '') or comp_name in s.get('title', ''))
    if c > 0:
        print(f'{comp_name} mentions: {c}')

# West industry key events
print('\n--- West region key events (latest 25) ---')
west_ind = [s for s in D if s.get('primary_theme') == '西区重点产业']
for s in sorted(west_ind, key=lambda x: x['date'], reverse=True)[:25]:
    print(f"  {s['date']} | {s.get('title', '')[:100]}")

print('\n--- Latest competitor/theme signals (latest 15) ---')
comp_theme = [s for s in D if s.get('primary_theme') == '竞对情报']
for s in sorted(comp_theme, key=lambda x: x['date'], reverse=True)[:15]:
    print(f"  {s['date']} | {s.get('title', '')[:100]}")

# Key terms
for kw in ['换版', '转版', '过渡期', 'FDIS', 'AI培训', 'AI学习', '17024', '17065', '半导体', '芯片', '储能', '光伏', '新能源', '钙钛矿', '成渝', '西安', '长安', 'TISAX', 'IATF', '功能安全', '碳']:
    c = sum(1 for s in D if kw in s.get('content', '') or kw in s.get('title', ''))
    if c > 0:
        print(f'"{kw}" mentions: {c}')

# 莱茵 self mentions
tr_self = sum(1 for s in D if '莱茵' in s.get('content', '') or '莱茵' in s.get('title', '') or 'TUV Rheinland' in s.get('content', '') or 'TÜV莱茵' in s.get('content', ''))
print(f'\nTUV莱茵 self mentions: {tr_self}')

# Latest overall signals
print('\n--- Latest 15 signals (all) ---')
for s in sorted(D, key=lambda x: x['date'], reverse=True)[:15]:
    print(f"  {s['date']} | [{s.get('primary_theme', '?')}] {s.get('title', '')[:100]}")
