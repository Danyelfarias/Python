import os

home=os.path.dirname(__file__)


for pasta in os.walk(home):
    print(pasta)