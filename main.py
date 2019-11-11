str_one = "EXPONENTIAL"
str_two = "POLYNOMIAL"

X = "CATAAGCTTCTGACTCTTACCTCCCTCTCTCCTACTCCTGCTCGCATCTGCTATAGTGGAGGCCGGAGCAGGAACAGGTTGAACAG"
Y = "CGTAGCTTTTTGGTTAATTCCTCCTTCAGGTTTGATGTTGGTAGCAAGCTATTTTGTTGAGGGTGCTGCTCAGGCTGGATGGA"

def edit_distance_table(s, t):
    m = len(s)
    n = len(t)

    # Instantiate the array
    edit_array = [[0 for i in range(n)] for j in range(m)]

    for i in range(1, m):
        edit_array[i][0] = i

    for j in range(1, n):
        edit_array[0][j] = j

    for i in range(1, n):
        for j in range(1, m):
            if s[j] == t[i]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            edit_array[i][j] = min(edit_array[i - 1][j] + 1,                        # Delete
                                   edit_array[i][j - 1] + 1,                        # Insert
                                   edit_array[i - 1][j - 1] + substitution_cost     # Substitute
                                   )

    return edit_array[m][n]


print('Edit Distance: ' + str(edit_distance_table(str_one, str_two)))
