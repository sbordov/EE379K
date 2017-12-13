#!/bin/bash

scp -i ~/.ssh/kevin_instance_key.pem.txt ubuntu@ec2-35-165-150-255.us-west-2.compute.amazonaws.com:~/ee379k/tensorflow-wavenet/loss_values.txt ~/Documents/Fall_2017/EE379K/FinalProject/loss_plots/loss_values_bossa.txt

scp -i ~/.ssh/kevin_instance_key.pem.txt ubuntu@ec2-34-216-197-128.us-west-2.compute.amazonaws.com:~/ee379k/tensorflow-wavenet/loss_values.txt ~/Documents/Fall_2017/EE379K/FinalProject/loss_plots/loss_values_piano.txt

cd /Users/Stefan/Documents/Fall_2017/EE379K/FinalProject/loss_plots

python plot_loss.py piano
python plot_loss.py bossa
