from os import chdir

#First, enter the path to file QA_VISUALS.txt
#Example path
path = 'C:/DDaCT/SSC-1779/Comparison1'
chdir(path)

with open("QA_VISUALS.txt", "r") as qa_file:
    lines = qa_file.readlines()

with open("sample.txt", "w") as new_file:
    for line in lines:
        if not "coloraxis" in line:
            new_file.write(line)
