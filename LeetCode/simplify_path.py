def simplifyPath(path: str) -> str:
    path_members = path.split('/')
    new_path = list()
    for member in path_members:
        if member == '..':
            if new_path:
                new_path.pop()
        elif member == '.' or member == '':
            continue
        else:
            new_path.append(member)
    new_path = '/' + '/'.join(new_path)

    return new_path


path = "/home/"
assert simplifyPath(path) == path
