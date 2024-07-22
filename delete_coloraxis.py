from os import chdir

# First, enter the path to file QA_VISUALS.txt
# Example path
path = 'C:/DDaCT/SSC-1779/Comparison1'
chdir(path)


def read_delete_coloraxis(path) -> None:
    chdir(path)
    with open("QA_VISUALS.txt", "r") as qa_file:
        lines = qa_file.readlines()

    with open("QA_VISUALS.txt", "w") as new_file:
        for line in lines:
            if not "coloraxis" or not "DDaCT" in line:
                new_file.write(line)


if __name__ == '__main__':
    read_delete_coloraxis(path)
