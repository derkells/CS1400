import sys

def main():

    alg_dict = {}
    ttl_dict = {}
    woo_dict = {}
    fmp_dict = {}
    pnp_dict = {}
    tsl_dict = {}

    with open('bookData.txt', encoding='utf-8') as file:

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
            elif code == "FMP":
                fmp_dict[line_num] = text
            elif code == "PNP":
                woo_dict[line_num] = text
            elif code == "TSL":
                woo_dict[line_num] = text

    alg_dict = dict(sorted(alg_dict.items()))
    ttl_dict = dict(sorted(ttl_dict.items()))
    woo_dict = dict(sorted(woo_dict.items()))
    fmp_dict = dict(sorted(woo_dict.items()))
    pnp_dict = dict(sorted(woo_dict.items()))
    tsl_dict = dict(sorted(woo_dict.items()))

    #
    # # # Initialize variables to hold the longest, shortest, and average line lengths
    #
    fmp_longest = ""
    fmp_shortest = ""
    fmp_total_length = 0
    fmp_count = 0
    fmp_longest_key = 0

    pnp_longest = ""
    pnp_shortest = ""
    pnp_total_length = 0
    pnp_count = 0
    pnp_longest_key = 0

    tsl_longest = ""
    tsl_shortest = ""
    tsl_total_length = 0
    tsl_count = 0
    tsl_longest_key = 0

    alg_longest = ""
    alg_shortest = ""
    alg_total_len = 0
    alg_count = 0
    alg_longest_key = 0

    ttl_longest = ""
    ttl_shortest = ""
    ttl_total_len = 0
    ttl_count = 0
    ttl_longest_key = 0
    #
    woo_longest = ""
    woo_shortest = ""
    woo_total_len = 0
    woo_count = 0
    woo_longest_key = 0

    if fmp_dict:
        for line_num, text in fmp_dict.items():
            fmp_total_length += len(text)
            fmp_count += 1
            if len(text) == len(fmp_longest):
                fmp_longest = text
                fmp_longest_key = line_num
            elif len(text) > (len(fmp_longest)):
                fmp_longest = text
                fmp_longest_key = line_num
            if not fmp_shortest or len(text) < len(fmp_shortest):
                fmp_shortest = text

    if pnp_dict:
        for line_num, text in pnp_dict.items():
            pnp_total_length += len(text)
            pnp_count += 1
            if len(text) == len(pnp_longest):
                pnp_longest = text
                pnp_longest_key = line_num
            elif len(text) > (len(pnp_longest)):
                pnp_longest = text
                pnp_longest_key = line_num
            if not pnp_shortest or len(text) < len(pnp_shortest):
                pnp_shortest = text

    if tsl_dict:
        for line_num, text in tsl_dict.items():
            tsl_total_length += len(text)
            tsl_count += 1
            if len(text) == len(tsl_longest):
                tsl_longest = text
                tsl_longest_key = line_num
            elif len(text) > (len(tsl_longest)):
                tsl_longest = text
                tsl_longest_key = line_num
            if not tsl_shortest or len(text) < len(tsl_shortest):
                tsl_shortest = text
    if alg_dict:
        for line_num, text in alg_dict.items():
            alg_total_len += len(text)
            alg_count += 1
            if len(text) == len(alg_longest):
                alg_longest = text
                alg_longest_key = line_num
            elif len(text) > (len(alg_longest)):
                alg_longest = text
                alg_longest_key = line_num

    if ttl_dict:
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

    if woo_dict:
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

    # Calculate the average line length for each dictionary
    alg_avg_len = alg_total_len / alg_count if alg_count > 0 else 0
    ttl_avg_len = ttl_total_len / ttl_count if ttl_count > 0 else 0
    woo_avg_len = woo_total_len / woo_count if woo_count > 0 else 0

    fmp_avg_len = fmp_total_length / fmp_count if fmp_count > 0 else 0
    pnp_avg_len = pnp_total_length / pnp_count if pnp_count > 0 else 0
    tsl_avg_len = tsl_total_length / tsl_count if tsl_count > 0 else 0


    fmp_longest_key = 0
    for key, value in fmp_dict.items():
        if value == fmp_longest:
            fmp_longest_key = key
    pnp_longest_key = 0
    for key, value in pnp_dict.items():
        if value == pnp_longest:
            pnp_longest_key = key
    tsl_longest_key = 0
    for key, value in tsl_dict.items():
        if value == tsl_longest:
            tsl_longest_key = key



    fmp_shortest_key = 0
    for key3, value in fmp_dict.items():
        if value == fmp_shortest:
            fmp_shortest_key = key3
    pnp_shortest_key = 0
    for key3, value in pnp_dict.items():
        if value == pnp_shortest:
            pnp_shortest_key = key3
    tsl_shortest_key = 0
    for key3, value in tsl_dict.items():
        if value == tsl_shortest:
            tsl_shortest_key = key3


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

    #Summary of stats Results
    with open("novel_summary.txt", "w") as f:
        if alg_dict:
            f.write("ALG\n")
            f.write("Longest line ({}): {}\n".format(alg_longest_key, alg_longest))
            f.write("Shortest line ({}): {}\n".format(alg_shortest_key, alg_shortest))
            f.write("Average length: {:.0f}\n".format(alg_avg_len))
            f.write("\n")

            f.write("TTL\n")
            f.write("Longest line ({}): {}\n".format(ttl_longest_key, ttl_longest))
            f.write("Shortest line ({}): {}\n".format(ttl_shortest_key, ttl_shortest))
            f.write("Average length: {:.0f}\n".format(ttl_avg_len))
            f.write("\n")

            f.write("WOO\n")
            f.write("Longest line ({}): {}\n".format(woo_longest_key, woo_longest))
            f.write("Shortest line ({}): {}\n".format(woo_shortest_key, woo_shortest))
            f.write("Average length: {:.0f}\n".format(woo_avg_len))

        if pnp_dict:
            f.write("FMP\n")
            f.write("Longest line ({}): {}\n".format(fmp_longest_key, fmp_longest))
            f.write("Shortest line ({}): {}\n".format(fmp_shortest_key, fmp_shortest))
            f.write("Average length: {:.0f}\n".format(fmp_avg_len))
            f.write("\n")

            f.write("PNP\n")
            f.write("Longest line ({}): {}\n".format(pnp_longest_key, pnp_longest))
            f.write("Shortest line ({}): {}\n".format(pnp_shortest_key, pnp_shortest))
            f.write("Average length: {:.0f}\n".format(pnp_avg_len))
            f.write("\n")

            f.write("TSL\n")
            f.write("Longest line ({}): {}\n".format(tsl_longest_key, tsl_longest))
            f.write("Shortest line ({}): {}\n".format(tsl_shortest_key, tsl_shortest))
            f.write("Average length: {:.0f}\n".format(tsl_avg_len))


    #Book Data Text
    with open('novel_text.txt', 'w') as novel_text:
        if alg_dict:
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

        if pnp_dict:
            novel_text.write("FMP\n")
            for value in fmp_dict.values():
                novel_text.write(f"{value}\n")

            novel_text.write("-----\n")

            novel_text.write("PNP\n")
            for value in pnp_dict.values():
                novel_text.write(f"{value}\n")

            novel_text.write("-----\n")

            novel_text.write("TSL\n")
            for value in tsl_dict.values():
                novel_text.write(f"{value}\n")
