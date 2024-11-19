import speech_recognition as sr
import os

def voice_to_text():
    """Convert voice input to text."""
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("\nAdjusting for better noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening... Speak now!")
            
            try:
                
                recognizer.pause_threshold = 2  
                audio = recognizer.listen(source)
                print("Recognizing...")
                
                
                text = recognizer.recognize_google(audio)
                print(f"\nYou said: {text}")
                
               
                with open("output.txt", "a") as file:
                       file.write(f"{text}\n")

                print("Text saved to 'output.txt'.\n")
                print("Thankyou For Using me - Robo")
                
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that. Please try again.")
            except sr.RequestError as e:
                print(f"Error with the Speech Recognition service: {e}")
            
            

if __name__ == "__main__":
    print("Welcome to the Voice-to-Text Tool!")
    voice_to_text()
