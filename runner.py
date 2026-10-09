import subprocess, sys

test_cases = []

if len(sys.argv) < 3:
    print("Argumen kurang keknya")
    sys.exit()

targ_file = sys.argv[1]
tc_file = sys.argv[2]

# WAJIB PAKE EXTENSION NAMA FILENYA

with open(tc_file, "r") as file:
    for line in file:
        test_cases.append(line.split())

for inputs in test_cases:
    print(f"input = {inputs}")
    runner = subprocess.run([sys.executable, str(targ_file)], input="\n".join(inputs) + "\n", capture_output=True, text=True, timeout=5)
    print(runner.stdout)
    print(runner.stderr)


