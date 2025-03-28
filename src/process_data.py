import pandas as pd
from typing import Dict, Sequence, Any
import logging


def create_dataframe(data: Dict[str, Any] | Sequence[Dict[str, Any]]) -> pd.DataFrame:
    """
    Create a new data frame from the data returned by the data fetching functions
    :param data: raw data from data fetching functions
    :return: new pandas data frame created from the raw data. If data is falsy, data frame will be empty
    """
    if not data:
        logging.error("create_dataframe: Invalid input data format")

    return pd.DataFrame(data)


def clean_player_data(
        player_dataframe: pd.DataFrame,
        epl_teams: Sequence[Dict[str, Any]],
        element_types: Sequence[Dict[str, Any]]) -> pd.DataFrame:
    """
    Clean up the information in the player dataframe by renaming column names,
    dropping unneeded columns, converting values to appropriate and intuitive formats and types.
    :param player_dataframe: data frame containing relevant data for all players in the EPL
    :param epl_teams: array of dictionaries that contain data about each EPL team
    :param element_types: Array of dictionaries that contain data about each element type, e.g. GK, DEF, MID, FWD, MGR
    :return: the transformed player dataframe
    """
    # Select the relevant columns
    relevant_cols = [
        'web_name', 'team', 'element_type',
        'minutes', 'goals_scored', 'assists',
        'clean_sheets', 'total_points', 'now_cost',
        'points_per_game', 'selected_by_percent', 'form'
    ]
    player_dataframe = player_dataframe[relevant_cols]

    # Rename the columns for readability and consistency
    player_dataframe.rename(columns={
        'team': 'Team',
        'web_name': 'Player',
        'element_type': 'Position',
        'now_cost': 'Price (£mil.)',
        'minutes': 'Minutes',
        'goals_scored': 'Goals',
        'assists': 'Assists',
        'clean_sheets': 'Clean Sheets',
        'total_points': 'Points',
        'points_per_game': 'Points per Game',
        'selected_by_percent': 'Ownership',
        'form': 'Form'
    }, inplace=True)

    # Data Transformations
    player_dataframe['Price (£mil.)'] = player_dataframe['Price (£mil.)'] / 10
    player_dataframe['Team'] = player_dataframe['Team'].map({team.get('id'): team.get('name') for team in epl_teams})
    player_dataframe['Position'] = player_dataframe['Position'].map(
        {
            element_type.get('id'): element_type.get('singular_name_short')
            for element_type in element_types
        }
    )
    player_dataframe['Ownership'] = player_dataframe['Ownership'].astype(float)
    player_dataframe['Form'] = player_dataframe['Form'].fillna(0).astype(float)
    player_dataframe['Form'] = player_dataframe['Form'].astype(float)
    player_dataframe['Points per Game'] = player_dataframe['Points per Game'].astype(float)

    return player_dataframe


def create_player_dataframe(
        players: Sequence[Dict[str, Any]],
        epl_teams: Sequence[Dict[str, Any]],
        element_types: Sequence[Dict[str, Any]]) -> pd.DataFrame:
    """
    Convert raw player data into a pandas DataFrame with relevant features
    :param players: Array containing data for all the players
    :param epl_teams: Array of all current EPL teams
    :param element_types: Dictionary mapping element type ids to short forms like GK for goalkeeper, DEF for defender e.t.c.
    :return: DataFrame with player data
    """
    # Create the new data frame from the elements dict in the fpl_data
    df = clean_player_data(create_dataframe(players), epl_teams, element_types)
    return df