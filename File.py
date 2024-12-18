import csv
from datetime import datetime

def save_result(result, file_name='history.csv'):
    current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M')
    formatted_result = f"{current_datetime}, Result: {result}"
    
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([formatted_result])
    print(f"Game result '{formatted_result}' has been saved.")

def retrieve_history():
    history = []
    try:
        with open("history.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Check if the row is not empty
                    history.append(", ".join(row))
    except FileNotFoundError:
        print("History file not found. Starting with empty history.")
    return history

def draw_history(screen, history, start_x, start_y, line_spacing, font, color):
    y_position = start_y
    for line in history:
        text = font.render(line, True, color)
        screen.blit(text, (start_x, y_position))
        y_position += line_spacing
