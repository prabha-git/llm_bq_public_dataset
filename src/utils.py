import re

def preprocess_text_for_markdown(text: str) -> str:

    #Remove the text "Answer: " from the response
    text = text.replace("Answer: ", "")

    # Escape special Markdown characters
    # List of special characters in Markdown: \ ` * _ { } [ ] ( ) # + - . !
    special_chars = "\`*_{}[]()#+.!"
    for char in special_chars:
        text = text.replace(char, f"\\{char}")

    # Escape $ signs which are used for LaTeX math blocks in Markdown
    text = text.replace("$", "\\$")

    # Replace newlines with Markdown line breaks
    text = text.replace("\n", "  \n")

    return text


