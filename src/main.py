import argparse
from modules import docker_scripts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", help="Function to run")
    parser.add_argument("args", nargs="*", help="Arguments for the functions")
    args = parser.parse_args()

    if args.function == "version":
        docker_scripts.check_docker_version(*args.args)
    else:
        print("Unknown function")


if __name__ == "__main__":
    main()
