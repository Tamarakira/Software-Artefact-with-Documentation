import interface
import data_processor as dp
import visualizer as vz
from export_manager import ExportHandler

def main():
    interface.display_welcome_message()
    data = dp.load_dataset('data/theme_park_reviews.csv')
    print(f"Dataset loaded with {len(data)} reviews.")

    while True:
        interface.show_main_menu()
        user_choice = interface.get_user_input().upper()

        if user_choice == 'A':
            handle_data_viewing(data)
        elif user_choice == 'B':
            handle_visualization(data)
        elif user_choice == 'C':
            exporter = ExportHandler(data)
            handle_data_export(exporter)
        elif user_choice == 'X':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
