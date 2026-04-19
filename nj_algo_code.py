import numpy as np
dist_matrix = np.array([
    [0, 10, 12, 9, 19],
    [10, 0, 6, 5, 13],
    [12, 6, 0, 7, 9],
    [9, 5, 7, 0, 14],
    [19, 13, 9, 14, 0]
])

labels = ['A', 'B', 'C', 'D', 'E']

print ("original Distance matrix: ", dist_matrix)
print("original Labels of nodes: ", labels)


# function for : merge the nodes and create new matrix
def merge_node(i,j,labels,dist_matrix):
  #new distance calculaiton
  new_dist= []
  for k in range(len(labels)):
    if k != i and k != j:
      d = (dist_matrix[i][k] + dist_matrix[j][k] - dist_matrix[i][j]) / 2
      new_dist.append(d)

  #print( "Distnaces of merge node from other nodes: ", new_dist)

  # label removal of merged nodes , and append merged node
  new_node = labels[i] + labels[j]
  new_labels = labels.copy()
  new_labels.append(new_node)
  new_labels.remove(labels[i])
  new_labels.remove(labels[j])
  print("New  node label: ", new_labels)     # Labbel append with merge node


  # Step 3: delete rows & columns
  D_new = np.delete(dist_matrix, [i, j], axis=0)
  D_new = np.delete(D_new, [i, j], axis=1)

  # Step 4: add new column
  new_col = np.array(new_dist).reshape(-1, 1)  # convert into column vector
  D_new = np.hstack((D_new, new_col))

    # Step 5: add new row
  new_row = np.append(new_dist, 0)
  D_new = np.vstack((D_new, new_row))
  print("New Distance matrix: ", D_new)
  return new_labels, D_new


step = 1

while len(labels) > 2:
  L = len(dist_matrix) # Length of matrix
  print("\nOriginal Distance matrix: ", dist_matrix)
  print("Length of matrix: ", L)

  # sum of d calculaiton
  r = np.sum(dist_matrix, axis=1) # sum of row
  r_dict = dict(zip(labels, r))
  print("r (sum of row) for all nodes/row: ",r_dict)
  D_matrix = np.zeros((L, L))
  for i in range(L):
    for j in range(L):
      if i != j:
        D_matrix[i,j] = (L-2)*dist_matrix[i,j] - r[i] - r[j]
  print("D_Matrix :", D_matrix)
  #print(np.min(D_matrix))

  D = D_matrix.copy()
  np.fill_diagonal(D, np.inf) # filled diagonal with inf
  #print(D)
  min_val = np.min(D)
  print("Minimum value in D matrix:", min_val)
  i, j = np.unravel_index(np.argmin(D), D.shape)
  #print(i,j)
  print("Node that need to be merge: ",labels[i], labels[j])

  #calling merge fucntiona new distance matrix calculaiton
  labels, dist_matrix = merge_node(i,j,labels,dist_matrix)
  step += 1

# Final step
print("\n--- Final Step ---")
