import subprocess

# Replace with the actual path where tshark.exe is installed
tshark_path = r"C:\Program Files\Wireshark\tshark.exe"

try:
    result = subprocess.run(
        [tshark_path, "-D"],
        capture_output=True,
        text=True
    )
    print("Return code:", result.returncode)
    print("Output:\n", result.stdout)
    print("Errors:\n", result.stderr)
except Exception as e:
    print("Error:", e)
