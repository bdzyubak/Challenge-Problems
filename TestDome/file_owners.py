# Implement a group_by_owners function that: Accepts a dictionary containing the file owner name for each file name.
# Returns a dictionary containing a list of file names for each owner name, in any order.
# For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}


def group_by_owners(files):
    by_owner = dict()
    for file, owner in files.items():
        if owner in by_owner:
            by_owner[owner].append(file)
        else:
            by_owner[owner] = [file]
    return by_owner


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))
