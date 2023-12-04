import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def greet():
    return "Hello! How can I assist you today?"

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}"

def get_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return f"Today is {current_date}"

def search_web(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def main():
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Initialize speech recognition
    recognizer = sr.Recognizer()

    # Greet the user
    engine.say(greet())
    engine.runAndWait()

    while True:
        try:
            # Listen for user input
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                print("Recognizing...")

            # Recognize speech using Google Speech Recognition
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)

            # Perform actions based on user commands
            if "hello" in command:
                response = greet()
            elif "time" in command:
                response = get_time()
            elif "date" in command:
                response = get_date()
            elif "search" in command:
                query = command.replace("search", "").strip()
                response = f"Searching the web for {query}..."
                search_web(query)
            elif "exit" in command:
                response = "Goodbye!"
                engine.say(response)
                engine.runAndWait()
                break
            else:
                response = "I'm sorry, I didn't understand that."

            # Speak the response
            engine.say(response)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()
