Certainly! Here's the README.md content that explains the updated functionality of the script:

markdown

# Key Pattern Search and Delete Tool

This CLI tool searches for a specific regex pattern within all files in a given directory and optionally prompts to delete the file if the pattern is found.

## Usage

### Search Pattern in Directory

Run the script with the directory as the argument to search for the default pattern `"-----BEGIN \*. KEY-----"`:

```bash
python search_key.py "/home/umlal/.ssh"

Search Custom Pattern in Directory

You can also specify a different pattern to search:

```bash

python search_key.py "your-custom-regex-pattern" "/home/umlal/.ssh"
```
Search and Prompt to Delete Files

To search for the pattern and prompt to delete any files where the pattern is found, use the --delete option:

```bash

python search_key.py "/home/umlal/.ssh" --delete
```
If the pattern is found, you will be prompted with a question asking if you want to delete the file. Type 'y' or 'Y' to confirm the deletion, or 'n' or 'N' to skip to the next file.
Warning

When using the --delete option, ensure that you have proper permissions and understand that the files will be forcibly deleted without recovery. Use this option with caution.
Requirements

Python 3.x


This README.md file outlines how to use the script, including the new deletion prompt functionality, and provides warnings and requirements for using the script.

