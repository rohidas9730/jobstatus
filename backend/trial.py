import time
import subprocess
from datetime import date
from datetime import datetime

datetime_obj = datetime.now()
date_obj = datetime_obj.date()
dt = datetime.today()
print(type(dt))
print(date_obj)
print(type(datetime_obj))
print(type(date_obj))
# start = time.time()
# human_readable_st = time.ctime(start)
# print("Human-readable time:", human_readable_st)
# print(human_readable_st[11:19])



# result = subprocess.run(["python", "Folder/tes3s.py"], capture_output=True, text=True)

# # Capture and print the output
# print("Output from script1:", result.stdout.strip())
# print("Return code:", result.returncode)



# end = time.time()
# human_readable_en = time.ctime(end)
# print(human_readable_en[11:19])
# print("Human-readable time:", human_readable_en)

# print(f"Elapsed time: {end - start:.2f} seconds")
# dur = round(end-start, 2)


# value = {
#     "start": human_readable_st,
#     "end": human_readable_en,
#     "dur": dur
    
# }

# print(value)

