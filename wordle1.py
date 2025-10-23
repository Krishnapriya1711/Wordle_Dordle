import string
with open('words.txt', 'r') as f:
    words = f.readlines()
possible_answers = set([word.lower().strip() for word in words if len(word.strip()) == 5])

def fil(x):
    for ch in x:
        if ch not in string.ascii_letters:
            return False
    return True
possible_answers = list(filter(fil, possible_answers))

attempt = 0

print("Wordle Solver - Interactive Mode")
print("=" * 50)
print("Instructions:")
print("  - Enter your 5-letter guess")
print("  - For each letter position, enter:")
print("    'green' or 'g' = correct position")
print("    'yellow' or 'y' = wrong position")
print("    'x' or 'gray' = not in word")
print("=" * 50)

while attempt < 6:
    print(f"\nAttempt {attempt + 1}/6")
    print(f"Possible answers remaining: {len(possible_answers)}")
    
    word = input(f"Enter your 5-letter guess: ").strip().lower()
    
    if len(word) != 5 or not word.isalpha():
        print("Invalid input! Please enter exactly 5 letters.")
        continue
   
    feedback = []
    print("\nEnter feedback for each letter:")
    for i, letter in enumerate(word):
        while True:
            status = input(f"  Letter {i+1} ({letter.upper()}): ").strip().lower()
            if status in ['green', 'g']:
                feedback.append('green')
                break
            elif status in ['yellow', 'y']:
                feedback.append('yellow')
                break
            elif status in ['x', 'gray']:
                feedback.append('gray')
                break
            else:
                print("    Invalid! Enter 'green'/'g', 'yellow'/'y', or 'x'/'gray'")
    
    if all(f == 'green' for f in feedback):
        print(f"\nCongratulations! The word is: {word.upper()}")
        break
    
    filtered = list(possible_answers.copy())
    
    for i, (letter, status) in enumerate(zip(word, feedback)):
        if status == 'green':
            
            filtered = [w for w in filtered if w[i] == letter]
        
        elif status == 'yellow':
            
            filtered = [w for w in filtered if letter in w and w[i] != letter]
        
        elif status == 'gray':
            appears_elsewhere = False
            for j, (l, s) in enumerate(zip(word, feedback)):
                if l == letter and j != i and s in ['green', 'yellow']:
                    appears_elsewhere = True
                    break
            
            if appears_elsewhere:
                filtered = [w for w in filtered if w[i] != letter]
            else:
                filtered = [w for w in filtered if letter not in w]
    
    possible_answers = filtered
    

    print(f"\nRemaining possibilities: {len(possible_answers)}")
    if len(possible_answers) == 0:
        print("No possible words found! Please check your inputs.")
        break
    elif len(possible_answers) <= 20:
        print("Possible words:", ', '.join(sorted(possible_answers)))
    else:
        print("Top 20 suggestions:", ', '.join(sorted(possible_answers)[:20]))
    
    attempt += 1

if attempt >= 6 and len(possible_answers) > 0:
    print("\nOut of attempts!")
    print(f"Possible answer(s): {', '.join(sorted(possible_answers)[:10])}")