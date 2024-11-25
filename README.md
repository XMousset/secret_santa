## Overview

The **Secret Santa Organizer** is a Python tool designed to simplify the process of organizing a Secret Santa event. It allows users to randomly assign Secret Santa pairs from a group of people. The assignments are handled discreetly, ensuring no one knows who their Secret Santa is.

This tool operates using a `.csv` file (e.g., exported from Google Sheets), where participants can input their details directly. The assignments can be shared via email or as individual `.txt` files, making the process easy and secure.

**For full explanations on emails, see the appropriate section below**.

## How It Works

1. **Prepare the Input File**:
   - Use a `.csv` containing the columns in the example (be careful not to have any coma `,` inside this file as it will be used as separator).
   - **Exclusions** must contain the exact same names as there is in **Name**. Multiple names can be used, separated by a space ` `.
   - Example:

     | Name        | Email               | Exclusions       | Gifts ideas      |
     |-------------|---------------------|------------------|------------------|
     | Alice       | alice@example.com   |                  | Books            |
     | Bob         | bob@example.com     | Charlie          |                  |
     | Charlie     | charlie@example.com |                  | Cinema tickets   |
     | Daisy       | daisy@example.com   | Alice Bob        |                  |

2. **Update the `config.json` and personnalize your text**:
   - Replace at least `"sending address"` in the `config.json` file by your address registered in `yagmail`.
   - All text are written in `outputs.py` so feel free to change them.
   - If you change the columns names, be sure to modify them in `christmas_friends.py` and `test.py`.

3. **Test the assignments, export and emails**:
   - Make some test with `main.py` to check if everything works well (config: `"print attributions"`).
   - Try creating some `.txt` files (config: `"create .txt"`).
   - Try sending emails to yourself using (config: `test_email.py`).

4. **Share the Assignments**:
   - Everything should work fine at this point.


## Libraries

- `yagmail` and `keyring` for email sending


## Sending email with Python using `yagmail`

I suggest you to create a new gmail account for this purpose. You will always use the same with Python and you will not expose your real account. You need to register your email and password into `yagmail` only once to send email (therefore, once done, you don't need to write your password directly in the code). But this password **IS NOT** the password of your gmail account. This password used by `yagmail` is unique and given by your gmail account specifically for this usage.

### **Protocol for getting your password**:
1) **Get a 2-step Verification for your account** (e.g. add a phone number)
2) **Go to *app passwords*** - *search "app" if you don't find it, the link should be:* myaccount.google.com/apppasswords
3) **Set a name for the password** (e.g. *Python yagmail*) - *This step is **blocked** if your account doesn't have a 2-step Verification*
4) **Copy the password** - *be careful, it cannot be seen again afterward, but can be deleted of course*

There are many tutorials for this on the web (e.g. *Google Gmail Remove Allow Less Secure Apps Option Alternative Solution* by **Geeky Shows**). When you have your password, follow these steps **ONE TIME** in order to be able to send email.

### **Python implementation**:
1) Install `yagmail` and `keyring`.
2) Register you email address and password : `yagmail.register("your-python-email@gmail.com", "yourpassword")`.
3) Put `"your-python-email@gmail.com"` in config:"sending address".
4) Test if you can send an email to one of your email adress with `test_email.py`.

Now you can use `yagmail` without explicitely write your password in your code as the following example :
```
mail = yagmail.SMTP("your-python-email@gmail.com")
mail.send("receiver@example.com", "Test yagmail python", "Hello World")
mail.close()
```

To delete a password, use `keyring.delete_password("yagmail", "your-python-email@gmail.com")`.

## Acknowledgement
This code takes its inspiration from `santa` by **jarhill0** - [PyPI](https://pypi.org/project/santa/) - [GitHub](https://github.com/jarhill0/santa)