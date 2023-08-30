import time

def speed_typing_test(text):
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")
    
    print("\n" + "-" * 40 + "\n")
    print(text + "\n")
    print("-" * 40 + "\n")
    
    start_time = time.time()
    user_input = input("Start typing here: ")
    end_time = time.time()
    
    time_taken = end_time - start_time
    words = text.split()
    typed_words = user_input.split()
    
    correct_words = 0
    for expected, typed in zip(words, typed_words):
        if expected == typed:
            correct_words += 1
    
    accuracy = (correct_words / len(words)) * 100
    words_per_minute = (len(typed_words) / time_taken) * 60
    
    print("\nTime taken: {:.2f} seconds".format(time_taken))
    print("Accuracy: {:.2f}%".format(accuracy))
    print("Words per minute: {:.2f} wpm".format(words_per_minute))

if __name__ == "__main__":
    test_text = "The quick brown fox jumps over the lazy dog."
    speed_typing_test(test_text)

