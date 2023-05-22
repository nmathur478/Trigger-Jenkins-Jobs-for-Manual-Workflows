import os

# print(f"""TEST1: {os.getenv("TEST1")}""")
print(f"""TEST1: {os.environ.get("TEST1")}""")
print(f"""TEST: {os.environ.get("TEST")}""")
