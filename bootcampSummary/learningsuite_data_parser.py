import argparse
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "-m",
    "--modules",
    help="creates summaries for each module, include directory of csv files as argument",
)
parser.add_argument("-f", "--file", help="collects the module data for a single file")
parser.add_argument(
    "-p",
    "--participants",
    help="creates summaries for each student, include directory of csv files as argument",
)
parser.add_argument(
    "-s", "--summary", help="creates a summary for bootcamp participation"
)
args = parser.parse_args()

# establish paths, make directory
home_path = os.path.expanduser("~/")
ran_in_path = os.getcwd()
moduleSummaries_dir_path = os.path.join(ran_in_path, "moduleSummaries")
participantSummaries_dir_path = os.path.join(ran_in_path, "participantSummaries")
bootcampSummary_dir_path = os.path.join(ran_in_path, "bootcampSummary")
temptxt_path = os.path.join(moduleSummaries_dir_path, "temp.txt")

# correct the csv file from learning suite and put it in temp.txt
def fix_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        lines[0] = lines[0].strip()
        lines[0] = f"{lines[0]},\n"
        del lines[1:6]
        fixed = "".join(lines)
        os.chdir(moduleSummaries_dir_path)
        with open("temp.txt", "w") as newf:
            newf.write(fixed)
        os.chdir(data_dir_path)


# create data summaries for each module
def get_module_info(file_name, data):
    float_hours = []
    for value in data.iloc[:, 7]:
        if not pd.isnull(value):
            float_hours.insert(0, value)
    string_hours = [str(x) for x in float_hours]
    comments = [str(x) for x in data.iloc[:, 9]]
    if file_name[0:38] == "Student Answers for Computing Bootcamp":
        new_file_name = f"{file_name[39:-4].replace(' ', '')}_Results.txt"
    elif file_name[-11:] == "_Module.csv":
        new_file_name = f"{file_name[:-11]}_Results.txt"
    else:
        new_file_name = f"{file_name[:-4]}_Results.txt"
    os.chdir(moduleSummaries_dir_path)
    with open(new_file_name, "w") as out:
        out.write(f"Time Spent\n{'-'*100}\n")
        out.write(f"  - Mean: {np.mean(float_hours)}\n")
        out.write(f"  - Median: {np.median(float_hours)}\n")
        out.write(f"  - Max: {max(float_hours)}\n")
        out.write(f"  - Min: {min(float_hours)}\n")
        out.write(f"  - Full Data: {', '.join(np.sort(string_hours))}\n\n")
        out.write(f"Comments\n{'-'*100}\n")
        for comment in comments:
            if comment.find("nan"):
                out.write((f"  - {comment}\n"))
    os.remove(temptxt_path)
    os.chdir(data_dir_path)


# read module data and organize data by student
def get_student_info(file_name, data):
    if file_name[0:38] == "Student Answers for Computing Bootcamp":
        module_name = file_name[39:-4].replace(" ", "")
    elif file_name[-11:] == "_Module.csv":
        module_name = file_name[:-11]
    else:
        module_name = file_name[:-4]
    student_list = data.iloc[:, 0]
    i = 0
    for student in student_list:
        if student not in student_modules:
            student_modules[student] = []
            student_hours[student] = []
        student_data = data.iloc[i, :]
        if student_data[6] == "A":
            student_modules[student].append(module_name)
        student_hours[student].append(student_data[7])
        i = i + 1


# create a textfile for each student from student data
def create_student_summaries():
    os.chdir(participantSummaries_dir_path)
    for student in student_modules:
        new_file_name = f'{student.replace(" ", "")}_Results.txt'
        total_time = 0
        for value in student_hours[student]:
            if not pd.isnull(value):
                total_time = total_time + value
        if total_time != 0:
            with open(new_file_name, "w") as out:
                out.write(
                    f"{student} completed {len(student_modules[student])} modules:\n"
                )
                for mod in student_modules[student]:
                    out.write(f"    {mod}\n")
                out.write(f"\nTotal hours spent: {total_time}\n")


# remove students who have completed 0 modules
def remove_nonparticipants(modules, hours):
    new_modules = {}
    new_hours = {}
    for student in modules:
        if len(modules[student]) < 1:
            zero_modules_completed.append(student)
    for student in modules:
        if student not in zero_modules_completed:
            new_modules[student] = len(modules[student])
    for student in student_hours:
        if student not in zero_modules_completed:
            total_time = 0
            for value in student_hours[student]:
                if not pd.isnull(value):
                    total_time = total_time + value
            new_hours[student] = total_time
    return new_modules, new_hours


def get_module_summary_info():
    if file_name[0:38] == "Student Answers for Computing Bootcamp":
        module_name = file_name[39:-4].replace(" ", "")
    elif file_name[-11:] == "_Module.csv":
        module_name = file_name[:-11]
    else:
        module_name = file_name[:-4]
    float_hours = []
    num_participants = 0
    for value in data.iloc[:, 7]:
        if not pd.isnull(value):
            float_hours.insert(0, value)
    student_list = data.iloc[:, 0]
    i = 0
    for student in student_list:
        student_data = data.iloc[i, :]
        if student_data[6] == "A":
            num_participants = num_participants + 1
        i = i + 1
    module_participants[module_name] = num_participants
    module_hours[module_name] = sum(float_hours)


