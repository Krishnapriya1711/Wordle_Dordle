import string

with open('words.txt', 'r') as f:
    words = f.readlines()

all_words = set([word.lower().strip() for word in words if len(word.strip()) == 5])

def fil(x):
    for ch in x:
        if ch not in string.ascii_letters:
            return False
    return True

all_words = list(filter(fil, all_words))

possible_answers_1 = list(all_words.copy())
possible_answers_2 = list(all_words.copy())

attempt = 0

print("Dordle Solver - Interactive Mode")
print("=" * 50)
print("Instructions:")
print("  - You're solving TWO Wordle puzzles simultaneously!")
print("  - Enter your 5-letter guess (same guess for both boards)")
print("  - For each letter position on EACH board, enter:")
print("    'green' or 'g' = correct position")
print("    'yellow' or 'y' = wrong position")
print("    'x' or 'gray' = not in word")
print("=" * 50)

board1_solved = False
board2_solved = False

while attempt < 7:  
    print(f"\n{'='*50}")
    print(f"Attempt {attempt + 1}/7")
    print(f"{'='*50}")
    
    if not board1_solved:
        print(f"Board 1 - Possible answers: {len(possible_answers_1)}")
        if len(possible_answers_1) <= 10:
            print(f"  Suggestions: {', '.join(sorted(possible_answers_1))}")
    else:
        print("Board 1 - SOLVED! ✓")
    
    if not board2_solved:
        print(f"Board 2 - Possible answers: {len(possible_answers_2)}")
        if len(possible_answers_2) <= 10:
            print(f"  Suggestions: {', '.join(sorted(possible_answers_2))}")
    else:
        print("Board 2 - SOLVED! ✓")
    
    if board1_solved and board2_solved:
        print("\n🎉 Congratulations! You solved both Dordles!")
        break
    
    word = input(f"\nEnter your 5-letter guess: ").strip().lower()
    
    if len(word) != 5 or not word.isalpha():
        print("Invalid input! Please enter exactly 5 letters.")
        continue
    
    if not board1_solved:
        print("\n--- BOARD 1 FEEDBACK ---")
        feedback_1 = []
        for i, letter in enumerate(word):
            while True:
                status = input(f"  Letter {i+1} ({letter.upper()}): ").strip().lower()
                if status in ['green', 'g']:
                    feedback_1.append('green')
                    break
                elif status in ['yellow', 'y']:
                    feedback_1.append('yellow')
                    break
                elif status in ['x', 'gray']:
                    feedback_1.append('gray')
                    break
                else:
                    print("    Invalid! Enter 'green'/'g', 'yellow'/'y', or 'x'/'gray'")
        
        if all(f == 'green' for f in feedback_1):
            print(f"✓ Board 1 SOLVED: {word.upper()}")
            board1_solved = True
        else:
            filtered_1 = list(possible_answers_1.copy())
            
            for i, (letter, status) in enumerate(zip(word, feedback_1)):
                if status == 'green':
                    filtered_1 = [w for w in filtered_1 if w[i] == letter]
                elif status == 'yellow':
                    filtered_1 = [w for w in filtered_1 if letter in w and w[i] != letter]
                elif status == 'gray':
                    appears_elsewhere = False
                    for j, (l, s) in enumerate(zip(word, feedback_1)):
                        if l == letter and j != i and s in ['green', 'yellow']:
                            appears_elsewhere = True
                            break
                    
                    if appears_elsewhere:
                        filtered_1 = [w for w in filtered_1 if w[i] != letter]
                    else:
                        filtered_1 = [w for w in filtered_1 if letter not in w]
            
            possible_answers_1 = filtered_1
            print(f"Board 1 remaining: {len(possible_answers_1)}")
            if len(possible_answers_1) <= 10:
                print(f"  Suggestions: {', '.join(sorted(possible_answers_1))}")
    
    if not board2_solved:
        print("\n--- BOARD 2 FEEDBACK ---")
        feedback_2 = []
        for i, letter in enumerate(word):
            while True:
                status = input(f"  Letter {i+1} ({letter.upper()}): ").strip().lower()
                if status in ['green', 'g']:
                    feedback_2.append('green')
                    break
                elif status in ['yellow', 'y']:
                    feedback_2.append('yellow')
                    break
                elif status in ['x', 'gray']:
                    feedback_2.append('gray')
                    break
                else:
                    print("    Invalid! Enter 'green'/'g', 'yellow'/'y', or 'x'/'gray'")
        
        if all(f == 'green' for f in feedback_2):
            print(f"✓ Board 2 SOLVED: {word.upper()}")
            board2_solved = True
        else:
            filtered_2 = list(possible_answers_2.copy())
            
            for i, (letter, status) in enumerate(zip(word, feedback_2)):
                if status == 'green':
                    filtered_2 = [w for w in filtered_2 if w[i] == letter]
                elif status == 'yellow':
                    filtered_2 = [w for w in filtered_2 if letter in w and w[i] != letter]
                elif status == 'gray':
                    appears_elsewhere = False
                    for j, (l, s) in enumerate(zip(word, feedback_2)):
                        if l == letter and j != i and s in ['green', 'yellow']:
                            appears_elsewhere = True
                            break
                    
                    if appears_elsewhere:
                        filtered_2 = [w for w in filtered_2 if w[i] != letter]
                    else:
                        filtered_2 = [w for w in filtered_2 if letter not in w]
            
            possible_answers_2 = filtered_2
            print(f"Board 2 remaining: {len(possible_answers_2)}")
            if len(possible_answers_2) <= 10:
                print(f"  Suggestions: {', '.join(sorted(possible_answers_2))}")
    
    if not board1_solved and len(possible_answers_1) == 0:
        print("No possible words for Board 1! Please check your inputs.")
        break
    if not board2_solved and len(possible_answers_2) == 0:
        print("No possible words for Board 2! Please check your inputs.")
        break
    
    attempt += 1

if attempt >= 7:
    print("\n" + "="*50)
    print("Out of attempts!")
    if not board1_solved and len(possible_answers_1) > 0:
        print(f"Board 1 possible answers: {', '.join(sorted(possible_answers_1)[:5])}")
    if not board2_solved and len(possible_answers_2) > 0:
        print(f"Board 2 possible answers: {', '.join(sorted(possible_answers_2)[:5])}")