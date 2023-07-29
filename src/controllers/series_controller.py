from src.entities.championship import Championship
from src.entities.series import Series

class SeriesController:

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_number_of_series():
        while True:
            try:
                num_series = int(input("Enter the number of series to be played: "))
                if num_series <= 0:
                    print("Number of series must be greater than 0.")
                else:
                    return num_series
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    @staticmethod
    def get_series_type(series_num):
        while True:
            series_type = input(f"Enter the type 1 for RANKED or 2 for RANDOM Series {series_num}: ").lower()
            if series_type in ['1', '2']:
                return series_type
            else:
                print("Invalid input. Please enter 1 for 'ranked' or 2 for 'random'.")

    @staticmethod
    def assess_series_type(championship):
        random_series = 0
        for series_type in championship.seriesArr:
            if series_type == 1:
                # Handle ranked series, if needed
                pass
            elif series_type == 2:
                random_series+=1
            else:
                print(f"Invalid series type {series_type}. Skipping...")
        return random_series
