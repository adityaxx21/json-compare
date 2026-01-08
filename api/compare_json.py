import json
import sys
from typing import Any, Dict, List, Tuple, Set

def load_json(filepath: str) -> Any:
    """Load JSON data from a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from '{filepath}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading '{filepath}': {e}")
        sys.exit(1)

def flatten_json(y: Any, parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Recursively flatten a nested JSON object."""
    items: Dict[str, Any] = {}
    
    if isinstance(y, dict):
        for k, v in y.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, (dict, list)):
                items.update(flatten_json(v, new_key, sep=sep))
            else:
                items[new_key] = v
    elif isinstance(y, list):
        for i, v in enumerate(y):
            # Use bracket notation for list indices to distinguish from dict keys
            new_key = f"{parent_key}[{i}]"
            if isinstance(v, (dict, list)):
                items.update(flatten_json(v, new_key, sep=sep))
            else:
                items[new_key] = v
    else:
        # Primitive at root
        items[parent_key if parent_key else 'root'] = y
        
    return items

def compare_json(data_a: Any, data_b: Any) -> Tuple[List[Tuple[str, Any, Any]], List[str], List[str]]:
    """Compare two JSON objects and return differences."""
    flat_a = flatten_json(data_a)
    flat_b = flatten_json(data_b)
    
    keys_a = set(flat_a.keys())
    keys_b = set(flat_b.keys())
    
    all_keys = keys_a.union(keys_b)
    
    value_diffs = []
    only_in_a = []
    only_in_b = []
    
    for key in sorted(all_keys):
        if key in keys_a and key in keys_b:
            val_a = flat_a[key]
            val_b = flat_b[key]
            if val_a != val_b:
                value_diffs.append((key, val_a, val_b))
        elif key in keys_a:
            only_in_a.append(key)
        else:
            only_in_b.append(key)
            
    return value_diffs, only_in_a, only_in_b

def annotate_json(data: Any, diff_keys: Set[str], exclusive_keys: Set[str], parent_key: str = '', indent: int = 4) -> str:
    """
    Recursively serialize JSON to string with HTML highlighting for differences and exclusive keys.
    """
    spaces = ' ' * indent
    
    if isinstance(data, dict):
        if not data:
            return "{}"
        lines = []
        lines.append("{")
        for i, (k, v) in enumerate(data.items()):
            full_key = f"{parent_key}.{k}" if parent_key else k
            
            # Determine styling
            key_style = ""
            val_style = ""
            
            # If the specific leaf key matches, highlight
            # Note: For objects/lists, exact match on parent key usually means the whole subtree is missing/extra
            if full_key in diff_keys:
                 val_style = ' style="background-color: #ffe6e6; color: #cc0000; font-weight: bold;"'
            elif full_key in exclusive_keys:
                 key_style = ' style="background-color: #fff8e1; color: #e6a800; font-weight: bold;"'
                 val_style = ' style="background-color: #fff8e1; color: #e6a800;"'

            # Recursively format value
            formatted_value = ""
            if isinstance(v, (dict, list)):
                formatted_value = annotate_json(v, diff_keys, exclusive_keys, full_key, indent + 4)
            else:
                json_val = json.dumps(v, ensure_ascii=False)
                formatted_value = f'<span{val_style}>{json_val}</span>'

            # Format the key
            key_str = f'<span{key_style}>"{k}"</span>'
            
            line = f'{spaces}{key_str}: {formatted_value}'
            if i < len(data) - 1:
                line += ","
            lines.append(line)
        
        lines.append(' ' * (indent - 4) + "}")
        return "\n".join(lines)
    
    elif isinstance(data, list):
        if not data:
            return "[]"
        lines = []
        lines.append("[")
        for i, v in enumerate(data):
            # Construct key with index
            full_key = f"{parent_key}[{i}]"
            
            val_style = ""
            if full_key in diff_keys:
                 val_style = ' style="background-color: #ffe6e6; color: #cc0000; font-weight: bold;"'
            elif full_key in exclusive_keys:
                 # In a list, we don't have a "key" string to highlight, so we assume highlighting the value
                 val_style = ' style="background-color: #fff8e1; color: #e6a800;"'
            
            formatted_value = ""
            if isinstance(v, (dict, list)):
                formatted_value = annotate_json(v, diff_keys, exclusive_keys, full_key, indent + 4)
            else:
                json_val = json.dumps(v, ensure_ascii=False)
                formatted_value = f'<span{val_style}>{json_val}</span>'
                
            lines.append(f'{spaces}{formatted_value}' + ("," if i < len(data) - 1 else ""))
            
        lines.append(' ' * (indent - 4) + "]")
        return "\n".join(lines)
    else:
        return json.dumps(data, ensure_ascii=False)

