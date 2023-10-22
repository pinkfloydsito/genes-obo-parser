import obonet

def parse_obo_file(file_path) -> list[dict]:
    graph = obonet.read_obo(file_path)
    term_data = []

    for node_id, data in graph.nodes(data=True):
        term_data.append({
            'id': node_id,
            'name': data.get('name', ''),
            'namespace': data.get('namespace', ''),
            'definition': data.get('def', ''),
            'synonym': data.get('synonym', ''),
            'is_a': data.get('is_a', []),
        })

    return term_data