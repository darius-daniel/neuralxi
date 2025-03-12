"""
Functions to fetch FPL data from API
"""
from typing import Optional, Dict, Any
import logging
import requests

logging.basicConfig(level=logging.INFO, filename="neuralxi.log")


def get_general_fpl_data() -> Optional[Dict[str, Any]]:
    """
    Fetch overall game data including players, teams, positions, events, chips.
    :return: None if the request or JSON decoding fails, a dict with the data if successful.
    """
    logging.info("Fetching general FPL data")
    try:
        res = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/", timeout=15)
        res.raise_for_status()
        data = res.json()
        logging.info(f"Fetched general FPL data: {data}")
        return data
    except requests.exceptions.JSONDecodeError:
        logging.error("Response contains invalid JSON data")
    except requests.exceptions.RequestException as e:
        logging.error(f"Could not fetch data from .../bootstrap-static: {e}")


    return None


def get_player_data(player_id: str) -> Optional[Dict[str, Any]]:
    """
    Detailed stats for an individual player
    :param player_id:
    :return: JSON data if successful, None if the request fails
    """
    logging.info(f"Fetching player data for {player_id}")
    try:
        res = requests.get(f"https://fantasy.premierleague.com/api/{player_id}", timeout=15)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.JSONDecodeError:
        logging.error(f"Response contains invalid JSON data for player {player_id}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Could not fetch data for player {player_id}: {e}")

    return None


def get_fixtures() -> Optional[Dict[str, Any]]:
    """
    Fetch all fixture data (both past and future)
    :return: JSON data if successful, None if the request fails
    """
    logging.info("Fetching fixtures data")
    try:
        res = requests.get("https://fantasy.premierleague.com/api/fixtures/", timeout=15)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.JSONDecodeError:
        logging.error("Response contains invalid JSON data")
    except requests.exceptions.RequestException as e:
        logging.error(f"Could not fetch data from .../fixtures: {e}")

    return None


def get_game_week_data(game_week: int | str) -> Optional[Dict[str, Any]]:
    """
    Fetch data for a specific game week
    :param game_week:
    :return: JSON data if successful, None if the request fails
    """
    logging.info(f"Fetching game week data for {game_week}")
    try:
        res = requests.get(f"https://fantasy.premierleague.com/api/event/{game_week}/live/", timeout=15)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.JSONDecodeError:
        logging.error(f"Response contains invalid JSON data for game week {game_week}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Could not fetch data for game week {game_week}: {e}")

    return None


def get_team_data(team_id: int) -> Optional[Dict[str, Any]]:
    """
    Fetch data for a specific team
    :param team_id:
    :return: JSON data if successful, None if the request fails
    """
    logging.info(f"Fetching team data for {team_id}")
    try:
        res = requests.get(f"https://fantasy.premierleague.com/api/team/{team_id}/", timeout=15)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.JSONDecodeError:
        logging.error(f"Response contains invalid JSON data for team {team_id}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Could not fetch data for team {team_id}: {e}")

    return None
