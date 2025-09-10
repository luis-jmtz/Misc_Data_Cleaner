import markdown

def text_replace_md(file_path, find_text, replacement_text, new_path):
    '''
    This code takes a markdown file and effectively does a find and replace
    
    Parameters:
        file_path: the file path of the markdown file to modify
        find_text: the text you want to replace
        replacement_text: the text that will replace the find_text
        new_path: the path and name of the new file that gets created
    '''

    with open(file_path, "r", encoding="utf-8") as md_file:
        text = md_file.read()

    # print(text)
    text = text.replace(find_text, replacement_text)

    with open(new_path, 'w') as file:
        file.write(text)
