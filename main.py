import os
if __name__ == "__main__":
    # Retrieve Jenkins secrets from environment variables
    # jenkins_url = os.getenv("JENKINS_URL")
    # print(jenkins_url)
    print(f"""TEST1: {os.environ.get("TEST1")}""")
    print(f"""TEST: {os.environ.get("TEST")}""")
