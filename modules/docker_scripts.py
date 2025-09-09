import docker
import docker.errors


def check_docker_version():
    try:
        client = docker.from_env()
        version = client.version()
        print(f"Docker service is running. Version: {version['Version']}")
        return version["Version"]
    except docker.errors.APIError as e:
        print(f"Error: Ошибка Docker API: {e}")
        return None
    except docker.errors.DockerException as e:
        print(f"Error: Общая ошибка Docker: {e}")
        return None
