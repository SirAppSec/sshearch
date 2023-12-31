import re
import os
import argparse


def delete_file(filepath):
    os.remove(filepath)
    print("File " + filepath + " deleted.")


def find_pattern_in_directory(
    pattern: str, directory: str, delete_prompt: bool = False, non_interactive=False
) -> None:
    regex = re.compile(pattern)
    try:
        for root, _, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                with open(filepath, "r", errors="ignore") as file:
                    contents = file.read()
                    if regex.search(contents):
                        print("Pattern found in file:" + filepath)
                        if delete_prompt:
                            if non_interactive:
                                delete_file(filepath)
                                continue
                            response = input(
                                filepath
                                + "Do you want to delete? (y/Y for yes, n/N for no): ",
                            )
                            if response.lower() == "y":
                                delete_file(filepath)
    except PermissionError:
        print("premission deneid " + filepath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Search for a pattern in files within a directory."
    )
    parser.add_argument(
        "--pattern",
        "-p",
        type=str,
        help="The pattern to search for.",
        default="BEGIN.*KEY",
    )
    parser.add_argument(
        "--directory",
        "-d",
        type=str,
        required=False,
        default="~/.ssh",
        help="The directory to search within.",
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Prompt to delete the file if the pattern is found.",
    )
    parser.add_argument(
        "--non-interactive",
        "-i",
        action="store_true",
        help="None interactive mode.",
    )
    args = parser.parse_args()

    find_pattern_in_directory(
        args.pattern, args.directory, args.delete, args.non_interactive
    )
