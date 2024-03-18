# for i in 0 1 2 3 4 5 6 7
# do
#     python rtdetr_pytorch/benchmark.py --model_idx $i --resolution 640
# done

for i in 0 1 2 3 4 5 6 7
do
    python rtdetr_pytorch/benchmark.py --model_idx $i --resolution 1280 --n 200
done
