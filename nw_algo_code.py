import numpy as np
input = open("/input/nw_input.fasta", "r")
reads = input.readlines()
seq = [line.strip() for line in reads if not line.startswith(">")]

print("Two input sequences:", *(i for i in seq))
n=len(seq[0])
m=len(seq[1])

nw_matrix= np.zeros((n+1, m+1))
#print(nw_matrix)

mismatch = -1
match = 1
gap = -1

#first row and column of matrix filling with gap penalty
nw_matrix[0,:] = np.arange(0, m+1)*gap
nw_matrix[:,0] = np.arange(0, n+1)*gap
#print(nw_matrix)
print("Dimension of matrix: ",np.ndim(nw_matrix))
print("Shape of matrix: ",np.shape(nw_matrix))

#calculation of NW matrix:
for i in range(1, len(nw_matrix)):
  for j in range(1, len(nw_matrix[0])):
    nw_matrix[i][j]=max(nw_matrix[i-1][j-1]+(match if seq[0][i-1]==seq[1][j-1] else mismatch), nw_matrix[i-1][j]+gap, nw_matrix[i][j-1]+gap)

print("\nNeedleman-Wunsch Algorithem matrix: \n", nw_matrix)

# backtracing :
i, j = len(seq[0]), len(seq[1])
alignment1, alignment2 = "", ""
#print(seq[0][i-1])

# seq[0] : sequence 1 => i
# seq[1] : sequence 2 => j

while i > 0 or j > 0:
  # up check
  if nw_matrix[i][j] == nw_matrix[i-1][j]+gap:
    alignment1 = seq[0][i-1] + alignment1
    alignment2 = "-" + alignment2
    i -=1

  # right check
  elif nw_matrix[i][j] == nw_matrix[i][j-1]+gap:
    alignment1 = "-" + alignment1
    alignment2 = seq[1][j-1] + alignment2
    j -=1

  # diagonal check
  else:
    alignment1 = seq[0][i-1] + alignment1
    alignment2 =  seq[1][j-1] + alignment2
    i -=1
    j -=1

print("\nFinal alignment: \n")

print(alignment1)
print(alignment2)

# ask sir for the how to get mupltiple path
