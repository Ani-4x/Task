def fifo_scheduling(processes):
    n = len(processes)
    
    waiting_time = n*[0]
    turn_around_time = n*[0]
    
    waiting_time[0]= 0
    
    for i in range(1,n):
        waiting_time[i] = waiting_time[i-1] + processes[i-1][1]
    
    for i in range(n):
        turn_around_time[i] = waiting_time[i] + processes[i][1]
        
        
    total_waiting_time = sum(waiting_time)
    total_turn_around_time = sum(turn_around_time)
    average_waiting_time = total_waiting_time / n
    average_turn_around_time = total_turn_around_time / n
    
    return(average_waiting_time,average_turn_around_time)
    
if __name__ == "__main__":
    processes = [ (1,24),(2,30)]
        
        
    
    
    
    average_waiting_time, average_turn_around_time = fifo_scheduling(processes)
    
    print("Average Waiting Time:", average_waiting_time)
    print("Average Turnaround Time:", average_turn_around_time)
    
     