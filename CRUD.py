def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines

def add_line(lines):
    last_line = lines[-1]
    last_number = int(last_line.split(',')[0])
    new_number = str(last_number + 1)
    
    name = input("Enter name: ")
    name = name.capitalize()
    phone = input("Enter phone number: ")
    phone = "'" + phone

    new_line = f"{new_number},{name},{phone}\n"
    lines.append(new_line)
    print("Line added successfully.")

def update_line(lines):
    line_number = int(input("Enter the line number to update: "))
    if line_number < 1 or line_number > len(lines):
        print("Invalid line number.")
        return

    name = input("Enter the updated name: ")
    name = name.capitalize()
    phone = input("Enter the updated phone number: ")
    phone = "'" + phone

    line_parts = lines[line_number - 1].split(',')
    line_parts[1] = name
    line_parts[2] = phone
    updated_line = ','.join(line_parts)
    lines[line_number - 1] = updated_line

    print("Line updated successfully.")

def delete_line(lines):
    line_number = int(input("Enter the line number to delete: "))
    if line_number < 1 or line_number > len(lines):
        print("Invalid line number.")
        return
    del lines[line_number - 1]
    print("Line deleted successfully.")

def display_menu():
    print("1. Add a new line")
    print("2. Read all lines")
    print("3. Update a specific line")
    print("4. Delete a specific line")
    print("5. Exit")

def main():
    filename = "dummy.txt"  # Replace with the actual file name/path
    lines = read_file(filename)
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_line(lines)
        elif choice == "2":
            print("Number | Name | Phone Number")
            for line in lines:
                line_parts = line.split(',')
                line_parts[0] = line_parts[0].strip()
                line_parts[1] = line_parts[1].strip()
                line_parts[2] = line_parts[2].strip().replace("'", "")
                print(" | ".join(line_parts))
        elif choice == "3":
            update_line(lines)
        elif choice == "4":
            delete_line(lines)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

    with open(filename, "w") as file:
        file.writelines(lines)

if __name__ == "__main__":
    main()
