def calculate_sum(number1, number2):
    return number1 + number2

def display_result(result):
    print(f"Hasil penjumlahan: {result}")

def main():
    first_number = 10
    second_number = 5

    result = calculate_sum(first_number, second_number)
    display_result(result)

if __name__ == "__main__":
    main()