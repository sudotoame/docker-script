import unittest

from unittest.mock import patch, MagicMock

from modules import docker_scripts


class TestCheckDockerVersion(unittest.TestCase):
    @patch("docker.from_env")
    def test_check_docker_version_success(self, mock_docker_client):
        mock_client_instance = MagicMock()
        mock_client_instance.version.return_value = {"Version": "20.10.12"}
        mock_docker_client.return_value = mock_client_instance

        version = docker_scripts.check_docker_version()
        self.assertEqual(version, "20.10.12")

    @patch("docker.from_env")
    def test_check_docker_version_failure(self, mock_docker_client):
        mock_client_instance = MagicMock()
        mock_client_instance.version.side_effect = Exception("Docker not available")
        mock_docker_client.return_value = mock_client_instance

        with self.assertRaises(Exception):
            docker_scripts.check_docker_version()


# if __name__ == "__main__":
# unittest.main()
