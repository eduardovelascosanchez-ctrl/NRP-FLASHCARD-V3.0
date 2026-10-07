"""Actualiza los datos embebidos de index.html. No valida exactitud médica."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
data = json.loads((root / 'contenido.json').read_text(encoding='utf-8'))
assert isinstance(data['lessons'], list) and isinstance(data['cards'], list)
lesson_ids = {l['n'] for l in data['lessons']}
assert len(lesson_ids) == len(data['lessons']), 'Lecciones duplicadas'
ids = [c['id'] for c in data['cards']]
assert len(ids) == len(set(ids)), 'Identificadores duplicados'
for card in data['cards']:
    assert card['lesson'] in lesson_ids, 'Lección no encontrada'
    for field in ['id', 'title', 'kind', 'case', 'end', 'origin']:
        assert isinstance(card[field], str), field
    assert all(len(step) == 3 for step in card['steps']), 'Cada fase requiere tres campos'
html_path = root / 'index.html'
html = html_path.read_text(encoding='utf-8')
start_tag = '<script id="data" type="application/json">'
start = html.index(start_tag) + len(start_tag)
end = html.index('</script>', start)
payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
updated = html[:start] + payload + html[end:]
import re
updated = re.sub(r'\d+ tarjetas ·', str(len(ids)) + ' tarjetas ·', updated)
updated = re.sub(r'(<progress id="progress" max=")\d+', lambda m: m[1] + str(len(ids)), updated)
html_path.write_text(updated, encoding='utf-8')
print(f'Actualizadas {len(ids)} tarjetas. Revisar el contenido clínico antes de distribuir.')
