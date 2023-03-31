class AbckeyRequests:
    def isPass(self,key:str):
        pass
class keyTs(AbckeyRequests):

    def isPass(self,key):
        print(key)
        return True
cs=keyTs()

isPass=cs.isPass