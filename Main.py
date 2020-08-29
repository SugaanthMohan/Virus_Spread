# INITIAL DETAILS RETREIVE
# IMPORT STATEMENTS HERE
import datetime
import re
import numpy as np

"""
SAMPLE INPUT FORMAT
3
6 5
(2,2)
100 50
(39,5)
44 130
(1,1)
"""

# <<<<<<<<<<< INPUT RETRIEVING >>>>>>>>>>>>>>
# GET THE TOTAL NUMBER OF TEST CASES
print("ENTER TOTAL NUMBER OF TEST CASES HERE:")
t = str(input()).strip()

# VALIDATE IF THE GIVEN INPUT IS A NUMBER
assert t.isdigit(), "NOT A VALID NUMBER"

t = int(t)

# ITERATE THROUGHT THE TOTAL NUMBER OF TEST CASES T TIMES 
for x in range(t):


	# GET THE SIZE OF THE MATRIX
	# VALIDATE IF THE NUMBER IS VALID
	print("ENTER TOTAL SIZE OF THE MATRIX HERE")
	nXm = str(input()).strip()
	nXm_coord = re.findall(r'\d+', nXm)
	for value in nXm_coord:
		assert value.isdigit(), "NOT A VALID NUMBER"

	assert len(nXm_coord) == 2, "NOT VALID INPUT"

	n,m = map(int, nXm_coord)

	my_matrix = np.ones((n,m))

	# GET THE VIRUS COORDINATES 
	# VALIDATE IF THE NUMBER IS VALID
	print("ENTER VIRUS COORDINATES HERE")
	virus_string = str(input()).strip()
	virus_coord = re.findall(r'\d+', virus_string)
	for value in virus_coord:
		assert value.isdigit(), "NOT A VALID NUMBER"

	assert len(virus_coord) == 2, "NOT VALID INPUT"

	r,c = map(int, virus_coord)

	my_matrix[r][c] = 0

	print(my_matrix)
	exit()

	# OUTPUT VALUES HERE 
	max_time = max([row_spread_total_time, column_spread_total_time])

	# <<<<<<<<<<< OUTPUT PRINTING >>>>>>>>>>>>>>>>>  
	hours,mins,secs = map(int,str(datetime.timedelta(seconds=max_time)).split(':'))

	output_string = ""
	if hours == 1:
		output_string += str(hours) + " hour "
	elif hours > 1:
		output_string += str(hours) + " hours "

	if mins == 1:
		output_string += str(mins) + " minute "
	elif mins > 1:
		output_string += str(mins) + " minutes "

	if secs == 1:
		output_string += str(secs) + " second "
	elif secs > 1:
		output_string += str(secs) + " seconds "

	print(output_string)

