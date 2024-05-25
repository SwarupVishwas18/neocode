import re
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")
stop_words = nlp.Defaults.stop_words


def analyze_code(code):

    variable_names = re.findall(r"\b[a-z_][a-z0-9_]*\b =", code)
    class_names = re.findall(r"class (\w+)", code)
    function_names = re.findall(r"def (\w+)", code)

    total_variables = len(variable_names)
    if total_variables == 0:
        total_variables = 1
    meaningful_variables = 0

    upper_tokens = 0
    for var in variable_names:
        upper_label = False
        for i in var:
            if i.isupper():
                upper_label = True
        if upper_label == True:
            upper_tokens += 1

    for var in function_names:
        if var.islower():
            upper_tokens += 1

    title_token = 0

    for var in class_names:
        if var.istitle():
            title_tokens += 1

    for var in variable_names:
        doc = nlp(var)
        if len(doc[0]) > 1:
            if doc[0].text not in stop_words:
                meaningful_variables += 1

    total_class = len(class_names)
    meaningful_class = 0
    for var in class_names:
        doc = nlp(var)
        if doc[0].text not in stop_words:
            meaningful_class += 1

    total_functions = len(function_names)
    meaningful_functions = 0
    for var in function_names:
        doc = nlp(var)
        if doc[0].text not in stop_words:
            meaningful_functions += 1

    total_functions = len(function_names)
    functions_with_docstrings = 0
    for func in function_names:
        if '"""' in code or "'''" in code:
            functions_with_docstrings += 1

    comments = re.findall(r"#.*?\n", code)
    meaningful_comments = 0
    for comment in comments:
        words = word_tokenize(comment)
        if not any(word in stopwords.words("english") for word in words):
            meaningful_comments += 1

    total_tokens = (len(variable_names) + len(class_names) + len(function_names)) * 2
    meaningful_tokens = (
        meaningful_variables
        + meaningful_class
        + meaningful_functions
        + upper_tokens
        + title_token
    )

    readability_index = meaningful_tokens / total_tokens * 100

    print(f"Total variables: {total_variables}")
    print(f"Meaningful variable names: {meaningful_variables}")
    print(f"Functions and Variables with Lower Case: {upper_tokens}")
    print(f"Total classes: {total_class}")
    print(f"Meaningful class names: {meaningful_class}")
    print(f"Classes With Title Casing: {title_token}")
    print(f"Total functions: {total_functions}")
    print(f"Functions with docstrings: {functions_with_docstrings}")
    print(f"Meaningful comments: {meaningful_comments}")
    print(f"Readability index: {readability_index:.2f}%")

    return {
        "total_variables": total_variables,
        "meaningful_variables": meaningful_variables,
        "total_class": total_class,
        "meaningful_class": meaningful_class,
        "meaningful_functions": meaningful_functions,
        "total_functions": total_functions,
        "function_with_docstrings": functions_with_docstrings,
        "meaningful_comments": meaningful_comments,
        "readability_index": readability_index,
    }


if __name__ == "__main__":
    file_path = "code1.py"
    analyze_code(file_path)
