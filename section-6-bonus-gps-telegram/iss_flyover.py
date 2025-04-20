from skyfield.api import load, Topos, utc, wgs84
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import os

def get_gps_coordinates():
    import serial
    gps = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=2)
    while True:
        line = gps.readline().decode('ascii', errors='replace').strip()
        if line.startswith("$GPGGA"):
            parts = line.split(',')
            fix = int(parts[6]) if len(parts) > 6 and parts[6].isdigit() else 0
            if fix > 0 and parts[2] and parts[4]:
                lat_raw, lon_raw = parts[2], parts[4]
                lat = float(lat_raw[:2]) + float(lat_raw[2:]) / 60
                lon = float(lon_raw[:3]) + float(lon_raw[3:]) / 60
                if parts[3] == 'S': lat = -lat
                if parts[5] == 'W': lon = -lon
                return lat, lon
            else:
                print("🕐 Waiting for GPS fix...")
        else:
            print(".", end="", flush=True)

def download_tle(path):
    print("📡 Downloading latest ISS TLE data...")
    import requests
    r = requests.get("https://celestrak.org/NORAD/elements/stations.txt")
    with open(path, "w") as f:
        f.write(r.text)

def main():
    lat, lon = get_gps_coordinates()
    print(f"📍 Location acquired: Latitude = {lat:.6f}, Longitude = {lon:.6f}")

    ts = load.timescale()

    tle_path = 'stations.txt'
    if not os.path.exists(tle_path):
        download_tle(tle_path)

    satellites = load.tle_file(tle_path)
    iss = {sat.name: sat for sat in satellites}.get("ISS (ZARYA)")
    if not iss:
        print("❌ ISS not found in TLE data.")
        return

    observer = wgs84.latlon(lat, lon)
    t0 = ts.now()
    t1 = ts.utc(datetime.utcnow().replace(tzinfo=utc) + timedelta(days=2))

    print("\n📆 Upcoming ISS Flyovers:")
    times, events = iss.find_events(observer, t0, t1, altitude_degrees=10.0)
    labels = ['⬆️ Rise above 10°', '🌟 Culminate', '⬇️ Set below 10°']
    kyiv = ZoneInfo("Europe/Kyiv")

    for ti, event in zip(times, events):
        local = ti.utc_datetime().astimezone(kyiv)
        print(f"{local.strftime('%Y-%m-%d %H:%M:%S')} (Kyiv time) — {labels[event]}")

if __name__ == "__main__":
    main()
