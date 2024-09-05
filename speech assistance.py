import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# Function to continuously listen for any spoken commands
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for the next command...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            # Listen for a command
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print(f"Detected command: {command}")
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected. Waiting for command...")
        except sr.UnknownValueError:
            print("Could not understand the command. Please repeat.")
        except sr.RequestError as e:
            print(f"Could not request results from the service; {e}")

# Function to listen continuously for the wake word
def listen_for_wake_word():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Listening for 'Hey Buddy'...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            command = command.lower()

            print(f"Detected: {command}")

            # Check if "Hey Buddy" was mentioned
            if "hey buddy" in command:
                print("Wake word detected! Now listening for further commands...")
                return True
            else:
                print("Wake word not detected. Listening again...")
                return False
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected. Listening again...")
            return False
        except sr.UnknownValueError:
            print("Could not understand the audio. Listening again...")
            return False
        except sr.RequestError as e:
            print(f"Could not request results from the service; {e}")
            return False

# Main function to keep the mic on after the wake word is detected
def main():
    while True:
        # Listen for the wake word first
        if listen_for_wake_word():
            # Once the wake word is detected, keep listening for further commands
            while True:
                listen_for_command()

# Run the main function
if _name_ == "_main_":
    main()