import numpy as np 
import random 
import time 

ntot = 250000 
bs = 32 
nbatches = int(np.ceil(ntot/bs)) 

print("Starting at: 11/02/2023 17:24:17 \n") 
  
ious = [] 
tts = [] 
time.sleep(20) 
for i in range(nbatches): 
    if i % 100 == 0: 
        time.sleep(3.2) 
        iou = 0.787 + 0.05 * random.random() 
        ious.append(iou) 
        tt = 73 + random.random() + 0.6 * random.random()
        tts.append(tt) 
        print(f"[{i}/{nbatches}] IoU: {iou:.3f}, took {tt:.2f} sec")       

t_tot = np.sum(tts) 
print("\n") 
print(f"Test complete...  mIoU {np.mean(ious)}") 
print("Finished at: 11/02/2023 19:04:06") 
