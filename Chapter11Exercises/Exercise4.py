def worker_punches():
    worker_dict={}
    worker_times_dict={"clock_in":None,"clock_out":None,"hours_worked":None}
  
    while True:
      worker_name=input("Who is the worker? ")
      worker_dict[worker_name]=worker_times_dict.copy()
      worker_dict[worker_name]["clock_in"]=input("What time did the worker clock in? ")
      worker_dict[worker_name]["clock_out"]=input("What time did the worker clock out? ")
      worker_dict[worker_name]["hours_worked"]=((int(worker_dict[worker_name]["clock_out"])-int(worker_dict[worker_name]["clock_in"])))
      if input("Are you done (input 'y' to indicate stop or any key to continue)? ") == "y":
        return worker_dict

print(worker_punches())
  