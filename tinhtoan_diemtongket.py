
# Open file, get data and Close file
def read_file(fname):
    """Extract data from file"""
    f = open(fname, "r")
    try:
        data = f.readlines()
        return data
    finally:
        f.close()


def hocsinh_bangdiem(input_data):
    """Create a dictionary of student's ids and courses's scores: {id: {course: score}}"""
    # List of courses
    monhoc = input_data[0].split(',')
    monhoc.pop(0)
    for x in range(len(monhoc)):
        monhoc[x] = monhoc[x].strip()


    # All scores of each student
    bangdiem = {}

    # List of studen's ids
    mahocsinh = []

    # Get information from file, exclude first line (titles line)
    for line in input_data[1:]:
        # Append each student's id to student's ids list
        mahocsinh.append(line[0])

        # Get all scores and exclude student's id
        diem = line.split()[1]

        # Create dictionaries contains each course's scores
        diem_tungmon = diem.split(";")

        # Dictionary of each student and his/her scores
        bangdiem[line[0]] = {k: v for (k, v) in zip(monhoc, diem_tungmon)}

    return bangdiem


#============================1.a Ham tinhdiem_trungbinh======================================
def tinhdiem_trungbinh(input_bangdiem):
    """Create a dictionary of student's ids and courses's average scores: {id: {course: average_score}}"""
    hs_tb = {}
    # Loop through courses and their scores of each student
    for hs, bd in input_bangdiem.items():
        tb = {}

        # Loop through scores of each course of each student
        for monhoc, diemmon in bd.items():
            int_diemmon = []

            # Convert each score into integer
            for diem in diemmon.split(","):
                int_diemmon.append(int(diem))

            # average score of science course (4 scores)
            if len(int_diemmon) == 4:
                tb[monhoc] = round(int_diemmon[0] * 0.05 + int_diemmon[1] * 0.1 + int_diemmon[2] * 0.15 + int_diemmon[3] * 0.7, 2)
            # average score of social course (5 scores)
            elif len(int_diemmon) == 5:
                tb[monhoc] = round(int_diemmon[0] * 0.05 + int_diemmon[1] * 0.1 + int_diemmon[2] * 0.1 + int_diemmon[3] * 0.15 + int_diemmon[4] * 0.6, 2)

        # average scores of each student:
        hs_tb[hs] = tb

    return hs_tb


#============================1.b Ham luudiem_trungbinh======================================
def luudiem_trungbinh(input_file, input_data, input_bangdiemtb):
    """
    - Create file to input directory (file_path parameter)
    - Get title line from originale file's data (data parameter), get student's ids and average scores (bangdiemtb parameter)
    - Create file 'diem_trungbinh.txt' at input file path (where to create file, need a backslash at the end of path)
    - Write title line, student's ids and average scores of each id according to each course
    """
    # Get titles line
    title = input_data[0]

    # Get a list of courses
    monhoc = title.split(',')[1:]
    for x in range(len(monhoc)):
        monhoc[x] = monhoc[x].strip()

    try:
        # Get directory and file name and append to it (write to the end of the file)
        luu_file = open(input_file, "a")
        luu_file.write(title)

        for hs, diemtb in input_bangdiemtb.items():
            # Start line with student's ids
            tb_hs = f"{hs}; "

            # Loop through each course's average score and convert it to string
            for mon, diem in diemtb.items():
                # If it is last score, make new line for new student's id
                if mon == list(diemtb.keys())[-1]:
                    tb_hs += str(diem) + "\n"
                # If not last score, concatenate to student's id, separate by ";"
                else:
                    tb_hs += str(diem) + ";"

            # Write to the end of file: ID; average scores
            luu_file.write(tb_hs)
    finally:
        luu_file.close() 


#============================1.c Ham main======================================
def main():
    """Input file paths of input file 'diem_chitiet.txt' and output file 'diem_trungbinh.txt', calculate average scores and output to file"""
    # Input full path to open input file "diem_chitiet.txt"
    open_path = input("- Press Enter to open file if file is in same directory with program.\n- IF NOT same directory, input directory of 'diem_chitiet.txt' file to open (include '\\' at the end of path, not include file name):\n ")
    if len(open_path) <= 1:
        open_path = ""
    open_file = open_path + "diem_chitiet.txt"

    # Input full path to write output file "diem_trungbinh.txt"
    write_path = input("- Press Enter to write file if file is in same directory with program.\n- IF NOT same directory, input directory of 'diem_trungbinh.txt' file to write to (include '\\' at the end of path, not include file name):\n ")
    if len(write_path) <= 1:
        write_path = ""
    write_file = write_path + "diem_trungbinh.txt"


    # Get all data from original file
    data = read_file(open_file)

    # Create dictionary of student's id and scores of each course: {id1: {course: score}, id2:{course: score}}
    bangdiem = hocsinh_bangdiem(data)

    # Create dictionary of student's id and average score of each course: {id1: {course: average_score}, id2:{course: average_score}}
    diemtrungbinh = tinhdiem_trungbinh(bangdiem)
    print(diemtrungbinh)

    # Create file "diem_trungbinh.txt" to input directory which contain courses (title line), student's ids, and average scores
    luudiem_trungbinh(write_file, data, diemtrungbinh)



if __name__ == "__main__":
    main()
