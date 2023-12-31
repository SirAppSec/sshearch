
# Key Pattern Search and Delete Tool

This CLI tool searches for a specific regex pattern within all files in a given directory and optionally prompts to delete the file if the pattern is found.

This CLI tool was made durin BsidesLV23 Pros vs Joes ctf.

## Usage

### Search Pattern in Directory

Run the script with the directory as the argument to search for the default pattern `"BEGIN.*KEY"`:

```bash
which python3
sudo apt-get install git
git clone https://github.com/impoSTARS/sshearch
cd sshearch
sudo su

python3 search.py -d / --delete --non-interactive
python search.py
python search.py -d /home/umlal/.ssh
```

Single line to deploy:
```bash
 which python3 && sudo apt-get install -y git && git clone https://github.com/impoSTARS/sshearch && cd sshearch && sudo python3 search.py -d / --delete --non-interactive
 ```
Search Custom Pattern in Directory

You can also specify a different pattern to search:

```bash

python search.py -p regexpattern -d directory
```
Search and Prompt to Delete Files

To search for the pattern and prompt to delete any files where the pattern is found, use the --delete option:

```bash

python search.py -d /home/umlal/.ssh --delete
```
If the pattern is found, you will be prompted with a question asking if you want to delete the file. Type 'y' or 'Y' to confirm the deletion, or 'n' or 'N' to skip to the next file.
Warning

When using the --delete option, ensure that you have proper permissions and understand that the files will be forcibly deleted without recovery. Use this option with caution.
Requirements

Python 3.x



