# -Network-Port-Scanner

สคริปต์ Python สำหรับตรวจสอบพอร์ตบนอุปกรณ์เครือข่ายและ IoT เช่น IP Camera, DVR/NVR  
รองรับการส่งทราฟฟิกผ่าน Proxy Server (SOCKS4, SOCKS5, HTTP) เพื่อการทดสอบความปลอดภัยจากภายนอกเครือข่าย

---

- **TCP Connect Scan** — ใช้ `socket.connect_ex()` ตามมาตรฐาน RFC 793
- **Proxy Support** — รองรับ SOCKS4, SOCKS5 และ HTTP Proxy ผ่านโมดูล PySocks
- **IP Concealment** — ซ่อน IP จริงด้วยเทคนิค Socket Overriding
- **IoT-focused Port List** — ครอบคลุมพอร์ตยอดนิยมของกล้องวงจรปิดและอุปกรณ์เครือข่าย

---

## หลักการทำงาน

สคริปต์ใช้การสแกนแบบ **TCP Connect Scan** ซึ่งจำลองกระบวนการ 3-Way Handshake ของโปรโตคอล TCP:

```
[Client] ──── SYN ────────────► [Target]
[Client] ◄─── SYN-ACK ─────── [Target]   ← พอร์ตเปิดอยู่
[Client] ──── ACK ────────────► [Target]
```

การซ่อน IP จริงทำผ่าน **Socket Overriding** โดย PySocks จะเข้าควบคุม socket ในระดับ OS:

```python
socks.set_default_proxy(PROXY_TYPE, PROXY_HOST, PROXY_PORT)
socket.socket = socks.socksocket
```

---

## Installation

```bash
pip install PySocks
```

---

## Usage

แก้ไขตัวแปรใน Configuration Section ก่อนรันสคริปต์:

```python
# Proxy Settings
PROXY_HOST = "your.proxy.server"   # IP หรือ Domain ของ Proxy
PROXY_PORT = 1080                   # พอร์ตของ Proxy
PROXY_TYPE = socks.SOCKS5           # เลือก: SOCKS4 / SOCKS5 / HTTP

# Target Settings
target_ip     = "192.168.1.100"
ports_to_scan = [21, 22, 23, 80, 443, 554, 1935, 37777, 8000, 8080, 81, 82, 83, 88, 5000, 9000]
```

```bash
python scanner.py
```

---

## Configuration Variables

| ตัวแปร | คำอธิบาย |
|---|---|
| `PROXY_HOST` | IP หรือ Domain ของ Proxy Server |
| `PROXY_PORT` | พอร์ตของ Proxy Server |
| `PROXY_TYPE` | โปรโตคอล (`socks.SOCKS4` / `socks.SOCKS5` / `socks.HTTP`) |
| `target_ip` | IP ของอุปกรณ์เป้าหมาย |
| `ports_to_scan` | List ของพอร์ตที่ต้องการสแกน |

---

## 🔌 Port Reference — กล้องวงจรปิด & IoT

### Web Management (หน้าเว็บตั้งค่า)

| Port | Protocol | คำอธิบาย |
|---|---|---|
| 80 | HTTP | หน้า Web UI มาตรฐาน — เสี่ยงหากไม่เปลี่ยน Default Password |
| 443 | HTTPS | เวอร์ชัน Encrypted ของ Port 80 |
| 8080, 81, 82, 83, 88 | HTTP Alt | พอร์ตทางเลือก — มักถูกเปลี่ยนเพื่อหลบการสแกนอัตโนมัติ |

### Video Streaming

| Port | Protocol | คำอธิบาย |
|---|---|---|
| 554 | RTSP | ดึงภาพสดจากกล้อง — หากไม่มีรหัสผ่าน ดูได้ทันทีผ่าน VLC |
| 1935 | RTMP | สตรีมภาพไปยังแพลตฟอร์มออนไลน์ |

### Vendor-Specific SDK

| Port | Brand | คำอธิบาย |
|---|---|---|
| 8000 | Hikvision | เชื่อมต่อแอป iVMS และโปรแกรมจัดการ |
| 37777 | Dahua | รับส่งข้อมูลผ่านแอป DMSS |
| 9000, 5000 | Generic | กล้อง IP ทั่วไปจากผู้ผลิตจีน |

### Management & File Transfer

| Port | Protocol | คำอธิบาย |
|---|---|---|
| 21 | FTP | ส่งไฟล์ภาพ/วิดีโอขึ้น Storage Server |
| 22 | SSH | Remote Access แบบเข้ารหัส — ใช้งานโดยช่างเทคนิค |
| 23 | Telnet | Remote Access แบบ Plaintext — **อันตรายมาก** เสี่ยงต่อ Botnet |

---

## Legal Disclaimer

> สคริปต์นี้จัดทำขึ้นเพื่อวัตถุประสงค์ด้าน **การศึกษา** และ **การทดสอบความปลอดภัย (Penetration Testing)** บนระบบที่คุณมีสิทธิ์เข้าถึงเท่านั้น
>
> **การใช้งานบนระบบหรืออุปกรณ์ที่ไม่ได้รับอนุญาตถือเป็นความผิดทางกฎหมาย**  
> ผู้พัฒนาไม่รับผิดชอบต่อความเสียหายหรือการกระทำที่ผิดกฎหมายทุกกรณี

---

## License

MIT License
