import re

def check_password_strength(password):
    # Initialize criteria flags and score
    score = 0
    feedback = []
    
    # 1. Check Length
    length_criteria = len(password) >= 8
    if length_criteria:
        score += 1
    else:
        feedback.append("• Must be at least 8 characters long.")
        
    # 2. Check Uppercase Letters
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    if uppercase_criteria:
        score += 1
    else:
        feedback.append("• Should contain at least one uppercase letter (A-Z).")
        
    # 3. Check Lowercase Letters
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    if lowercase_criteria:
        score += 1
    else:
        feedback.append("• Should contain at least one lowercase letter (a-z).")
        
    # 4. Check Numbers
    digit_criteria = re.search(r'[0-9]', password) is not None
    if digit_criteria:
        score += 1
    else:
        feedback.append("• Should contain at least one number (0-9).")
        
    # 5. Check Special Characters
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>_+\-=\[\]\\]', password) is not None
    if special_char_criteria:
        score += 1
    else:
        feedback.append("• Should contain at least one special character (e.g., !, @, #, $, %).")

    # Determine strength category based on total score
    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong 👍"
    elif score == 3:
        strength = "Medium 😐"
    elif score == 2:
        strength = "Weak ⚠️"
    else:
        strength = "Very Weak ❌"
        
    return strength, feedback

def main():
    print("--- Password Complexity Checker ---")
    
    while True:
        password = input("\nEnter a password to evaluate (or type 'exit' to quit): ").strip()
        
        if password.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break
            
        if not password:
            print("Password cannot be empty. Please try again.")
            continue
            
        strength, improvements = check_password_strength(password)
        
        print(f"\nPassword Strength: {strength}")
        
        if improvements:
            print("\nSuggestions to improve your password:")
            for suggestion in improvements:
                print(suggestion)
        else:
            print("Excellent! Your password meets all security criteria.")
            
        print("-" * 40)

if __name__ == "__main__":
    main()