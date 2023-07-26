#!/bin/bash
sinfo -o "%20N  %10c  %25f  %10G "
echo "  "
# sinfo -p large -o="%P %.5a %.10l %.6D %.6t"
sinfo -p large
echo " " 
echo "Cores: Allocated, Idle, Other and Total"
sinfo -o%C
echo " " 
squeue -u dkundu --states=RUNNING --format="%.18i %.9P %.15j %.8u %.8T %.10M %.15l %.6D %.50R" 
squeue -u dkundu --states=RUNNING -h | wc -l
echo " "
squeue -u dkundu --start --format="%.18i %.9P %.15j %.8u %.8T %.20S %.6D %.50R"
echo " "
# sprio -p large -l 
echo " " 
echo "Pending jobs: short, medium, large, xlarge"
squeue -p short -h -r -t pending | wc -l; squeue -p medium -h -r -t pending | wc -l ; squeue -p large -h -r -t pending  | wc -l ; squeue -p xlarge -h -r -t pending  | wc -l



