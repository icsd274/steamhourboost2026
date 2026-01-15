from steam.client import SteamClient
from getpass import getpass
import time

games = [730]  # CS2

username = input("Steam username: ")
password = getpass("Steam password: ")

client = SteamClient()

def login():
    result = client.login(username=username, password=password)

    if result == 85:  # Steam Guard Mobile
        code = input("Steam Guard (mobile) code: ")
        result = client.login(
            username=username,
            password=password,
            two_factor_code=code
        )

    elif result == 63:  # Steam Guard Email
        code = input("Steam Guard (email) code: ")
        result = client.login(
            username=username,
            password=password,
            auth_code=code
        )

    return result

while True:
    try:
        print("Logging in...")
        result = login()

        if result != 1:
            print(f"Login failed: {result}")
            time.sleep(60)
            continue

        print("Logged in. Playing CS2...")
        client.games_played(games)
        client.run_forever()

    except Exception as e:
        print("ERROR:", e)

    print("Disconnected. Reconnecting in 30 seconds...")
    try:
        client.logout()
    except:
        pass

    time.sleep(30)
