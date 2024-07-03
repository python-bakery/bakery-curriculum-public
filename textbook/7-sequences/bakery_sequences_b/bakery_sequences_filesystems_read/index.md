---
waltz:
  title: bakery_sequences_filesystems_read
  display title: 7B1) Filesystems Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Filesystems
    youtube:
      Bart: o5Jq_eZzAlU
      Amy: bE7s1EY52tc
    small_layout: true
    hide_files: false
    summary: In this lesson, you will learn about your computer's File System. Files
      are an important part of making programs useful, because they allow us to persist
      information between runs of a program. Files are organized into directories
      within your file system, and are uniquely identified by paths.
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 7
    created: June 28 2022, 0300 PM
    modified: October 05 2022, 0906 AM
  files:
    path: bakery_sequences_filesystems_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## A System of Files

![A picture modeling someone's file system. At the top is a folder labeled "root", with three arrows pointing downwards at three other folders. The first folder is labeled "School work" and has two files below (a word document and a excel spreadsheet). The second folder is labeled "Photos" and has two picture files in it. The third folder is labeled "Python" and has two Python files in it.](bakery_sequences_filesystems_directories.png)

Your computer is equipped with a filesystem that lets you save and load files.
A file is simply a sequence of data, not unlike a string.
You create files all the time - text documents, pictures, music, python files, and so on.
These files are organized by your File System.

## Directories

* Directories == Folders
* Directories: A collection of files and directories

Directories, also known as folders, are a way to group files and other directories together.
Because we can put directories inside of directories, we end up with a hierarchical system.

## Paths

![The model from before, with three layers of files and folders, is shown. A blue line traces a route from the Root down to one of the Python files with the label "path" on it.](bakery_sequences_filesystems_path.png)

Think of files as a house.
Directories are neighborhoods, cities, states, and successively bigger ways to group houses.
Each file has a unique address within your file system called its "path".
We use these paths to navigate files and directories, just like we would houses and neighborhoods.

## Absolute Path

```
/root/python/example.py
/home/acbart/python/example.py
C:/Users/acbart/python/example.py
C:\\Users\\acbart\\python\\example.py
```

The full address for a file is known as its "absolute path".
The exact format of the path will depend on your platform, but typically they are a series of folder names separated by slashes. 
In Python, it is typically best to use forward slashes, since these tend to work regardless of the platform.
Otherwise, you need to escape the backslashes with extra backslashes.

## The Working Directory

```sh
>>> !pwd
'C:/Users/acbart/projects/pythonmisc'
```

Most modern programming environments, like Thonny, have a command line that let you interact with the file system.
These command lines have a **Current Working Directory**.
It's essentially "where you are" at the moment.
In Thonny, you can check your current directory using the `pwd` command with an exclamation mark in front of it.
PWD stands for Print Working Directory.
Note that this only only works in the Thonny command line, it's not actually a Python command.
In the regular command line, you would not need the exclamation mark either.

## Relative Paths

```
>>> !ls

Date        Time        Type  Size     Name
09/17/2017  09:41 PM    <DIR>          .
09/17/2017  09:41 PM    <DIR>          ..
09/12/2017  03:11 PM    <DIR>          photos
09/14/2017  05:34 PM    <DIR>          music
09/11/2017  02:45 PM    <DIR>          python
09/02/2016  06:08 PM             6,228 homework5.pdf
09/02/2016  06:08 PM             9,650 example.py
08/08/2015  07:43 PM           340,489 historyOfDogs.png
08/08/2015  07:44 PM           422,316 taxReturns.docx
```

If there are folders in your current working directory, you can reference them without writing the Absolute Path.
Instead, the folder's path is simply it's name.
You can see a list of the folders in your current directory by using the `ls` command.
`ls` stands for "list", as in "list the files".

## Moving between directories

```sh
# Absolute path:
# Move to specific folder anywhere in your file system
>>> !cd /c/Users/acbart/projects

# Relative path:
# Move to folder in current directory
>>> !cd pythonmisc/

# Move up a level
>>> !cd ../
```

To move from one directory to another, we use the `cd` command.
You can move to an absolute path or a relative path.
You can also move up a folder level by using a pair of periods.

## Commands

![A listing of the previously described commands and their meaning.](bakery_sequences_filesystems_command_table.png)

It can be tricky to remember these commands, but knowing how to use them will serve you well when you start working on larger projects.