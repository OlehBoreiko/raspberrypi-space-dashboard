import serial  # Library to read from serial ports

def parse_gpgga(sentence):
    # Parse NMEA $GPGGA sentence to extract fix status and coordinates
    try:
        parts = sentence.split(",")
        
        # Extract fix quality (0 = no fix, 1 = GPS fix, 2 = DGPS fix)
        fix = int(parts[6]) if len(parts) > 6 and parts[6].isdigit() else 0

        # If valid fix and coordinate fields are present
        if parts[2] and parts[4] and fix > 0:
            # Latitude is in format DDMM.MMMM
            lat_raw = parts[2]
            lat = float(lat_raw[:2]) + float(lat_raw[2:]) / 60

            # Longitude is in format DDDMM.MMMM
            lon_raw = parts[4]
            lon = float(lon_raw[:3]) + float(lon_raw[3:]) / 60

            # Adjust for southern and western hemispheres
            if parts[3] == 'S':
                lat = -lat
            if parts[5] == 'W':
                lon = -lon

            return lat, lon, fix

    except Exception as e:
        print("Parsing error:", e)

    return None, None, 0  # Default: no fix

def main():
    # Open GPS serial port
    with serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1) as gps:
        print("📡 Reading GPS data from /dev/ttyACM0 ...")
        
        while True:
            # Read one NMEA sentence
            line = gps.readline().decode('ascii', errors='replace').strip()

            # Filter for $GPGGA lines (position + fix info)
            if line.startswith("$GPGGA"):
                lat, lon, fix = parse_gpgga(line)

                if fix == 0:
                    print("🕐 Waiting for GPS fix... (no satellites locked)")
                elif lat and lon:
                    print(f"✅ GPS fix acquired: Latitude = {lat:.6f}, Longitude = {lon:.6f}")

if __name__ == "__main__":
    main()
