# Password Manager

![Logo](logo.png)

A simple password manager built with Python and Tkinter. This tool allows you to generate, save, and retrieve passwords for different websites securely. The passwords are saved in a local JSON file and can be easily retrieved using the website name.

## Features
- **Password Generation**: Generate random, secure passwords with letters, numbers, and symbols.
- **Save Passwords**: Save website credentials securely in a JSON file.
- **Search Passwords**: Find saved passwords for websites and retrieve associated email/username details.
- **Clipboard Integration**: Automatically copies generated passwords to your clipboard for easy pasting.

## Requirements
- Python 3.x
- `pyperclip` module for clipboard support
- `tkinter` module for the graphical user interface
- `json` module for storing passwords securely

## How to Use
1. Enter the website name in the "Website" field.
2. Provide your email or username associated with the website in the "Email/Username" field.
3. Generate a password by clicking the "Generate Password" button, or manually input one.
4. Click "Add" to save the details to your password vault.
5. To retrieve stored passwords, enter the website name and click "Search."

## File Storage
- The passwords are saved in a local file named `password_manager.json`.
- If the file does not exist, it will be created the first time you save credentials.

## How to Run
1. Clone the repository or download the source code.
2. Install the required dependencies:
   ```bash
   pip install pyperclip
   ```
3.  Run the script:
   ```bash
   python main .py
   ```

---

Stay secure and keep your passwords safe with this simple Password Manager! 🔐
