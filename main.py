from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

DIR = os.environ.get("DIR")
FILE = os.environ.get("FILE")

# def rename_on_one_file(absolute_path):
#     with open(absolute_path, "r") as f:
#         lines = f.readlines()


def rename_on_one_folder(absolute_path, finder, replacer):
    directory = os.listdir(absolute_path)

    for file in directory:
        file = DIR + file

        print(f"Converting { file }")

        with open(file, "r") as f:
            lines = f.read()
        lines = lines.replace(finder, replacer)

        with open(file, "w") as f:
            f.write(lines)


if __name__ == "__main__":
    # rename_on_one_file(DIR + FILE)
    finder = input("Text to find: ")
    replacer = input("Text to replace: ")
    rename_on_one_folder(DIR, finder, replacer)
