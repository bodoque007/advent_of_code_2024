def encode_disk_map(disk_map):
    encoded = []
    file_id = 0
    for i, char in enumerate(disk_map):
        count = int(char)
        if i % 2 == 0:
            # Commas are to handle IDs with several digits
            encoded.append((str(file_id) + ',') * count)
            file_id += 1
        else:
            encoded.append(('.' + ',') * count)
    return ''.join(encoded).rstrip(',')


def move_blocks(encoded_map):
    encoded = encoded_map.split(',')
    last_free_index = 0

    for i in range(len(encoded) - 1, -1, -1):
        if encoded[i] != '.':
            while last_free_index < i and encoded[last_free_index] != '.':
                last_free_index += 1
            if last_free_index >= i:
                break
            encoded[last_free_index] = encoded[i]
            encoded[i] = '.'
            last_free_index += 1

    return ','.join(encoded)


def simulate_disk_compaction(disk_map):
    encoded_map = encode_disk_map(disk_map)
    return move_blocks(encoded_map)


def calculate_checksum(compacted_map):
    checksum = 0
    for i, char in enumerate(compacted_map.split(',')):
        if char == '.':
            break
        checksum += int(char) * i
    return checksum


with open("input.txt") as file:
    line = file.read().strip()

compacted = simulate_disk_compaction(line)
suma = calculate_checksum(compacted)

print(suma)
