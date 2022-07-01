
def bangdiem_trungbinh(file):
	"""Read file and return a dictionary of course's score of each student: {id1: {course: average_score}, id2: {course: average_score}}"""

	f = open(file, "r")
	try:
		data = f.readlines()

		# List of course's names
		monhoc = data[0].split(",")
		monhoc.pop(0)
		for x in range(len(monhoc)):
			monhoc[x] = monhoc[x].strip()

		hs_diemtb = {}
		# Get student's ids and scores	
		for line in data[1:]:
			# Student's id
			ma_hocsinh = line.split(";")[0]

			# Scores as string
			dtb = line.split()[1]
			hs_bangdiem = dtb.split(";")

			# Convert scores for floating number
			for x in range(len(hs_bangdiem)):
				hs_bangdiem[x] = float(hs_bangdiem[x])

			# Create dictionary: {course: average_score}
			diemtb = {k:v for (k, v) in zip(monhoc, hs_bangdiem)}
			hs_diemtb[ma_hocsinh] = diemtb

		# Return a dictionary of each course's score of each student's id: {id1: {course: average_score}, id2: {course: average_score}}
		return hs_diemtb
	finally:
		f.close()


#=============================2.a Ham xeploai_hocsinh======================================
def xeploai_hocsinh(bang_diem_tb):
	"""Take in dictionary of average score for each course of each student, calculate his/her finally score and return his/her Academic Rank"""
	xeploai = {}
	for hs, diemtb in bang_diem_tb.items():
		# List of average scores of each student
		hs_diem = [v for x, v in diemtb.items()]

		# Calculate final average score of student
		dtb_chuan = ((diemtb["Toan"] + diemtb["Van"] + diemtb["Anh"]) * 2.0 + (diemtb["Ly"] + diemtb["Hoa"] + diemtb["Sinh"] + diemtb["Su"] + diemtb["Dia"]) * 1.0) / 11.0

		# Check conditions for to define Academic Rank
		if dtb_chuan > 9.0 and all(x >= 8.0 for x in hs_diem):
			xeploai[hs] = "Xuat sac"
		elif dtb_chuan > 8.0 and all(x >= 6.5 for x in hs_diem):
			xeploai[hs] = 'Gioi'
		elif dtb_chuan > 6.5 and all(x >= 5.0 for x in hs_diem):
			xeploai[hs] = "Kha"
		elif dtb_chuan > 6.0 and all(x >= 4.5 for x in hs_diem):
			xeploai[hs] = "TB kha"
		else:
			xeploai[hs] = "TB"
	return xeploai


#=============================2.b Ham xeploai_thidaihoc_hocsinh======================================
def xeploai_thidaihoc_hocsinh(bang_diem_tb):
	"""Input student's average scores, calculate his/her total average scores of each Focus Group of Courses (FGC) to define his/her Rank in that FGC"""

	xeploai_khoi = {}

	# Loop through each student and calculate his/her total average scores for each FGC
	for hs, diemtb in bang_diem_tb.items():
		A = diemtb["Toan"] + diemtb["Ly"] + diemtb["Hoa"]
		A1 = diemtb["Toan"] + diemtb["Ly"] + diemtb["Anh"]
		B = diemtb["Toan"] + diemtb["Hoa"] + diemtb["Sinh"]
		C = diemtb["Van"] + diemtb["Su"] + diemtb["Dia"]
		D = diemtb["Toan"] + diemtb["Van"] + diemtb["Anh"] * 2

		tongdiem_khoi = [A, A1, B, C, D]

		# Check the total scores and rank first 3 FGC (A, A1, B)
		for x in range(3):
			if tongdiem_khoi[x] >= 24:
				tongdiem_khoi[x] = 1
			elif 18 <= tongdiem_khoi[x] < 24:
				tongdiem_khoi[x] = 2
			elif 12 <= tongdiem_khoi[x] < 18:
				tongdiem_khoi[x] = 3
			elif tongdiem_khoi[x] < 12:
				tongdiem_khoi[x] = 4

		# Check total score and rank C group
		khoiC = tongdiem_khoi[3]
		if khoiC >= 21:
			tongdiem_khoi[3] = 1
		elif 15 <= khoiC < 21:
			tongdiem_khoi[3] = 2
		elif 12 <= khoiC < 15:
			tongdiem_khoi[3] = 3
		elif khoiC < 12:
			tongdiem_khoi[3] = 4

		# Check total score and rank D group
		khoiD = tongdiem_khoi[4]
		if khoiD >= 32:
			tongdiem_khoi[4] = 1
		elif 24 <= khoiD < 32:
			tongdiem_khoi[4] = 2
		elif 20 <= khoiD < 24:
			tongdiem_khoi[4] = 3
		elif khoiD < 20:
			tongdiem_khoi[4] = 4

		xeploai_khoi[hs] = tongdiem_khoi

	return xeploai_khoi

def main():
	"""Input file paths of input file 'diem_trungbinh.txt' and output file 'danhgia_hocsinh.txt', evaluate Rank of Academy and Focus Group of Courses, then output to file"""
	# Input full path to open input file "diem_trungbinh.txt"
	open_path = input("- Press Enter to open file if file is in same directory with program.\n- IF NOT same directory, input directory of 'diem_chitiet.txt' file to open (include '\\' at the end of path, not include file name):\n ")
	if len(open_path) <= 1:
		open_path = ""
	input_file = open_path + "diem_trungbinh.txt"

	# Input full path to write output file "danhgia_hocsinh.txt"
	output_path = input("- Press Enter to write file if file is in same directory with program.\n- IF NOT same directory, input directory of 'danhgia_hocsinh.txt' file to write to (include '\\' at the end of path, not include file name):\n ")
	if len(output_path) <= 1:
		output_path = ""
	output_file = output_path + "danhgia_hocsinh.txt"

	# Dictionary of student's IDs and average scores
	hs_diemtb = bangdiem_trungbinh(input_file)

	# Calculate final score of each student and evaluate Ranked Academic
	xeploai_hocluc = xeploai_hocsinh(hs_diemtb)

	# Calculate total score of each Focus Group of Course (FGC), evaluate rank of student for each FGC
	xeploai_khoidaihoc = xeploai_thidaihoc_hocsinh(hs_diemtb)

	# Lists of student's IDs, Ranked Academic, Ranked FGC
	hocsinh = [k for k, v in xeploai_hocluc.items()]
	hocluc = [v for k, v in xeploai_hocluc.items()]
	xeploai = [b for a, b in xeploai_khoidaihoc.items()]


	# List of Ranked Academic and Ranked FGC
	for x in range(len(hocsinh)):
		xeploai[x].insert(0, hocluc[x])

	# Dictionary each student with Ranked Academic and Ranked FGC
	danhgia = {k:v for (k, v) in zip(hocsinh, xeploai)}

	# Write to file, and close file
	try:
		output = open(output_file, "a")

		# First line (title line)
		output.write("Ma HS, xeploai_TB chuan, xeploai_A, xeploai_A1, xeploai_B, xeploai_C, xeploai_D\n")

		# Loop through each student's id and evaluation
		for k, v in danhgia.items():
			text = ""

			# Exclude last item of evaluation to add new line later
			for item in v[:-1]:
				text += str(item) + "; "

			# Add new line at the end
			text += str(v[-1]) +"\n"

			# Content of each line
			output.write(f"{k}; {text}")

	# Always close file
	finally:
		output.close()


if __name__ == "__main__":
	main()
