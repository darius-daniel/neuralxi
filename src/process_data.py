import pandas as pd
from typing import Dict, Any
import logging


def create_player_dataframe(fpl_data: Dict[str, Any]) -> pd.DataFrame:
    """
    Convert raw player data into a pandas DataFrame with relevant features
    :param fpl_data: Dictionary containing FPL data
    :return: DataFrame with player data
    """
    if not fpl_data:
        logging.error("Invalid FPL data format")
        return pd.DataFrame()
    
    # Create the new data frame from the elements dict in the fpl_data
    df = pd.DataFrame(fpl_data['elements'])

    # Select the relevant columns
    relevant_cols = [
        'web_name', 'team', 'element_type',
        'minutes', 'goals_scored', 'assists',
        'clean_sheets', 'total_points', 'now_cost',
        'points_per_game', 'selected_by_percent', 'form'
    ]
    df = df[relevant_cols]

    # Rename the columns for readability and consistency
    df.rename(columns={
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
    df['Price (£mil.)'] = df['Price (£mil.)'] / 10
    df['Team'] = df['Team'].map({team.get('id'): team.get('name') for team in fpl_data['teams']})
    df['Position'] = df['Position'].map(
        {
            element_type.get('id'): element_type.get('singular_name_short')
            for element_type in fpl_data['element_types']
        }
    )
    df['Ownership'] = df['Ownership'].astype(float)
    df['Form'] = df['Form'].fillna(0).astype(float)
    df['Form'] = df['Form'].astype(float)
    df['Points per Game'] = df['Points per Game'].astype(float)

    return df