# create file and histograms that give overall sumamry of data
def create_full_summary():
    os.chdir(bootcampSummary_dir_path)
    time_data = []
    num_modules_data = []
    modules_list = list(module_participants.keys())
    modules_hours_list = list(module_hours.values())
    module_participants_list = list(module_participants.values())
    for student in student_hours:
        time_data.append(student_hours[student])
    for student in student_modules:
        num_modules_data.append(student_modules[student])
    time_data = np.sort(time_data)
    string_time_data = [str(x) for x in time_data]
    num_modules_data = np.sort(num_modules_data)
    string_num_modules_data = [str(x) for x in num_modules_data]
    fig, axs = plt.subplots(2)
    axs[0].hist(time_data, bins=10)
    axs[0].set_title("Time Spent By Each Participant")
    axs[1].hist(num_modules_data, bins=16)
    axs[1].set_title("Modules Completed By Each Participant")
    plt.subplots_adjust(
        left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3
    )
    plt.savefig("histograms.png")
    plt.close()
    font = {"size": 6}
    plt.rc("font", **font)
    plt.subplot(211)
    plt.bar(modules_list, module_participants_list)
    plt.title("Participants By Module")
    plt.xticks(rotation=40, ha="right")
    plt.subplot(212)
    plt.bar(modules_list, modules_hours_list)
    plt.title("Time Spent By Module")
    plt.xticks(rotation=30, ha="right")
    plt.subplots_adjust(
        left=None, bottom=0.2, right=None, top=None, wspace=None, hspace=0.8
    )
    plt.savefig("barGraphs.png")

    max_time = max(time_data)
    min_time = min(time_data)
    for student in student_hours:
        if student_hours[student] == max_time:
            max_student = student
        if student_hours[student] == min_time:
            min_student = student
    with open("Bootcamp_Summary.txt", "w") as out:
        num_students = len(student_modules)
        num_inactive = len(zero_modules_completed)
        total_hours = sum(time_data)
        total_modules = sum(num_modules_data)
        out.write(f"Total Participants: {num_students + num_inactive}\n")
        out.write(f"Participants with 0 modules completed: {num_inactive}\n\n")
        out.write(f"Actual Participants: {num_students}\n")
        out.write(f"Total Hours Spent: {total_hours}\n")
        out.write(f"Mean Time Spent: {np.mean(time_data)}\n")
        out.write(f"Median Time Spent: {np.median(time_data)}\n")
        out.write(
            f"Max Time Spent: {max_time} ({student_modules[max_student]} modules)\n"
        )
        out.write(
            f"Min Time Spent: {min_time} ({student_modules[min_student]} modules)\n"
        )
        out.write(f"Average Time Per Module: {total_hours/total_modules}")
        # out.write(f"Full Time Data: {', '.join(string_time_data)}\n")
        # out.write(f"Full Modules Data: {', '.join(string_num_modules_data)}\n")


# main()
if args.file:
    if not os.path.isdir(moduleSummaries_dir_path):
        os.mkdir(moduleSummaries_dir_path)
    fix_file(args.file)
    data = pd.read_csv("temp.txt")
    get_module_info(args.file, data)
    os.remove(temptxt_path)
elif args.modules:
    if not os.path.isdir(moduleSummaries_dir_path):
        os.mkdir(moduleSummaries_dir_path)
    data_dir_path = os.path.join(ran_in_path, args.modules)
    for file_name in os.listdir(data_dir_path):
        os.chdir(data_dir_path)
        fix_file(file_name)
        data = pd.read_csv(temptxt_path)
        get_module_info(file_name, data)
elif args.participants:
    if not os.path.isdir(participantSummaries_dir_path):
        os.mkdir(participantSummaries_dir_path)
    data_dir_path = os.path.join(ran_in_path, args.participants)
    student_modules = {}
    student_hours = {}
    for file_name in os.listdir(data_dir_path):
        os.chdir(data_dir_path)
        fix_file(file_name)
        data = pd.read_csv(temptxt_path)
        get_student_info(file_name, data)
    os.remove(temptxt_path)
    create_student_summaries()
elif args.summary:
    if not os.path.isdir(bootcampSummary_dir_path):
        os.mkdir(bootcampSummary_dir_path)
    data_dir_path = os.path.join(ran_in_path, args.summary)
    student_modules = {}
    student_hours = {}
    module_participants = {}
    module_hours = {}
    for file_name in os.listdir(data_dir_path):
        os.chdir(data_dir_path)
        fix_file(file_name)
        data = pd.read_csv(temptxt_path)
        get_student_info(file_name, data)
        get_module_summary_info()
    os.remove(temptxt_path)
    zero_modules_completed = []
    student_modules, student_hours = remove_nonparticipants(
        student_modules, student_hours
    )
    create_full_summary()
else:
    print("No options were selected, use -h option for help")
