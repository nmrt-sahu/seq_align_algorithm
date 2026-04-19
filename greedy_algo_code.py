# Read input
#input = open("/content/lab2_input.txt.txt", "r")
#reads = input.readlines()
#reads = [read.strip() for read in reads]

#Printing the reads in the list
#print("Substring of read:", reads)
reads = ['ACG', 'CGA', 'CGC', 'CGT', 'GAC', 'GCG', 'GTA', 'TCG']

print("Substring of read:", reads)

def overlap(a, b):
    for k in range(len(a), 0, -1):
        if a.endswith(b[:k]):        # suffix of a == prefix of b
            return k
    return 0

while len(reads) > 1:
    max_overlap = -1
    best_i, best_j = None, None

    # find best pair
    for i in range(len(reads)):
        for j in range(len(reads)):
            if i != j:
                olap = overlap(reads[i], reads[j])
                if olap > max_overlap:
                    max_overlap = olap
                    best_i, best_j = i, j

    # here merginf the max overlap pair of substring
    if max_overlap > 0:
        merged = reads[best_i] + reads[best_j][max_overlap:]
    else:
        merged = reads[0] + reads[-1]
        best_i, best_j = 0, len(reads) - 1

    # updating list with merged substring and add ramining substring
    new_reads = []
    for k_substring in reads:
        if k_substring != reads[best_i] and k_substring != reads[best_j]:
            new_reads.append(k_substring)
    new_reads.append(merged)

    reads = new_reads
    print("update substring list after each iteration of merging:", reads)

print("\nFinal sequence:", reads[0])
