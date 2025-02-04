def display_welcome_message():
    print("---------------------------")
    print("Disneyland Review Analyzer")
    print("---------------------------")

def show_main_menu():
    print("\nSelect an option:")
    print("[A] View Data")
    print("[B] Visualize Data")
    print("[C] Export Data")
    print("[X] Exit")

def get_user_input():
    return input("Enter your choice: ").strip()
