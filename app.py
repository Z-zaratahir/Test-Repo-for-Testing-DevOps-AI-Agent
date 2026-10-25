from config import fetch_data


def main():
    data = fetch_data("https://api.example.com/items")
    print(data)


if __name__ == "__main__":
    main()
