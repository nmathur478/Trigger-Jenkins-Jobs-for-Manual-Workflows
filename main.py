# import os
# if __name__ == "__main__":
#     # Retrieve Jenkins secrets from environment variables
#     jenkins_url = os.environ.get("JENKINS_URL")
#     print(jenkins_url)
#     # print(f"""TEST1: {os.environ.get("TEST1")}""")
#     # print(f"""TEST: {os.environ.get("TEST")}""")

import os
hostname = "jenkins.calance.work" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print(f"{hostname} is up!")
else:
  print(f"{hostname} is down!")
