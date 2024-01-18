from langdetect import detect


def detect_language(text):
    try:
        language = detect(text)
        return language
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    print("Language Detection Program")
    print("Enter a text to detect its language. Type 'exit' to end.")

    while True:
        user_input = input("Enter text: ")

        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        if not user_input:
            print("Please enter a valid text.")
            continue

        language_detected = detect_language(user_input)

        if language_detected:
            print(f"The detected language is: {language_detected}\n")
        else:
            print("Language detection failed. Please try again.\n")


if __name__ == "__main__":
    main()
