import random
import time

def roll_dice():
    """Roll a dice with countdown animation"""
    print("\n🎲 Rolling dice...")
    
    # Countdown
    for i in range(3, 0, -1):
        print(f"   {i}...")
        time.sleep(0.8)
    
    # Generate random result
    result = random.randint(1, 6)
    
    # Display result
    print(f"\n🎉 You rolled: {result} 🎉\n")
    return result

def main():
    """Main program"""
    print("🎯 DICE ROLLER SIMULATOR 🎯")
    print("Press Enter to roll, 'quit' to exit\n")
    
    while True:
        user_input = input("Press Enter to roll: ").strip().lower()
        
        if user_input == 'quit':
            print("Thanks for playing! 🎲")
            break
        elif user_input == '':
            roll_dice()
        else:
            print("Just press Enter to roll or 'quit' to exit")

if __name__ == "__main__":
    main()