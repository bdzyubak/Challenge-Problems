def group_by_owners(files):
    grouped = dict()
    for file, owner in files.items():
        if owner in grouped:
            grouped[owner].append(file)
        else:
            grouped[owner] = [file]
    return grouped


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))