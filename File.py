import csv
from datetime import datetime

def save_result(result, file_name='history.csv'):
    current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M')
    formatted_result = f"{current_datetime}, Result: {result}"
    
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([formatted_result])
    print(f"Game result '{formatted_result}' has been saved.")

def retrieve_history(file_name='history.csv'):
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            print("\nGame History:")
            for row in reader:
                print(row[0])  
    except FileNotFoundError:
        print(f"\nThe file '{file_name}' does not exist yet.")
