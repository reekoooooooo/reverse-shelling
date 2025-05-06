# reverse-shelling
Reverse Shell Simulation and Malware Analysis (Educational) 🔐

🧠 Educational Malware Simulation Lab
Created by Reeko Long | For ethical use only in isolated environments

# 🛡️ Educational Malware Simulation Lab

A beginner-friendly simulation of two common malware techniques — a Python-based reverse shell and keylogger — built and tested inside a secure Kali Linux virtual environment. This project was created for educational and cybersecurity training purposes only.


## 🧩 Features
- Reverse shell for remote command execution
- Base64 obfuscation for simple evasion
- Keylogger using `pynput`
- Real-time traffic monitoring with `tcpdump`
- Ethical implementation in isolated VM lab

## ⚙️ How to Run This Lab

> 🧠 Tested inside Kali Linux in VMware for full isolation

### 🔁 Reverse Shell
1. On attacker terminal:
    ```bash
    nc -lvnp 4444
    ```

2. On victim terminal:
    ```bash
    python3 reverse_shell.py
    ```

3. Send commands like:
    ```bash
    echo -n "whoami" | base64
    ```

---

### ⌨️ Keylogger
1. In new terminal:
    ```bash
    python3 keylogger.py
    ```
2. Type anywhere (terminal, browser)
3. Press `CTRL+C` to stop and view logs:
    ```bash
    cat keylog.txt
    ```
## ⚠️ Legal + Ethical Disclaimer

This project is for educational purposes only and should only be run in a safe, isolated lab environment. Do not use, deploy, or test any part of this code on systems you do not own or have explicit permission to analyze.

The goal is to understand how attackers operate — so we can stop them.

## 💡 What I Learned
- How reverse shells work under the hood
- Python socket programming
- Simple evasion techniques using Base64
- Linux terminal command automation
- How to detect and analyze basic malware
- The importance of safe, ethical red team simulation

---
## 📸 Screenshots

### 🔁 Reverse Shell Python Code
![Reverse Shell Code](screenshots/reverser%20shell%20code.png)

### 📟 Keylogger Output Example
![Keylogger Output](screenshots/keylogger%20output.png)

### ⌨️ Keylogger Source Code
![Keylogger Code](screenshots/keylogger%20code.png)

### 🔒 Obfuscation Code Block
![Obfuscation Code](screenshots/obfuscation%20code.png)

### 🔐 Base64 Encoded Command
![Base64 Command](screenshots/Obfuscation.png)

### 🎯 Attacker and Victim Terminals
![Attacker and Victim](screenshots/Attacker%20and%20victim.png)

**Next Steps / Improvements**
```md
## 🚀 Future Improvements
- Send `keylog.txt` to attacker over TCP
- Add stealth + anti-debug tricks
- Combine keylogger + reverse shell
- Convert to `.exe` for Windows testing (safely)
