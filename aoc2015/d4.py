from hashlib import md5

input_val = 'yzbqklnj'

number = 0

five = False
six = False
while True:
    hash = md5(bytes(f"{input_val}{number}".encode('utf-8'))).hexdigest()
    if hash.startswith('00000') and not five:
        print(f'The hash {hash} with 5 zeros has been found with number {number}')
        five = True
    if hash.startswith('000000') and not six:
        print(f'The hash {hash} with 6 zeros has been found with number {number}')
        six = True
    if five and six:
        break
    number += 1