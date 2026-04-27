from flask import Flask, request, jsonify, send_file
import json
import os

app = Flask(__name__)

# Load the deterministic tree from JSON
def load_tree():
    with open('reflection-tree.json', 'r', encoding='utf-8') as f:
        return json.load(f)

tree_data = load_tree()
node_dict = {node['id']: node for node in tree_data}

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/api/start', methods=['GET'])
def start_tree():
    start_node = node_dict.get('START')
    return jsonify(start_node)

@app.route('/api/next', methods=['POST'])
def next_node():
    data = request.json
    current_id = data.get('current_id')
    answer = data.get('answer', '')
    history = data.get('history', {}) # {node_id: answer}
    signals = data.get('signals', {}) # {axis1: "internal", ...}

    if current_id not in node_dict:
        return jsonify({"error": "Node not found"}), 404

    current_node = node_dict[current_id]
    
    next_id = None
    
    if current_node.get('target'):
        next_id = current_node['target']
    else:
        children = [n for n in tree_data if n.get('parentId') == current_id]
        
        for child in children:
            if child['type'] == 'decision':
                for option in child.get('options', []):
                    if ':' in option:
                        condition, target = option.split(':', 1)
                        if condition.startswith('answer='):
                            accepted_answers = condition.split('=')[1].split('|')
                            if answer in accepted_answers:
                                next_id = target
                                break
                if next_id:
                    break
            else:
                next_id = child['id']
                break

    if not next_id:
        next_id = "END"

    next_node_data = node_dict.get(next_id)
    
    # Text Interpolation
    if next_node_data and '{' in next_node_data['text']:
        text = next_node_data['text']
        for k, v in history.items():
            text = text.replace(f"{{{k}.answer}}", str(v))
        
        text = text.replace("{axis1}", signals.get('axis1', 'neutral'))
        text = text.replace("{axis2}", signals.get('axis2', 'neutral'))
        text = text.replace("{axis3}", signals.get('axis3', 'neutral'))
        
        # We don't mutate the global dict permanently, just return it modified
        response_node = next_node_data.copy()
        response_node['text'] = text
        return jsonify({"node": response_node})

    return jsonify({"node": next_node_data})

if __name__ == '__main__':
    app.run(debug=True)
