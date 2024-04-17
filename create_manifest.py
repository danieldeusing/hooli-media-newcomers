import os
import json

def format_name(directory_name):
    """Format directory name by inserting spaces before capital letters in concatenated words."""
    # Split at the first dash if the prefix is a number
    name_parts = directory_name.split('-', 1)
    if len(name_parts) > 1:
        directory_name = name_parts[1]

    # Insert space before capital letters
    formatted_name = ""
    for i, char in enumerate(directory_name):
        if char.isupper() and i != 0 and not directory_name[i - 1].isspace():
            formatted_name += ' '
        formatted_name += char
    return formatted_name

def get_directories_and_files(_path):
    """Return a manifest of directories and files."""
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

# Directory to scan
path = '.'

# Get the manifest
manifest = get_directories_and_files(path)

# JSON output
json_output = json.dumps(manifest, indent=4)

# Print to console
print(json_output)

# Write to file
with open('manifest.json', 'w') as file:
    file.write(json_output)
