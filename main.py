import subprocess


def start_user_server():
    subprocess.run(["python", "core/grpc_server.py"])


def start_client():
    subprocess.run(["poetry", "run", "uvicorn", "core.client:app", "--reload"])


def main():
    start_user_server()


if __name__ == "__main__":
    main()