def generate_markdown_report(value_diffs: List[Tuple], only_in_a: List[str], only_in_b: List[str], 
                           data_a: Any, data_b: Any, outfile: str = None) -> str:
    """Generate a Markdown report of the comparison results."""
    
    lines = []
    lines.append("# JSON Comparison Result")
    lines.append("")
    
    # Summary Section
    lines.append("## Summary Section")
    lines.append(f"- Total number of value differences: {len(value_diffs)}")
    lines.append(f"- Total keys only in json_a: {len(only_in_a)}")
    lines.append(f"- Total keys only in json_b: {len(only_in_b)}")
    lines.append("")
    
    # Table 1 - Value Differences
    lines.append("## Table 1 – Value Differences")
    if value_diffs:
        lines.append("| Key Path | json_a Value | json_b Value |")
        lines.append("|---|---|---|")
        for key, val_a, val_b in value_diffs:
            str_a = json.dumps(val_a, ensure_ascii=False).replace("|", "\\|")
            str_b = json.dumps(val_b, ensure_ascii=False).replace("|", "\\|")
            lines.append(f"| {key} | {str_a} | {str_b} |")
    else:
        lines.append("No value differences found.")
    lines.append("")

    # Table 2 - Key Differences
    lines.append("## Table 2 – Key Differences")
    if only_in_a or only_in_b:
        lines.append("| Key Path | Exists In |")
        lines.append("|---|---|")
        for key in only_in_a:
            lines.append(f"| {key} | json_a |")
        for key in only_in_b:
            lines.append(f"| {key} | json_b |")
    else:
        lines.append("No key differences found.")
    lines.append("")
    
    # Annotated JSON Views
    diff_keys = {d[0] for d in value_diffs}
    set_only_a = set(only_in_a)
    set_only_b = set(only_in_b)
    
    lines.append("## Annotated json_a")
    lines.append("> **Legend**: <span style='background-color: #ffe6e6; color: #cc0000; font-weight: bold;'>Red Value</span> = Mismatch, <span style='background-color: #fff8e1; color: #e6a800; font-weight: bold;'>Orange Key</span> = Only in A")
    lines.append("")
    lines.append("<pre><code>")
    lines.append(annotate_json(data_a, diff_keys, set_only_a))
    lines.append("</code></pre>")
    lines.append("")
    
    lines.append("## Annotated json_b")
    lines.append("> **Legend**: <span style='background-color: #ffe6e6; color: #cc0000; font-weight: bold;'>Red Value</span> = Mismatch, <span style='background-color: #fff8e1; color: #e6a800; font-weight: bold;'>Orange Key</span> = Only in B")
    lines.append("")
    lines.append("<pre><code>")
    lines.append(annotate_json(data_b, diff_keys, set_only_b))
    lines.append("</code></pre>")
    lines.append("")
    
    report_content = "\n".join(lines)
    
    if outfile:
        try:
            with open(outfile, 'w', encoding='utf-8') as f:
                f.write(report_content)
            print(f"Success! Report generated at '{outfile}'")
        except Exception as e:
            print(f"Error: Failed to write report to '{outfile}': {e}")
            sys.exit(1)
            
    return report_content

def main():
    file_a = 'json_a.json'
    file_b = 'json_b.json'
    output_file = 'result.md'
    
    print(f"Reading {file_a}...")
    data_a = load_json(file_a)
    
    print(f"Reading {file_b}...")
    data_b = load_json(file_b)
    
    print("Comparing...")
    diffs, only_a, only_b = compare_json(data_a, data_b)
    
    print("Generating report...")
    generate_markdown_report(diffs, only_a, only_b, data_a, data_b, output_file)

if __name__ == "__main__":
    main()
