#!/bin/sh

GPU=${GPU:--1}

python3 -u gan_train.py \
 -b 128 --log-interval 100 -g ${GPU} --test data/prep-title.txt \
  data/prep-title.txt data/vocab.txt --valid-interval 50 --epoch 400