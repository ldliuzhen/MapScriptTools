import pandas as pd
import re

def compare_lines(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except OSError as e:
        print("Error while reading the file: {}".format(e))
        return
    repeat_count = {}
    repeat_lines = {}
    for i, line in enumerate(lines):
        quoted_strings = re.findall(r'"([^"]*)"', line)  # Extract all quoted strings
        filtered_strings = [s for s in quoted_strings if not (s.startswith('lv_') or s == '()')]  # Filter strings
        for string in filtered_strings:
            if filtered_strings.count(string) > 1:
                if string in repeat_count:
                    repeat_count[string] += 1
                else:
                    repeat_count[string] = 1
                if string in repeat_lines:
                    repeat_lines[string].append(i)
                else:
                    repeat_lines[string] = [i]
    data = {"Quoted String": [], "Line(s)": [], "Count": []}
    for string, count in repeat_count.items():
        lines = ", ".join([str(x) for x in repeat_lines[string]])
        data["Quoted String"].append(string)
        data["Line(s)"].append(lines)
        data["Count"].append(count)
    df = pd.DataFrame(data)
    df.to_excel("output.xlsx", index=False)

file_path = r"C:\Users\hnldl\Desktop\MapScript.galaxy"
compare_lines(file_path)