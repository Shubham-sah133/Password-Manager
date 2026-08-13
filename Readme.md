# 🔐 Password Manager

A simple **command-line Password Manager** built with Python. This project allows users to save, view, update, and generate passwords through an interactive menu-driven interface.

The application stores password data locally in a `password.txt` file and uses Python's `secrets` module to generate random passwords.

---

## 🚀 Features

* 💾 Save passwords with a website/ID
* 👀 View saved passwords
* 🔑 Generate random passwords
* ✏️ Update existing passwords
* 💽 Store passwords in a local text file
* 🔄 Load previously saved passwords when the application starts
* ⚠️ Handle invalid menu input
* 🔢 Allow users to choose the generated password length

---

## 🛠️ Technologies Used

* **Python 3**
* `secrets`
* `string`
* Dictionary
* File Handling
* Exception Handling
* Loops
* Functions

---

## 📂 Project Structure

```text
PasswordManager/
│
├── password_manager.py
├── password.txt
├── .gitignore
└── README.md
```

> **Note:** `password.txt` contains locally stored password data and should not be uploaded to GitHub if it contains real credentials.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/PasswordManager.git
```

### 2. Navigate to the project directory

```bash
cd PasswordManager
```

### 3. Run the application

```bash
python password_manager.py
```

---

## 📋 Application Menu

```text
---------------PASSWORD MANAGER APP---------------

1 Save password
2 View password
3 Generate password
4 Update password
5 Exit
```

---

## 💾 Save Password

Select option `1`:

```text
Please Enter your ID: gmail
please Enter your password: mypassword123
```

The information is stored in the dictionary and saved to `password.txt`.

The data is stored in the following format:

```text
gmail:mypassword123
instagram:examplepassword
```

---

## 👀 View Passwords

Select option `2` to display all saved credentials.

Example:

```text
gmail : mypassword123
instagram : examplepassword
```

If no passwords are stored:

```text
Not found any data
```

---

## 🔑 Generate Password

Select option `3`.

The application asks for the required password length:

```text
How much length of password you need: 12
```

Example output:

```text
Generated password: x7@Kp2&Lm9#Q
```

The password is generated using Python's `secrets` module.

---

## ✏️ Update Password

Select option `4` and enter the ID/website:

```text
please enter the ID name first: gmail
please enter your new password: newpassword123
Your password updated successfully 😊
```

The updated password is stored in the dictionary and the `password.txt` file is rewritten with the latest data.

If the ID doesn't exist:

```text
Id not found
```

---

## 🧠 How the Data Is Stored

The application uses a Python dictionary:

```python
password = {}
```

Each website/ID is stored as a **key**, and its password is stored as the **value**.

For example:

```python
password = {
    "gmail": "mypassword123",
    "instagram": "insta456"
}
```

The application then writes these values to `password.txt`.

---

## 🔐 Password Generation

The password generator uses:

```python
secrets.choice()
```

instead of `random.choice()`.

The character set contains:

* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Example:

```python
chars = string.ascii_letters + string.digits + "@#&^%$%&/-+"
```

The user can choose the desired password length.

---

## ⚠️ Current Limitations

This is a **learning project** and is not intended to be used as a production password manager.

Current limitations include:

* Passwords are stored in plain text.
* Passwords are displayed in plain text.
* No master password/authentication system.
* No encryption of stored passwords.
* No delete-password option yet.
* Password length input is checked only for being numeric.
* Password file uses a simple `website:password` format.

---

## 🔮 Future Improvements

Possible improvements for future versions:

* 🔒 Encrypt stored passwords
* 🔑 Add a master password
* 🗑️ Add delete password functionality
* 🔍 Add search functionality
* 👁️ Hide passwords when displaying them
* ✅ Improve password validation
* 📏 Add minimum and maximum password length
* 🗄️ Replace the text file with SQLite
* 📝 Add proper logging and error handling
* 🖥️ Build a graphical interface using Tkinter

---

## 🧠 Concepts Practiced

This project helped me practice:

* Python dictionaries
* `while` loops
* `for` loops
* Functions
* File handling
* Reading and writing files
* Exception handling with `try-except`
* User input
* String manipulation
* `secrets` module
* `string` module
* Basic CRUD operations
* Persistent local data storage

---

## 👨‍💻 Author

**Shubham Kumar**

GitHub: https://github.com/Shubham-sah133

---

## ⭐ Support

If you found this project useful for learning Python, consider giving the repository a ⭐ on GitHub.
