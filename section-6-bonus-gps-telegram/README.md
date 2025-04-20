# GPS Module Reader

This script reads NMEA data from a GPS module connected to your Raspberry Pi (via USB or GPIO) and extracts live latitude and longitude once a satellite fix is obtained.

## 📂 Files

- **gps_reader.py** — The Python script to read and parse NMEA `$GPGGA` sentences.

## 🔧 Setup

1. **Activate your virtual environment**:  
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies**:  
   ```bash
   pip install pyserial
   ```

3. **Choose your connection type**:  
   - **USB GPS dongle** (e.g., NEO-6M Mini SMA): device path likely `/dev/ttyUSB0` or `/dev/ttyACM0`.  
   - **GPIO wiring** with a NEO-6M breakout: use `/dev/serial0` (enable hardware serial in `raspi-config`).

4. **Update the port in `gps_reader.py`**:  
   Edit the `PORT` variable at the top of the script to match your detected device:
   ```python
   PORT = '/dev/ttyACM0'  # or '/dev/ttyUSB0' or '/dev/serial0'
   ```

## 🚀 Run the Script

```bash
python gps_reader.py
```

- You will see lines like:
  - `🕐 Waiting for GPS fix...` until satellites are locked.
  - `✅ GPS fix acquired: Latitude = xx.xxxxxx, Longitude = yy.yyyyyy` when a fix is obtained.

## ⚙️ How It Works

1. Opens the serial port at the specified `PORT` and `baudrate=9600`.
2. Reads NMEA sentences continuously.
3. Filters `$GPGGA` lines, parses the fields to determine fix quality and coordinates.
4. Converts latitude/longitude from degrees+minutes format to decimal degrees.
5. Prints diagnostic messages and coordinates.

