import obonet

def parse_obo_file(file_path) -> list[dict]:
    graph = obonet.read_obo(file_path, ignore_obsolete=False)
    term_data = []

    for node_id, data in graph.nodes(data=True):
        if data == {}:
            continue

        term_data.append({
            'id': node_id,
            'name': data.get('name', ''),
            'namespace': data.get('namespace', ''),
            'definition': data.get('def', ''),
            'synonym': data.get('synonym', ''),
            'is_a': data.get('is_a', []),
            'alt_id': data.get('alt_id', []),
            'is_obsolete': data.get('is_obsolete', None) == 'true',
            'replaced_by': data.get('replaced_by', []),
            'consider': data.get('consider', []),
        })

    return term_data