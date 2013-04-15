rows = []

def main():
    k = 10
    for i in range(0,9):
        rows.append([])
        row = []
        row = raw_input()
        row = row.split()
        for j in range(0,9):    
            rows[i].append(int(row[j]))
        print rows[i]

    print " "           
    while k > 0:    
        k = k - 1
        for i in range(0,9):
            for x in rows[i]:
                if x == 0:
                    create_sets(rows,i,rows[i].index(x))
    #   k = 0
        for i in range(0,9):
        #   print rows[i]
            for x in rows[i]:
                if x==0:

                print " "
                for i in range(0,9):
                        print rows[i]


def create_sets(rows,row_num,col_num):
    col = []
    grid = []
    for i in range(0,8):
        col.append(rows[i][col_num]) 
    if row_num < 2 and col_num < 2:
        for i in range(0,3):
            for j in range(0,3):
                grid.append(rows[i][j]) 

    elif row_num < 2 and col_num < 5:
        for i in range(0,3):
            for j in range(3,6):
                grid.append(rows[i][j]) 

    elif row_num < 5 and col_num < 2:
        for i in range(3,6):
            for j in range(0,3):
                grid.append(rows[i][j])

    elif row_num < 5 and col_num < 5:
        for i in range(3,6):
            for j in range(3,6):
                grid.append(rows[i][j])

    elif row_num < 2 and col_num < 8:
        for i in range(0,3):
            for j in range(6,9):
                grid.append(rows[i][j])


    elif row_num < 8 and col_num < 2:
        for i in range(6,9):
            for j in range(0,3):
                grid.append(rows[i][j])

    elif row_num < 5 and col_num < 8:
        for i in range(3,6):
            for j in range(6,9):
                grid.append(rows[i][j])


    elif row_num < 8 and col_num < 5:
        for i in range(6,9):
            for j in range(3,6):
                grid.append(rows[i][j])


    elif row_num < 8 and col_num < 8:
        for i in range(6,9):
            for j in range(6,9):
                grid.append(rows[i][j])
    full = [1,2,3,4,5,6,7,8,9]
    full = set(full)
    a = set(rows[row_num])
    b = set(col)
    c = set(grid)
    b = b.union(a)
    c = c.union(b)
    full = full.difference(c)
#   print full
    if len(full) == 1: 
        for x in full:
            if x!=0:
                print x,row_num,col_num
                rows[row_num][col_num] = x



if __name__ == "__main__":
    main()

                
