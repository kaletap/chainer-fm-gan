"""
Given two files containing lines with separate sentences in different styles creates file structure needed by
make_csv.py.
"""

import os
import pathlib
import tarfile
import shutil

first_file = "yelp/sentiment.train.0"
second_file = "yelp/sentiment.train.1"
tmp_output_folder = "text"

PLACEHOLDER = "<PLACEHOLDER>\n"


def create_file(line, path):
    with open(path, "w") as f:
        f.write(PLACEHOLDER)
        f.write(PLACEHOLDER)
        f.write(line)
        f.write(PLACEHOLDER)


def create_folder(input_file, output_folder):
    # file_name becomes name of the subfolder
    subfolder_name = os.path.split(input_file)[-1]
    path = os.path.join(output_folder, subfolder_name)
    print("Creating files in {}".format(path))
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    with open(input_file) as f:
        for i, line in enumerate(f.readlines()):
            file_path = os.path.join(path, str(i) + ".txt")
            create_file(line, file_path)


if __name__ == "__main__":
    create_folder(first_file, tmp_output_folder)
    create_folder(second_file, tmp_output_folder)
    with tarfile.open("data.tar.gz", "w:gz") as tar:
        tar.add(tmp_output_folder)
    shutil.rmtree(tmp_output_folder)


