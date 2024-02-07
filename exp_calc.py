import msvcrt

# Define the cost table
cost_table = {
    6: (25, 10),
    11: (30, 15),
    16: (40, 20),
    21: (50, 30),
    26: (70, 40),
    31: (90, 60),
    36: (120, 80),
    41: (150, 110),
    46: (190, 140),
    51: (230, 180),
    56: (280, 220),
    61: (330, 270),
    66: (390, 320),
    71: (450, 380),
    # Default value for advancements beyond 70
    float('inf'): (520, 440)
}

def calculate_total_experience(advancement_type, current_advancements, desired_advancements):
    total_experience = 0
    for i in range(current_advancements + 1, current_advancements + desired_advancements + 1):
        for threshold, (char_exp, skill_exp) in cost_table.items():
            if i <= threshold:
                if advancement_type == 'c':
                    total_experience += char_exp
                elif advancement_type == 'u':
                    total_experience += skill_exp
                break
    return total_experience

def main():

    while True:
        current_advancements = int(input("Wprowadź liczbę już posiadanych rozwinięć: "))
        advancement_type = input("Wprowadź 'u' dla umiejętności i 'c' dla cechy: ").lower()
        desired_advancements = int(input(f"Podaj o ile chcesz rozwinąć {advancement_type}: "))

        total_experience_needed = calculate_total_experience(advancement_type, current_advancements, desired_advancements)

        print("Całkowite potrzebne doświadczenie:", total_experience_needed, '\n', '============================', '\n')

        print("Naciśnij q by zakończyć program.")
        # Sprawdź, czy został wciśnięty klawisz 'q'
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'q' or key == b'Q':
                print("Do widzenia!")
                break
            

if __name__ == "__main__":
    main()
