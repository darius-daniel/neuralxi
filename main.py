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
        df = create_player_dataframe(fpl_data['elements'], fpl_data['teams'], fpl_data['element_types'])
        print(df.head())

    print("element keys")
    for key in fpl_data['elements'][0].keys():
        print(key)