import markdown

def text_replace_md(file_path, find_text, replacement_text, new_file):

    with open(file_path, "r", encoding="utf-8") as md_file:
        text = md_file.read()

    # print(text)
    text = text.replace(find_text, replacement_text)

    with open(new_file, 'w') as file:
        file.write(text)

    print(text)

text_replace_md(r"Uncleaned_Files\Barbarian.md", "Barbarian", "Thug", "test2.md")