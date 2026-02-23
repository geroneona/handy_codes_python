import speedtest
import time

# ANSI color codes for colored output
def color_font(selected_color):
    if selected_color == 'red':
        return '\033[91m'
    if selected_color == 'green':
        return '\033[92m'
    if selected_color == 'yellow':
        return '\033[93m'
    if selected_color == 'reset':
        return '\033[0m'

def test_speed():
    """
    Performs an internet speed test and prints the results.
    """
    st = speedtest.Speedtest()

    print("Finding the best server...")
    st.get_best_server() # This selects the nearest server for the most accurate results

    print("Performing download test...")
    download_speed = st.download() # Speed in bytes per second

    print("Performing upload test...")
    upload_speed = st.upload() # Speed in bytes per second

    ping_result = st.results.ping # Ping in milliseconds

    # Convert speeds to Mbps (Megabits per second) and format
    download_speed_mbps = download_speed / 1_000_000
    upload_speed_mbps = upload_speed / 1_000_000

    print(f"\n--- Internet Speed Test Results ---")
    print(f"Download Speed: {color_font(selected_color='red') if download_speed_mbps <= 5 else color_font(selected_color='yellow')}{download_speed_mbps:.2f} Mbps{color_font(selected_color='reset')}")
    print(f"Upload Speed: {color_font(selected_color='red') if download_speed_mbps <= 5 else color_font(selected_color='yellow')}{upload_speed_mbps:.2f} Mbps{color_font(selected_color='reset')}")
    print(f"Ping: {ping_result:.2f} ms")
    print("---------------------------------")
    print(f"{color_font(selected_color='yellow')}Log time at {time.strftime('%Y-%m-%d %H:%M:%S')}{color_font(selected_color='reset')}")
    print("Checking again after 15mins...\n")

    with open('localnetspeedcheck_every15mins.txt', 'a') as log_file:
        log_file.write(f"Internet Speed Test Results at {time.strftime('%Y-%m-%d %H:%M:%S')}: Download Speed: {download_speed_mbps:.2f} Mbps | Upload Speed: {upload_speed_mbps:.2f} Mbps | Ping: {ping_result:.2f} ms\n")

if __name__ == "__main__":
    while True:
        test_speed()
        time.sleep(15 * 60) # check every 15 mins
