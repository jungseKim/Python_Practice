def _merge(str,str2):
    return str+' '+str2

def hello(name="function"):
    return 'heell'+name

class User:
    def hello(self,name="class function"):
        return 'hello'+name

defaultUser=User()
defaultName='defUser'
_value=0

if __name__ == '__main__':
    print(hello('a'))