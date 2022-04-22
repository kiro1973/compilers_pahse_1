import re

class Dfa :
    def __init__(self):
        print("class DFA")


    def start(self,c):

        if (c == ' '):
            dfa = 0
        elif (c == '('):
            print("start state")
            dfa = 1

        # -1 is used to check for any
        # invalid symbol
        else:
        # print("oh yeaah")
            dfa = -1
        return dfa


    # This function is for the first
    # dfa = state of DFA
    def state1(self,c):
        print("state 1")
        x = re.findall(r"[\w]+", c)
        y=re.findall(r'([0-9][A-Za-z]+[0-9]*)',c)

        if (len(y) > 0):
           if (c == y[0]):
              dfa = -1
        elif(c=='!'):
            dfa=10
        elif (len(x)>0):
            if (c == ' '):
                dfa = 1
            elif (c == x[0]):
                dfa = 2

            else:
                dfa = -1

        else:
            dfa = -1

        return dfa


    # This function is for the second
    # dfa = state of DFA
    def state2(self,c):
        print("state 2")
        if (c == ' '):
            dfa = 2
        elif (c == ')'):
            dfa = 5
        elif (c == '='or c=='<'or c=='>'or c== '=>'or c=='<='or c=='&&'or c == '||'):
            dfa = 3
        else:
            dfa = -1
        return dfa


    # This function is for the third
    # dfa = state of DFA
    def state3(self,c):
        print("state 3")
        x = re.findall(r"[\w]+", c)
        y = re.findall(r'([0-9][A-Za-z]+[0-9]*)', c)

        if (len(y) > 0):
            if (c == y[0]):
                dfa = -1
        elif (c == '!'):
            dfa = 11
        elif len(x)>0:
            if (c == ' '):
                dfa = 3
            elif (c == x[0]):
            #    print("yoh bro")
                dfa = 4
            else:
                dfa = -1
        else:
            dfa = -1
        return dfa


    # This function is for the fourth
    # dfa = state of DFA
    def state4(self,c):
        print("state 4")
        #print(c)
        if (c== ' '):
            dfa = 4
        elif (c == '='or c == '<'or c == '>'or c == '=>'or c == '<='or c=='&&'or c=='||')  :
            dfa = 3
        elif (c == '!') :
            dfa = 1
        elif (c ==')')  :
            print("acceptance state")
            dfa=5
        else:
            dfa = -1
        return dfa


    def state5(self,c):

        if(c==' 'or c==''):
            dfa=5

        else:
            dfa= -1
        return dfa

    def error(self,c):
        print("error state")
        return -2




    def isAccepted(self,String):
        # store length of Stringing
        l = len(String)

        # dfa tells the number associated
        # with the present dfa = state
        dfa = 0
        for i in range(l):
            if (dfa == 0):
                dfa = self.start(String[i])

            elif (dfa == 1):
                dfa = self.state1(String[i])

            elif (dfa == 2):
                dfa = self.state2(String[i])

            elif (dfa == 3):
                dfa = self.state3(String[i])

            elif (dfa == 4):
                dfa = self.state4(String[i])

            elif (dfa == 5):
                dfa = self.state5(String[i])
            elif (dfa == -1):
                dfa = self.error(String[i])
            else:
                return 0
        if (dfa == 5):
            return 1
        else:
            return 0
    #############################################################################################################################################
    def Tokens (self,routes):


        types = []
        for i in range(len(routes)):
            error = re.findall (r'([0-9][A-Za-z]+[0-9]*)',routes[i])
            if (len(error) > 0):
                if (routes[i] == error[0]):
                    types.append("Illegal Type")

            y = re.findall(r'[A-Za-z][\w]*', routes[i])
            num = re.findall(r"[\d]+", routes[i])
            if (len(y) > 0):
                if (routes[i] == y[0]):
                    types.append("ID")
            elif (len(num) > 0):
                if (routes[i] == num[0]):
                    types.append("NUM")
            elif (routes[i] == '=' or routes[i] == '<=' or routes[i] == '=>' or routes[i] == '<' or routes[i] == '>' or
                routes[i] == '(' or routes[i] == ')'):
                types.append("Operators")
            elif (routes[i] == '&&' or routes[i] == '||' or routes[i] == '!'):
                types.append("Reserved words")

        print(types)
        print(routes)

        Token = []


        ##########################################3

        l = len(routes)

        # dfa tells the number associated
        # with the present dfa = state
        if(routes[0]=="("):
            dfa = 0
        else:
            dfa=-1

        for i in range(l):
            if (dfa == 0):
                dfa = self.start(routes[i])
                if(dfa==1):
                    Token.append(("'"+str(routes[i])+"',", "'"+str(types[i])+"',","2nd State"))
                elif (dfa == -1):
                    Token.append(("'"+str(routes[i])+"',", "'"+str(types[i])+"',", "error state"))
            elif(dfa==10):
                dfa=self.state1(routes[i])
                if (dfa == 2):
                    Token.append(("'" + str(routes[i]) + "',", "'" + str(types[i]) + "',", "4th State"))

            elif (dfa == 1):
                dfa = self.state1(routes[i])
                if(dfa==2):
                    Token.append(("'"+str(routes[i])+"',", "'"+str(types[i])+"',","4th State"))
                if(dfa==10):
                    Token.append(("'"+str(routes[i])+"',", "'"+str(types[i])+"',","3rd State"))
                elif (dfa == -1):
                    Token.append(("'"+str(routes[i])+"',", "'"+str(types[i])+"',", "error state"))

            elif (dfa == 2):
                dfa = self.state2(routes[i])
                if (dfa==5):
                    Token.append(("'" + str(routes[i]) + "',", "'" + str(types[i]) + "',", "acceptance state"))
                elif(dfa==3):
                    Token.append(("'"+str(routes[i])+"',", "'"+str(types[i])+"',", "5th State"))
                elif (dfa == -1):
                    Token.append(("'"+str(routes[i])+"',","'"+ str(types[i])+"',", "error state"))


            elif (dfa == 11):
                dfa = self.state3(routes[i])
                if (dfa == 4):
                    Token.append(("'" + str(routes[i]) + "',", "'" + str(types[i]) + "',", "7th State"))

            elif (dfa == 3):
                dfa = self.state3(routes[i])
                if(dfa==4):
                    Token.append(("'"+str(routes[i])+"',","'"+ str(types[i])+"',", "7th State"))
                elif(dfa==11):
                    Token.append(("'" + str(routes[i]) + "',", "'" + str(types[i]) + "',", "6th State"))
                elif (dfa == -1):
                    Token.append(("'"+str(routes[i])+"',", "'"+str(types[i])+"',", "error state"))

            elif (dfa == 4):
                dfa = self.state4(routes[i])
                if (dfa==5):
                    Token.append(("'"+str(routes[i])+"',","'"+ str(types[i])+"',", "accpetance State"))
                elif(dfa==1):
                    Token.append(("'"+str(routes[i])+"',", "'"+str(types[i])+"',", "2nd State"))
                elif (dfa == 3):
                    Token.append(("'"+str(routes[i])+"',","'"+ str(types[i])+"',", "5th State"))
                elif (dfa == -1):
                    Token.append(("'"+str(routes[i])+"',", str(types[i])+"',", "error state"))
            elif (dfa == 5):
                dfa = self.state5(routes[i])

            elif (dfa == -1):
                dfa = self.error(routes[i])
                Token.append(("'"+str(routes[i])+"'","',"+ str(types[i])+"',", "error state"))
            else: break

        ###########################################
        if (dfa==5):
            print("ACCEPTED")
        else:
            print("REJECTED")

        return Token
######################################################################################################################################
# Driver code

if __name__ == "__main__":
    String = input("enter the desired logical expression")
    x = re.findall(r"([(]|[)]|<=|=>|&&|[|]{2}|[<>=!]|[\w]+)", String)
    print(x)

    routes = []
    dfa = Dfa()
    for i in range(len(x)):
        routes.append(x[i])
    Token=dfa.Tokens(routes)
    print(Token)
