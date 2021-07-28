import os


def setup():
    print(10*'=' + ' App setup ' + 10*'=')

    downloads_path = str(
        input('Downloads folder path (always use / and, if in the same dir, use ./): '))
    driver_path = str(
        input('Web driver path (always use / and, if in the same dir, use ./): '))

    with open('./.env', 'w') as file:
        file.write(f"""DRIVER_PATH="{os.path.abspath(driver_path)}"
DOWNLOADS_PATH="{os.path.abspath(downloads_path)}"
""")


if __name__ == '__main__':
    setup()
