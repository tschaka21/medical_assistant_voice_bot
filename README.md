# medical_assistant_voice_bot
Overview
The AI Assistant is a voice-based interactive system that leverages AssemblyAI for real-time transcription, OpenAI for generating AI responses, and ElevenLabs for converting text to speech. It simulates a medical receptionist that interacts with users by asking about symptoms, recommending doctors, and managing appointments.

Features
- Real-time transcription of user input
- AI-driven responses using OpenAI's GPT-3.5-turbo model
- Text-to-speech conversion using ElevenLabs
- Simulated medical receptionist functionalities

Prerequisites
- Python 3.7 or higher
- Microphone connected to the system


Code Explanation
AI_Assistant Class
Initialization:
Sets up API keys for AssemblyAI, OpenAI, and ElevenLabs.

start_transcription:
Initializes and starts real-time transcription using AssemblyAI.

stop_transcription:
Stops the transcription session.

on_open:
Called when the transcription session opens.

on_data:
Processes transcription data. If it's a final transcript, it generates an AI response.

on_error:
Handles errors during transcription.

on_close:
Called when the transcription session closes.

generate_ai_response:
Sends the transcribed text to OpenAI for generating a response, then converts the response to speech.

generate_audio:
Uses ElevenLabs to convert AI response text into speech and streams it.

Troubleshooting
API Key Issues: Ensure your API keys are correct and have the necessary permissions.
Microphone Issues: Verify your microphone is working and accessible by the system.
Dependencies: Ensure all required packages are installed correctly.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Contributions are welcome. Please fork the repository and submit a pull request for review.

Acknowledgements
AssemblyAI
OpenAI
ElevenLabs

Credits
This project was created following the tutorial available at YouTube. https://www.youtube.com/watch?v=Nyo5m_glZXs&list=TLPQMDEwNzIwMjS0GD3gd5v-Fg&index=3

