# Speech Recognition Assistant

This is a Python-based speech recognition assistant that listens to voice commands and responds accordingly. It can search the web, check the time, and interact through speech synthesis.

## Features
- Speech recognition using `speech_recognition` library
- Voice responses using Google Text-to-Speech (`gTTS`)
- Web search capabilities (Google, YouTube, Maps)
- Simple voice-based assistant with predefined commands

## Requirements
Before running the program, ensure you have the necessary dependencies installed:

```sh
pip install speechrecognition gtts playsound3
```

Additionally, you may need to install `pyaudio` for microphone input:

```sh
pip install pyaudio
```

If you encounter errors with `pyaudio`, install it manually:

```sh
# Windows
pip install pipwin
pipwin install pyaudio

# macOS
brew install portaudio
pip install pyaudio
```

## Usage
Run the script using Python:

```sh
python speech_recognition.py
```

Once started, the assistant will prompt you with:

```
How can I help you?
```

You can then give voice commands, such as:
- **"What is your name?"** → Assistant responds with its name.
- **"What time is it?"** → Assistant announces the current time.
- **"Search"** → Assistant asks for a search query and opens Google.
- **"YouTube"** → Assistant asks for a search query and opens YouTube.
- **"Location"** → Assistant asks for a location and opens Google Maps.
- **"Exit"** → Ends the program.

## File Structure
```
├── main.py  # Main script
├── README.md              # Project documentation
```

## Potential Issues
- If the microphone is not detected, check system permissions.
- If `pyaudio` fails to install, try installing manually as shown above.
- If `playsound3` does not work, consider replacing it with `playsound`.

## Contributions
Feel free to contribute by improving the assistant's capabilities. Fork the repository, make changes, and submit a pull request.

## License
This project is open-source and available under the MIT License.
