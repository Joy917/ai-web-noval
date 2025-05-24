# Web Novel Writing Project

## Overview
This project is designed to assist writers in creating web novels by providing tools for generating character outlines, writing chapters, and editing content. The project is structured into three main layers: code, configuration, and output.

## Project Structure
```
web-novel-writing-project
├── code
│   ├── character_outline_generator.py
│   ├── chapter_writer.py
│   └── editor_verifier.py
├── config
│   ├── settings.yaml
│   └── prompts
│       ├── outline_prompt.txt
│       ├── chapter_prompt.txt
│       └── edit_prompt.txt
├── output
│   ├── outlines
│   │   └── [Outline] Title (Summary) - Date.txt
│   ├── chapters
│   │   └── [Chapter] Title (Summary) - Date.txt
│   └── edits
│       └── [Chapter] Title (Summary) - Date.txt
└── README.md
```

## Components

### Code Layer
- **character_outline_generator.py**: Contains the logic for generating character story outlines. It includes a function `generate_outline` that takes character details and generates a structured outline based on predefined templates.
  
- **chapter_writer.py**: Responsible for writing web article chapters. It exports a function `write_chapter` that takes an outline and generates a chapter, saving it in the specified format.

- **editor_verifier.py**: Handles the editing and verification process. It exports a function `verify_edit` that takes a chapter and provides feedback or suggestions for improvement.

### Configuration Layer
- **settings.yaml**: Contains configuration settings for the project, such as output paths and model parameters.

- **prompts**: This directory includes various prompt files used to guide the model in generating outlines, writing chapters, and editing content.
  - **outline_prompt.txt**: Prompts for generating outlines.
  - **chapter_prompt.txt**: Prompts for writing chapters.
  - **edit_prompt.txt**: Prompts for the editing process.

### Output Layer
- **outlines**: Directory for storing generated outlines, with files named according to the format: `[Outline] Title (Summary) - Date.txt`.

- **chapters**: Directory for storing written chapters, following the naming convention: `[Chapter] Title (Summary) - Date.txt`.

- **edits**: Directory for storing edited chapters, adhering to the same file format.

## Usage
1. Configure the project settings in `config/settings.yaml`.
2. Use `character_outline_generator.py` to create character outlines.
3. Write chapters using `chapter_writer.py` based on the generated outlines.
4. Edit and verify chapters with `editor_verifier.py`.

## Installation
Ensure you have the necessary dependencies installed. You can set up a virtual environment and install the required packages as specified in the project documentation.

## Contribution
Feel free to contribute to the project by submitting issues or pull requests. Your feedback and suggestions are welcome!