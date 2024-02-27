import sys
from transformers import AutoTokenizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC  # Replace with your chosen model
from sklearn.metrics import accuracy_score
from json import dumps
from functions import fa

from colorama import Fore

import os


def extract_features(code):
    """
    Extracts features from a given code snippet.

    Args:
      code: String containing the Python code snippet.

    Returns:
      Dictionary containing extracted features.
    """
    # Tokenize the code
    tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
    tokens = tokenizer(code, return_tensors="pt")

    # Feature extraction
    features = {}

    # 2. Data structures
    data_structures = ["list", "dict", "set", "tuple"]
    features["data_structure_usage"] = [
        (tokens["input_ids"] == tokenizer.convert_tokens_to_ids(ds)).sum().item()
        for ds in data_structures
    ]

    # 3. Function calls
    function_calls = set()
    for token in tokenizer.convert_ids_to_tokens(
        tokens["input_ids"].squeeze().tolist()
    ):
        if "(" in token and token.split("(")[0] not in function_calls:
            function_calls.add(token.split("(")[0])
    features["num_function_calls"] = len(function_calls)

    # 4. Comments (optional, use with caution)
    comments = []
    features["num_loops"] = 0
    features["num_ifs"] = 0

    for line in code.splitlines():
        if "#" in line:
            comments.append(line.split("#")[-1].strip())
        if "for" in line or "while" in line:
            features["num_loops"] += 1
        if "if" in line:
            features["num_ifs"] += 1
    features["num_comments"] = len(comments)

    return features


# Example usage
code = "def my_sort(data):\n  # Bubble sort implementation\n  for i in range(len(data) - 1):\n    for j in range(len(data) - i - 1):\n      if data[j] > data[j + 1]:\n        data[j], data[j + 1] = data[j + 1], data[j]"
# Load and pre-process your code dataset (replace with your data source)
data = []
labels = []

alldata = {}


print(Fore.GREEN)
for root, dirs, files in os.walk(".", topdown=True):
    print(root)
    print(dirs)
    # print(files)
    print("--------------------------------")

    for file in files:
        ext = file.split(".")[-1]
        if ext == "py":
            print(file)


print(Fore.CYAN)
with open(sys.argv[1]) as f:
    data = f.read()
    print(extract_features(data))

    print(Fore.RED)
    print(fa(data))


print(Fore.WHITE)
