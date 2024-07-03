---
waltz:
  title: bakery_project3_milestone1_tokens
  display title: 1.7) Your Own Data
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: November 08 2022, 0439 PM
    modified: November 08 2022, 0604 PM
  files:
    path: bakery_project3_milestone1_tokens
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Using User Tokens

This project will be most useful to you if it's processing your own Canvas data. Like everything we do, letting your program access Canvas on your behalf comes with some risks (e.g., leaving your room increases the risk of accidentally swallowing a bug). We always accept some risks in order to get benfits, but we usually try to *manage* those risks appropriately. We don't want to make you afraid to use this power, but we want you to be careful and to use it intelligently. The most important caution is to ensure that nobody else has access to your user token. 

In particular, **never include the actual token in the source code of any of your programs.** Instead, follow this process:

1. First, in Thonny, click the "View" menu at the top of the window (top of the screen in Mac). Then click "Program Arguments" to make the `Program arguments` box appear near the top of the interface. Copy and paste your user token into the `Program arguments` box. This is a new way to get values into your program, as "arguments"!
2. Inside of your main `final_project.py` file, you can use the following code to retrieve the contents of the `Program arguments` box:

```python
import sys

my_user_token = sys.argv[1]
```

Use the `my_user_token` variable where needed (e.g., as an argument to your `main` function). You can also swap out your user token for a different name from the test data (e.g., `"annie"`) to quickly try out other values.

## Create Your User Token

**You do not need to do this step if you do not want to!** Accessing your own data is an optional feature of this project.

When you are ready to start accessing your own data, you can follow these instructions to get <a href="https://community.canvaslms.com/t5/Admin-Guide/How-do-I-manage-API-access-tokens-as-an-admin/ta-p/89" target=_blank>a user access token from Canvas</a>. Name the token whatever you want. Be sure to have the token expire after about a day: that will limit the possible damage in case someone gets your token. It's easy to just get a new one when the old one expires. (This is an example of the principle of "defense in depth": plan to protect the token, but have a backup in case that plan fails.)

Once you have the token, copy it somewhere secure that you will be able to find later (e.g., a local text file or password manager). Do *not* store the user token in your source code file. Remember, anyone with the token can impersonate you on Canvas, and who knows what damage they could do! Treat it like a password.

If you think your token may have been leaked accidentally, immediately delete the token and generate a new one. There is no cost to generating new tokens! Do so as you need to, to protect yourself. 