import markdown

def text_replace_md(file_path):

    with open(file_path, "r", encoding="utf-8") as md_file:
        text = md_file.read()

    print(text)

    return 0

text_replace_md(r"Uncleaned_Files\Barbarian.md")