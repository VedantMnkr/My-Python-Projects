class QuizBrain:
    def __init__(self, qList, ans = None) -> None:
        self.q_no = 0
        self.qList = qList
        self.size = len(qList)
        self.ans = ans
        self.scoreBoard = 0
        print('''
████████╗██╗  ██╗███████╗                                   
╚══██╔══╝██║  ██║██╔════╝                                   
   ██║   ███████║█████╗                                     
   ██║   ██╔══██║██╔══╝                                     
   ██║   ██║  ██║███████╗                                   
   ╚═╝   ╚═╝  ╚═╝╚══════╝                                   
                                                            
             ██████╗ ██╗   ██╗██╗███████╗                   
            ██╔═══██╗██║   ██║██║╚══███╔╝                   
            ██║   ██║██║   ██║██║  ███╔╝                    
            ██║▄▄ ██║██║   ██║██║ ███╔╝                     
            ╚██████╔╝╚██████╔╝██║███████╗                   
             ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝                   
                                                            
                         ██████╗  █████╗ ███╗   ███╗███████╗
                        ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
                        ██║  ███╗███████║██╔████╔██║█████╗  
                        ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
                        ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
                         ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                            
The answer can only be 'True' or 'False'. Type 'exit' as answer to quit''')


    def que_avialibility(self):
        return self.q_no + 1 < self.size


    def score(self):
            self.scoreBoard += 1
            print(f"Your current score is - < {self.scoreBoard} >")


    def check_ans(self):
        if self.ans == "exit":
            pass
        elif self.ans == self.qList[self.q_no].answer:
            print("Yay! you are correct")
            self.score()
        else:
            print(f"Not Quite. The correct option is  - {self.qList[self.q_no].answer}")
        self.q_no += 1


    def next_que(self):
        self.ans = input(f'\nQ_no.{self.q_no + 1} : {self.qList[self.q_no].text} ? (True / False)')
        