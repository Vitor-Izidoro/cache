import os

CACHE_SIZE = 10
CACHE = {}

def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def display_bible_part(part_number):
    if part_number in CACHE:
        print("Retrieving from cache...")
        print(CACHE[part_number])
    else:
        file_path = f"biblia/{part_number}.txt"
        if os.path.exists(file_path):
            content = load_file(file_path)
            print(content)
            if len(CACHE) >= CACHE_SIZE:
                oldest_part = min(CACHE.keys())
                del CACHE[oldest_part]
            CACHE[part_number] = content
        else:
            print("Part not found on disk.")

def main():
    while True:
        try:
            part_number = int(input("Digite o número da parte da Bíblia que deseja exibir (1-100): "))
            if 1 <= part_number <= 100:
                display_bible_part(part_number)
            else:
                print("Número inválido. Por favor, digite um número entre 1 e 100.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()
