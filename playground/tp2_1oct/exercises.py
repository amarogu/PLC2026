from re import fullmatch, findall
import sys

def floatNum(word):
    if fullmatch(r'[+-]?(\d+\.\d*|\.\d+)([Ee][+-]?\d+)?', word) is None:
        return False

    return True

def files_8_3(lst):
    result = []
    for i in range(len(lst)):
        if fullmatch(r'[\w~]{1,8}(\.[A-Z]{3})?', lst[i]) is None:
            continue
        result.append(lst[i])
    return result

def euros(text):
    return findall(r'(\d+(?:\.\d+)?)\s*€|€\s*(\d+(?:\.\d+)?)', text)

print(euros('Actually it was €  30.30. So 20.309€,€20.40 maybe? 10!'))
print(files_8_3(["SIMCITY.exe", "DUKE3D.EXE", "LEMMINGS"]))
print(floatNum(sys.argv[1]))