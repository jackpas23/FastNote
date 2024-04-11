# FastNote

## Introduction

FastNote is a lightweight and efficient application designed to streamline note-taking and note-management on Linux systems, specifically tailored for GNOME desktop environments. It allows users to quickly create, display, and clear notes through convenient keyboard shortcuts, making it an ideal tool for users who prefer keyboard navigation over mouse interactions.

## Features

- **Create Notes**: Instantly create a new note with a predefined keyboard shortcut.
- **Display Notes**: Easily view your existing notes in a single command.
- **Clear Notes**: Quickly clear your notes when necessary.

## Installation

To install FastNote, follow these steps:

1. **Clone the Repository**
   Clone the FastNote repository to your local machine using the following command:

   ```bash
   git clone https://github.com/yourusername/FastNote.git
   Navigate to the FastNote Directory
Change to the FastNote directory:

bash

cd FastNote

Run the Setup Script
Execute the setup script to configure FastNote on your system:

bash

    ./set-up.py

    During the setup, you will be prompted to enter the full path where you want to store your notes. Please provide the absolute path to ensure FastNote functions correctly.

Usage

Once installed, FastNote can be used with the following default keyboard shortcuts:

    Create Note: Ctrl + Shift + C - Creates a new note.
    Display Note: Ctrl + Shift + S - Displays the existing notes.
    Clear Note: Super + N - Clears the note content.

These shortcuts are configurable during the setup process.
Configuration

FastNote stores its configuration in a config.py file, where it keeps the path to the text file used for storing notes. If you need to change the location of the text file after installation, update the config.py file with the new path.
Dependencies

FastNote relies on the GNOME settings daemon for keyboard shortcuts, so it is primarily intended for use in GNOME environments.
Support

If you encounter any issues or have suggestions for improvements, please file an issue on the GitHub repository.
Contributing

Contributions to FastNote are welcome! If you have ideas for new features or improvements, feel free to fork the repository and submit a pull request.
