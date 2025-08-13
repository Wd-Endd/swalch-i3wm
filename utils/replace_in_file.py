
def replace_in_file(file, old, new):
    content = "";
    with open(file, "r") as f:
        content = f.read();
        condition = not old in content
        if condition:
            raise Exception(f"Warn: character '{old}' is not found in {file}")

    content = content.replace(old, new)
    with open(file, "w") as f:
        f.write(content)
