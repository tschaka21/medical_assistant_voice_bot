import assemblyai as aai
from elevenlabs import generate, stream
from openai import OpenAI

class AI_Assistant:
    def __init__(self):
        aai.settings.api_key = "API_KEY"
        self.openai_client = OpenAI(api_key= "API_KEY")
        self.elevenlabs_api_key = "API_KEY"

        self.transcriber = None

        #prompt
        self.full_transcript = [{
            "role":"system", "content":"you are a assistant and ask what symptoms someone has, recommend a doctor and ask to book an appointment. Afterwards ask if you should book the appointment to the calendar, if you should remind one day before and book a cab to the location"

        }]

    ####step 2: Real-Tome Transcription with Assembly AI

    def start_transcription(self):
        self.transcriber = aai.RealtimeTranscriber(
            sample_rate=16000,
            on_data = self.on_data,
            on_error=self.on_error,
            on_open=self.on_open,
            on_close=self.on_close,
            end_utterance_silence_threshold=1000
        )

        self.transcriber.connect()
        microphone_stream = aai.extras.MicrophoneStream(sample_rate=16000)
        self.transcriber.stream(microphone_stream)

    def stop_transcription(self):
        if self.transcriber:
            self.transcriber.close()
            self.transcriber = None

    def on_open(self, session_opened: aai.RealtimeSessionOpened):
        "This function is called when the connection has been established."

        print("Session ID:", session_opened.session_id)
        return

    def on_data(self, transcript: aai.RealtimeTranscript):
        "This function is called when a new transcript has been received."

        if not transcript.text:
            return

        if isinstance(transcript, aai.RealtimeFinalTranscript):
            self.generate_ai_response(transcript)
        else:
            print(transcript.text, end="\r")

    def on_error(self, error: aai.RealtimeError):
        "This function is called when the connection has been closed."

        print("An error occured:", error)
        return

    def on_close(self):
        "This function is called when the connection has been closed."

        #print("Closing Session")
        return
    
#### Step 3: Pass real time transcript to OpenAI###

    def generate_ai_response(self, transcript):
        self.stop_transcription()

        self.full_transcript.append({"role":"user", "content":transcript.text})
        print(f"\nPatient: {transcript.text}", end="\r\n")

        response = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = self.full_transcript)

        ai_response = response.choices[0].message.content

        self.generate_audio(ai_response)
        self.start_transcription()
        
### Step 4: Generate Audio w Elevenlabs ###

    def generate_audio(self, text):

        self.full_transcript.append({"role":"assistant", "content": text})
        print(F"\nAI Receptionist: {text}")

        audio_stream = generate(
            api_key= self.elevenlabs_api_key,
            text=text,
            voice="Rachel",
            stream = True
        )

        stream(audio_stream)

greeting = "Hello and welcome to our medical service. How can I assist you today? Could you please describe your symptoms?"
ai_assistant = AI_Assistant()
ai_assistant.generate_audio(greeting)
ai_assistant.start_transcription()
