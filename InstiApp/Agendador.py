import schedule
import time

def tarefa():
    print('Please Subscribe on this Chanell!!')

#schedule.every().second.do(tarefa)
schedule.every().day.at("03:36").do(tarefa)

while True:
    schedule.run_pending()
    time.sleep(3)