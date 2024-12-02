import random
import time

def digit_span_task(levels=3):
    """
    Simulate a digit span task where the user recalls a sequence of numbers.
    Levels represent the difficulty of the task (e.g., how many digits).
    """
    print("Starting Digit Span Task...")

    # List to store participant's results
    results = []

    for level in range(1, levels + 1):
        # Generate a random sequence of numbers (level defines the length of the sequence)
        sequence = [random.randint(0, 9) for _ in range(level)]
        
        print(f"Level {level}: Memorize this sequence:")
        print(" ".join(map(str, sequence)))
        time.sleep(3)  # Give the participant 3 seconds to memorize the numbers

        # Clear the screen (for simplicity, print a message instead)
        print("\n" * 50)
        
        # Ask for the sequence recall
        recall = input(f"Recall the sequence of {level} digits (separated by spaces): ").split()
        
        # Check if recall matches the sequence
        if recall == [str(num) for num in sequence]:
            print("Correct!\n")
            results.append(True)
        else:
            print(f"Incorrect! The correct sequence was: {' '.join(map(str, sequence))}\n")
            results.append(False)
    
    # Summarize the result
    score = results.count(True)
    print(f"Your score: {score} out of {levels}")
    return score

def problem_solving_task():
    """
    Simulate a simple math problem-solving task.
    """
    print("Starting Problem-Solving Task...")

    # List to store participant's results
    results = []

    problems = [
        ("5 + 3", 8),
        ("12 - 7", 5),
        ("6 * 4", 24),
        ("18 / 3", 6),
    ]
    
    for problem, correct_answer in problems:
        print(f"Problem: {problem}")
        answer = int(input("Your answer: "))
        
        if answer == correct_answer:
            print("Correct!\n")
            results.append(True)
        else:
            print(f"Incorrect! The correct answer was: {correct_answer}\n")
            results.append(False)
    
    # Summarize the result
    score = results.count(True)
    print(f"Your score: {score} out of {len(problems)}")
    return score

def cognitive_test():
    print("Welcome to the Cognitive Development Test\n")
    
    # Step 1: Working Memory Test
    print("Step 1: Working Memory Test")
    memory_score = digit_span_task()
    
    # Step 2: Problem Solving Test
    print("\nStep 2: Problem Solving Test")
    problem_solving_score = problem_solving_task()
    
    # Summarize results
    print("\nTest Summary:")
    print(f"Working Memory Score: {memory_score} out of 3")
    print(f"Problem Solving Score: {problem_solving_score} out of 4")

    # You can analyze the relationship between memory_score and problem_solving_score here.
    if memory_score > 1:
        print("You seem to have a good working memory, which might help in problem-solving!")
    else:
        print("You may benefit from working on improving your memory to enhance problem-solving skills.")

if __name__ == "__main__":
    cognitive_test()
