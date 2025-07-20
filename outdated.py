def main():
    while True:
        try:
            date = input("Date: ").strip()

            # Try Month Day, Year format
            if "," in date:
                month_day, year = date.split(",")
                month, day = month_day.strip().split()
                day = int(day)
                month = month.lower().capitalize()

                months = {
                    "January": 1, "February": 2, "March": 3, "April": 4,
                    "May": 5, "June": 6, "July": 7, "August": 8,
                    "September": 9, "October": 10, "November": 11, "December": 12
                }

                if month not in months or not (1 <= day <= 31):
                    continue

                print(f"{int(year.strip())}-{months[month]:02}-{day:02}")
                break

            else:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)

                if not (1 <= month <= 12 and 1 <= day <= 31):
                    continue

                print(f"{int(year):04}-{month:02}-{day:02}")
                break

        except (ValueError, IndexError):
            continue  


if __name__ == "__main__":
    main()
