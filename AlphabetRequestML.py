import collections


def calculate_frequency(file_path):
    with open(file_path, 'r') as file:
        content = file.read().lower()
        alphabet_count = collections.Counter(c for c in content if c.isalpha())
    return alphabet_count


def sort_frequency(alphabet_count):
    sorted_alphabet_count = sorted(alphabet_count.items(), key=lambda x: x[1])
    return [item[0] for item in sorted_alphabet_count]


def encrypt_file(input_file, output_file, mapping):
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        content = in_file.read().lower()
        encrypted_content = ''.join(mapping[c] if c.isalpha() else c for c in content)
        out_file.write(encrypted_content)


def decrypt_file(input_file, output_file, mapping):
    reverse_mapping = {v: k for k, v in mapping.items()}
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        content = in_file.read().lower()
        decrypted_content = ''.join(reverse_mapping[c] if c.isalpha() else c for c in content)
        out_file.write(decrypted_content)


input_file =  "C:/Users/USER/Desktop/alphabet.txt"  
encrypted_file = 'C:/Users/USER/Desktop/암호화.txt'
decrypted_file = 'C:/Users/USER/Desktop/복호화.txt'


frequency = calculate_frequency(input_file)# 빈도 수 계산


sorted_alphabet = sort_frequency(frequency)


mapping = {chr(97+i): sorted_alphabet[i] for i in range(26)}


encrypt_file(input_file, encrypted_file, mapping)


decrypt_file(encrypted_file, decrypted_file, mapping)

def count(sorted_alphabet, frequency, output_file):
    with open(output_file, 'w') as out_file:
        for char in sorted_alphabet:
            out_file.write(f'{char}: {frequency[char]}\n')




sorted_alphabet = sort_frequency(frequency)


sorted_frequency_file = 'C:/Users/USER/Desktop/키값.txt'
count(sorted_alphabet, frequency, sorted_frequency_file)







