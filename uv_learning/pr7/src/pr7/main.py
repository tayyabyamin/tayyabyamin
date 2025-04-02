#pip install onnxruntime==1.15.0
from crewai.flow.flow import flow, start, listen
import time

class simpleflow(flow):

    @start()
    def function1(self):
        print("step1..")
        time.sleep(3)

    @listen(function1)
    def function2(self):
        print("step2..")

    @listen(function2)
    def function3(self):
        print("step3..")


def kickoff():
    print("hello world")
    obj = simpleflow()  # Fixed typo here
    obj.kickoff()