def globe_bot():
    print("--- Welcome to GlobeBot! ---")
    print("Let's play a guessing game about countries.")
    print("-------------------------------------------")

    # Step 1: Hot or Cold?
    print("\nQuestion 1: Do you prefer Hot or Cold climates?")
    climate = input("Type 'hot' or 'cold': ").strip().lower()

    if climate == "hot":
        # Step 2 (Hot branch): Spicy food or Rainforests?
        print("\nQuestion 2: What interests you more?")
        print("1. Spicy food and temples")
        print("2. Rainforests and carnival")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            print("\n> GlobeBot says: You are thinking of India! 🇮🇳")
        elif choice == "2":
            print("\n> GlobeBot says: You are thinking of Brazil! 🇧🇷")
        else:
            print("\nInvalid choice. GlobeBot lost track of your clues!")

    elif climate == "cold":
        # Step 2 (Cold branch): Volcanoes or Maple syrup?
        print("\nQuestion 2: What interests you more?")
        print("1. Volcanoes and northern lights")
        print("2. Maple syrup and ice hockey")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            print("\n> GlobeBot says: You are thinking of Iceland! 🇮🇸")
        elif choice == "2":
            print("\n> GlobeBot says: You are thinking of Canada! 🇨🇦")
        else:
            print("\nInvalid choice. GlobeBot lost track of your clues!")
            
    else:
        print("\nInvalid input. Please restart and type either 'hot' or 'cold'.")

    # Goodbye Intent
    print("\n-------------------------------------------")
    print("GlobeBot: Bye, see you, adios...")

# Run the chatbot
if __name__ == "__main__":
    globe_bot()