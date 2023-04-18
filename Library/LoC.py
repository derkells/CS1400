"""
Module Docstring
"""
def main():
    """
    Module Docstring
    """


    alg_dict = {}
    ttl_dict = {}
    woo_dict = {}

    with open("book_data.txt", "r") as file:

        for line in file:

            components = line.strip().split("|")

            code = components[-1]

            line_num = int(components[1])
            text = components[0]

            if code == "ALG":
                alg_dict[line_num] = text
            elif code == "TTL":
                ttl_dict[line_num] = text
            elif code == "WOO":
                woo_dict[line_num] = text

    alg_dict = dict(sorted(alg_dict.items()))
    ttl_dict = dict(sorted(ttl_dict.items()))
    woo_dict = dict(sorted(woo_dict.items()))


# # Initialize variables to hold the longest, shortest, and average line lengths

    alg_longest = ""
    alg_shortest = ""
    alg_total_len = 0
    alg_count = 0

    ttl_longest = ""
    ttl_shortest = ""
    ttl_total_len = 0
    ttl_count = 0

    woo_longest = ""
    woo_shortest = ""
    woo_total_len = 0
    woo_count = 0

    # Loop through each dictionary to find the longest, shortest, and average line lengths
    for line_num, text in alg_dict.items():
        alg_total_len += len(text)
        alg_count += 1
        if not alg_longest or len(text) > len(alg_longest):
            alg_longest = text
        if not alg_shortest or len(text) < len(alg_shortest):
            alg_shortest = text

    for line_num, text in ttl_dict.items():
        ttl_total_len += len(text)
        ttl_count += 1
        if len(text) == len(ttl_longest):
            ttl_longest = text
            ttl_longest_key = line_num
        elif len(text) > (len(ttl_longest)):
            ttl_longest = text
            ttl_longest_key = line_num
        if not ttl_shortest or len(text) < len(ttl_shortest):
            ttl_shortest = text

    for line_num, text in woo_dict.items():
        woo_total_len += len(text)
        woo_count += 1
        if len(text) == len(woo_longest):
            woo_longest = text
            woo_longest_key = line_num
        elif len(text) > (len(woo_longest)):
            woo_longest = text
            woo_longest_key = line_num
        if not woo_shortest or len(text) < len(woo_shortest):
            woo_shortest = text

    # Calgulate the average line length for each dictionary
    alg_avg_len = alg_total_len / alg_count if alg_count > 0 else 0
    ttl_avg_len = ttl_total_len / ttl_count if ttl_count > 0 else 0
    woo_avg_len = woo_total_len / woo_count if woo_count > 0 else 0

    alg_longest_key = 0
    for key, value in alg_dict.items():
        if value == alg_longest:
            alg_longest_key = key

    ttl_longest_key = 0
    for key1, value in ttl_dict.items():
        if value == ttl_longest:
            ttl_longest_key = key1

    woo_longest_key = 0
    for key2, value in woo_dict.items():
        if value == woo_longest:
            woo_longest_key = key2

    alg_shortest_key = 0
    for key3, value in alg_dict.items():
        if value == alg_shortest:
            alg_shortest_key = key3

    ttl_shortest_key = 0
    for key4, value in ttl_dict.items():
        if value == ttl_shortest:
            ttl_shortest_key = key4

    woo_shortest_key = 0
    for key5, value in woo_dict.items():
        if value == woo_shortest:
            woo_shortest_key = key5


    # Write the results to a file
    with open("novel_summary.txt", "w") as file_to_write:
        file_to_write.write("ALG\n")
        file_to_write.write(f"Longest line ({alg_longest_key}): {alg_longest}\n")
        file_to_write.write(f"Shortest line ({alg_shortest_key}): {alg_shortest}\n")
        file_to_write.write(f"Average length: {alg_avg_len:.0f}\n")
        file_to_write.write("\n")

        file_to_write.write("TTL\n")
        file_to_write.write(f"Longest line ({ttl_longest_key}): {ttl_longest}\n")
        file_to_write.write(f"Shortest line ({ttl_shortest_key}): {ttl_shortest}\n")
        file_to_write.write(f"Average length: {ttl_avg_len:.0f}\n")
        file_to_write.write("\n")

        file_to_write.write("WOO\n")
        file_to_write.write(f"Longest line ({woo_longest_key}): {woo_longest}\n")
        file_to_write.write(f"Shortest line ({woo_shortest_key}): {woo_shortest}\n")
        file_to_write.write(f"Average length: {woo_avg_len:.0f}\n")


    with open('novel_text.txt', 'w') as novel_text:
        novel_text.write("ALG\n")
        for value in alg_dict.values():
            novel_text.write(f"{value}\n")

        novel_text.write("-----\n")

        novel_text.write("TTL\n")
        for value in ttl_dict.values():
            novel_text.write(f"{value}\n")

        novel_text.write("-----\n")

        novel_text.write("WOO\n")
        for value in woo_dict.values():
            novel_text.write(f"{value}\n")
