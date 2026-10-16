#!/usr/bin/env python3
# python

import subprocess
import shlex
import sys

def run(cmd):
    res = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
    if res.returncode != 0:
        print("Command failed:", cmd, file=sys.stderr)
        print(res.stderr, file=sys.stderr)
        raise SystemExit(res.returncode)
    return res.stdout

def compile_sketch(sketch_path, fqbn):
    cmd = f"arduino-cli compile --fqbn {fqbn} {sketch_path}"
    return run(cmd)

def upload_sketch(sketch_path, fqbn, port):
    cmd = f"arduino-cli upload -p {port} --fqbn {fqbn} {sketch_path}"
    return run(cmd)

if __name__ == "__main__":
    # Edit these for your setup
    fqbn = "arduino:avr:uno"      # example for UNO
    sketch_path = r"\Servo\Servo_ctrl\Servo_ctrl.ino"  # folder containing the .ino
    port = "COM3"

    print("Compiling...")
    print(compile_sketch(sketch_path, fqbn))

    print("Uploading...")
    print(upload_sketch(sketch_path, fqbn, port))

    print("Done.")