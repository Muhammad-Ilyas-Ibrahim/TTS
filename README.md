# TTS (Text to Speech)

This project provides a simple graphical user interface (GUI) for converting text to speech using Python's `pyttsx3` library and `tkinter` for the interface. The application allows users to enter text, choose a voice and speech speed, and then convert the text to speech. Users can also save the speech output as an MP3 file.

## Features

- **Text-to-Speech Conversion**: Converts entered text to speech with the selected voice and speed.
- **Voice Selection**: Choose between "Microsoft David" and "Microsoft Zira" voices.
- **Speed Control**: Set the speech speed to Slow, Normal, or Fast.
- **Save as MP3**: Save the converted speech to an MP3 file.
- **Clear Text**: Clear the entered text.
- **Exit**: Close the application.

## Requirements

- Python 3.x
- `pyttsx3` library

To install the required library, run:
```bash
pip install pyttsx3
```

## Usage

1. **Run the Application**: Execute the Python script to start the application.
2. **Enter Text**: Type the text you want to convert to speech in the text field.
3. **Select Voice and Speed**: Choose the desired voice and speed from the dropdown menus.
4. **Convert Text**: Click the "Convert" button to hear the speech.
5. **Save as MP3**: Click the "Save As" button to save the speech output as an MP3 file.
6. **Clear Text**: Click the "Clear" button to remove the text from the field.
7. **Exit**: Click the "Exit" button to close the application.

## Notes

- Ensure that the `Images` folder contains the required image files for the buttons (`Button1.png`, `Button2.png`, `Button3.png`, `Button4.png`).
- The application uses Microsoft voices installed on the system. Adjust the `voice_id` paths if necessary to match available voices on your system.

Feel free to modify the content as needed!
