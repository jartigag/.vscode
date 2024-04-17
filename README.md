# Getting started
In order to apply these settings:
- For your project, go to the folder where you usually clone your git repositories (your Workspace) and copy `.vscode/` there.
- For your user, go to `~/.config/Code/` (`%USERPROFILE%\AppData\Roaming\Code` in Windows) and copy the content of `User/*` there.

## Why bother
### About editor settings
```py
#TO-DO
```

### About formatting
Code is read much more often than it is written.
This is intended to improve the readability of code and make it consistent.

> Readability counts.
> 
> &nbsp;   &nbsp;   &nbsp; — PEP 20 - The Zen of Python

> Consistency with this style guide is important. However, know when to be inconsistent. Sometimes style guide recommendations just aren't applicable.
> When in doubt, use your best judgment. Look at other examples and decide what looks best. And don't hesitate to ask!
>
> In particular: do not break backwards compatibility just to comply with this PEP!
> 
> &nbsp;   &nbsp;   &nbsp; — PEP 8 - Style Guide for Python Code

## What's here
```sh
$ tree -a -I .git/ -I README.md
.
├── sample_script.snippet.conf
├── sample_script.snippet.py  
├── User/
│   └── snippets/
│       ├── conf.json   # sample .conf file,    just for illustration
│       └── python.json # sample .py file,      just for illustration
└── .vscode/
    └── .gitignore      # ref for python repos, adjust to suit yourself
```
