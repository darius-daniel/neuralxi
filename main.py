#!/usr/bin/python3
"""
Entry point for the project
"""
from src.process_data import create_player_dataframe
from src.fetch_data import get_general_fpl_data

MY_TEAM_ID = 7777090


if __name__ == "__main__":
    fpl_data = get_general_fpl_data()
    if fpl_data:
        df = create_player_dataframe(fpl_data)
        print(df.head())