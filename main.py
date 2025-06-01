import gc
import os
import time

from bs4 import BeautifulSoup
from seleniumbase import SB


def add_text(path, s):
    with open(path, "a") as file:
        # Write the text to be appended
        file.write(f"{s}\n")


def wait_for_string(string_variable, timeout=60):
    start_time = time.time()
    while True:
        if string_variable:  # Checks if the string is not None or empty
            return string_variable
        if time.time() - start_time > timeout:
            raise TimeoutError("Timeout waiting for string to be not null")
        time.sleep(1)


file_path = "target.txt"
if os.path.exists(file_path):
    try:
        with SB(uc=True, test=True, locale="en") as sb, open("target.txt") as file:
            # Iterate through each line in the file
            for line in file:
                processed_line = line.strip()
                print(f"processing: {processed_line}")
                url = f"https://viewdns.info/reverseip/?host={processed_line}&t=1"
                sb.open(url)
                sb.activate_cdp_mode(url)
                while "a moment" in sb.get_title():
                    sb.uc_gui_click_captcha()
                    sb.sleep(2)

                source = sb.get_page_source()
                try:
                    output = wait_for_string(source)
                    soup = BeautifulSoup(source, "html.parser")
                    table = soup.find("table", attrs={"class": "min-w-full"})
                    rows = []
                    try:
                        for row in table.find_all("tr")[1:]:
                            cells = [td.text.strip() for td in row.find("td", attrs={"class": "font-medium"})]
                            rows.append("".join(cells))
                        for row in rows:
                            add_text("./result.txt", row)
                    except AttributeError:
                        add_text("./recheck.txt", processed_line)
                    except Exception as e:
                        print(e)

                except TimeoutError as e:
                    print(e)

                gc.collect()
                sb.sleep(5)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
else:
    print(f"Error: The file '{file_path}' does not exist.")
