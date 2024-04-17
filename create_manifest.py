import os
import json


def format_name(directory_name):
    """Inserts spaces before capital letters to format concatenated words, unless they are acronyms."""
    name_parts = directory_name.split('-', 1)
    if len(name_parts) > 1:
        directory_name = name_parts[1]

    formatted_name = directory_name[0]
    for i in range(1, len(directory_name)):
        if (directory_name[i].isupper() and
            not directory_name[i-1].isspace() and
            not directory_name[i-1].isupper()):
            formatted_name += ' '
        formatted_name += directory_name[i]
    return formatted_name


def get_directories_and_files(_path):
    """Builds a manifest of directories and files with formatted names."""
    _manifest = {"folders": []}
    for item in os.listdir(_path):
        full_path = os.path.join(_path, item)
        if os.path.isdir(full_path) and item.split('-')[0].isdigit():
            files = [f for f in os.listdir(full_path)
                     if f.split('-')[0].isdigit() and os.path.isfile(os.path.join(full_path, f))]
            _manifest['folders'].append({
                "name": format_name(item),
                "path": item,
                "files": files
            })
    return _manifest


path = '.'

manifest = get_directories_and_files(path)

json_output = json.dumps(manifest, indent=4)

with open('manifest.json', 'w') as file:
    file.write(json_output)
