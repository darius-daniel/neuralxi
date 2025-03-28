import unittest
from unittest.mock import patch, Mock
from src.fetch_data import get_general_fpl_data, get_player_data, get_fixtures, get_game_week_data, get_team_data


class TestFetchData(unittest.TestCase):

    @patch('src.fetch_data.requests.get')
    def test_get_general_fpl_data_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}
        mock_get.return_value = mock_response

        result = get_general_fpl_data()
        self.assertEqual(result, {'key': 'value'})

    @patch('src.fetch_data.requests.get')
    def test_get_general_fpl_data_no_content(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 204
        mock_get.return_value = mock_response

        result = get_general_fpl_data()
        self.assertIsNone(result)

    @patch('src.fetch_data.requests.get')
    def test_get_general_fpl_data_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_general_fpl_data()
        self.assertIsNone(result)

    @patch('src.fetch_data.requests.get')
    def test_get_player_data_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'player': 'data'}
        mock_get.return_value = mock_response

        result = get_player_data('1')
        self.assertEqual(result, {'player': 'data'})

    @patch('src.fetch_data.requests.get')
    def test_get_player_data_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_player_data('1')
        self.assertIsNone(result)

    @patch('src.fetch_data.requests.get')
    def test_get_fixtures_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'fixtures': []}
        mock_get.return_value = mock_response

        result = get_fixtures()
        self.assertEqual(result, {'fixtures': []})

    @patch('src.fetch_data.requests.get')
    def test_get_fixtures_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_fixtures()
        self.assertIsNone(result)

    @patch('src.fetch_data.requests.get')
    def test_get_game_week_data_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}
        mock_get.return_value = mock_response

        result = get_game_week_data(1)
        self.assertEqual(result, {'key': 'value'})

    @patch('src.fetch_data.requests.get')
    def test_get_game_week_data_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_game_week_data(1)
        self.assertIsNone(result)

    @patch('src.fetch_data.requests.get')
    def test_get_team_data_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'team': 'data'}
        mock_get.return_value = mock_response

        result = get_team_data(1)
        self.assertEqual(result, {'team': 'data'})

    @patch('src.fetch_data.requests.get')
    def test_get_team_data_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_team_data(1)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()