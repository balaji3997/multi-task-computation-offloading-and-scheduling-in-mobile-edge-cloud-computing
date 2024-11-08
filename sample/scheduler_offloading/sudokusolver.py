def print_grid(arr):
	for i in range(9):
		for j in range(9):
			print(arr[i][j],end=" ")
		print("\n")

def find_empty_location(arr,l):
	res=[]
	for row in range(9):
		for col in range(9):
			if(arr[row][col]==0):
				l[0]=row
				l[1]=col
				res.append(True)
				res.append(l)
				return res
	res.append(False)
	res.append(l)
	return res

def used_in_row(arr,row,num):
	for i in range(9):
		if(arr[row][i]==num):
			return True
	return False

def used_in_col(arr,col,num):
	for i in range(9):
		if(arr[i][col]==num):
			return True
	return False

def used_in_box(arr,row,col,num):
	for i in range(3):
		for j in range(3):
			if(arr[i+row][j+col]==num):
				return True
	return False

def check_location_is_safe(arr,row,col,num):
	return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row-row%3,col-col%3,num)

def solve_sudoku(arr):
	l=[0,0]
	r=[]
	ans=find_empty_location(arr,l)
	if(ans[0]==False):
		r.append(True)
		r.append(arr)
		return r
	l=ans[1].copy()
	row=l[0]
	col=l[1]
	for num in range(1,10):
		if(check_location_is_safe(arr,row,col,num)):
			arr[row][col]=num
			#a=arr.copy()
			res=solve_sudoku(arr)
			arr=res[1].copy()
			if(res[0]==True):
				r.append(True)
				r.append(arr)
				return r
			arr[row][col]=0
	r.append(False)
	r.append(arr)
	return r

if __name__=="__main__":
	grid=[[0 for x in range(9)] for y in range(9)]
	grid=[[3,0,6,5,0,8,4,0,0],
		[5,2,0,0,0,0,0,0,0],
		[0,8,7,0,0,0,0,3,1],
		[0,0,3,0,1,0,0,8,0],
		[9,0,0,8,6,3,0,0,5],
		[0,5,0,0,9,0,6,0,0],
		[1,3,0,0,0,0,2,5,0],
		[0,0,0,0,0,0,0,7,4],
		[0,0,5,2,0,6,3,0,0]]
	res=solve_sudoku(grid)
	if(res[0]==True):
		print_grid(res[1])
	else:
		print("no solution exists")
		print_grid(res[1])

