def count_words(text):
    """
    This function takes a string and returns the number of words in it.
    Words are separated by spaces.
    """
    words = text.split()  # Split the text into a list of words based on spaces
    return len(words)

def main():
    """
    Main function to handle user input and display the word count.
    """
    print("Welcome to the Word Counter Program!")  # User-friendly greeting
    
    # Prompt the user for input
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: Input cannot be empty. Please try again.")
        return  # Exit the function if input is invalid

    # Count the words using the function
    word_count = count_words(user_input)
    
    # Display the result
    print(f"The number of words in the entered text is: {word_count}")

# Run the program
if __name__ == "__main__":
    main()
