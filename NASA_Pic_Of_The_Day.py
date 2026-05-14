from datetime import datetime
from datetime import timedelta
import requests


def get_apod(date_scr=None):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": "DEMO_KEY"}
    if date_scr:
        params["date"] = date_scr
    try:
        r = requests.get(url, params=params, timeout=6)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"NASA API Error: {e}")
        return None

def show_apod():
    choice = input("Enter Date (YYYY-MM-DD) or empty for today/random: ").strip()
    if not choice:
        for offset in [0, -1, -2]:
            d = (datetime.now() - timedelta(days=offset)).strftime("%Y-%m-%d")
            data = get_apod(d)
            if data and data.get("media_type") == "image":
                break
            else:
                data = None
    else:
        data = get_apod(choice)

    if not data:
        print("Could not fetch APOD.")
        return

    print(f"\nNASA Astronomy Picture - {data['date']}")
    print(f"Title: {data['title']}")
    print("-" * 60)
    print(data["explanation"][:400] + "..." if len(data["explanation"]) > 400 else data['explanation'])
    print("-" * 60)

def main():
    print("NASA APOD Viewer (Astronomy Picture of the Day)\n")
    while True:
        print("1.  Show Today's Recent APOD")
        print("2.  Exit")
        ch = input("Enter your choice (1 or 2): ")
        if ch == "1":
            show_apod()
        elif ch == "2":
            break

if __name__ == "__main__":
    main()



