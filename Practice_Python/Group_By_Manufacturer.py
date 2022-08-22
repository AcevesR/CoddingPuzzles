from collections import defaultdict

def group_by_manufacturer(files):
    manufacturers = defaultdict(list)
    for file, manufacturer in files.items():
        manufacturers[manufacturer].append(file)
    return manufacturers

files = {
    'Model 3.txt': 'Tesla',
    'Mustang.text': 'Ford',
    'Model S.py': 'Tesla',
    'Grand Cherokee.py': 'Jeep'
}

print(group_by_manufacturer(files))
