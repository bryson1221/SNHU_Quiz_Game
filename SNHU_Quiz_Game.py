import time

def play_game():
    score = 0

    questions = [
        {
            "question": "What city is SNHU located?",
            "answer": "Manchester"
        },
        {
            "question": "What year was SNHU founded?",
            "answer": "1932"
        },
        {
            "question": "What is the full name of the SNHU mascot?",
            "answer": "Petey Penmen"
        },
        {
            "question": "Is SNHU a dry campus?",
            "answer": "yes"
        },
        {
            "question": "Is SNHU a Yellow Ribbon school?",
            "answer": "yes"
        }
    ]

    print("Welcome to my SNHU Game!")

    while True:
        playing = input("Do you want to play? (yes/no) ")

        if playing != "yes":
            print("Thanks for playing! Goodbye.")
            break

        print("Okay! Let's play ")

        for question in questions:
            print(question["question"])
            start_time = time.time()
            answer = input("Your answer: ")
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Time taken: ", elapsed_time)
            if answer.lower() == question["answer"].lower():
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")

        print("Your final score is: ", score)
        play_again = input("Do you want to play again? (yes/no) ")
        if play_again.lower() != "yes":
            break

play_game()


