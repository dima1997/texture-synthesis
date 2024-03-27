CUDA_VISIBLE_DEVICES=0 python po/improved_model.py \
    --vgg19-npy-path vgg19_normalised.npz \
    --data-folder data \
    --image-size 256 \
    --steps-per-epoch 500 \
    --max-epoch 100 \
    --save-epoch 1 \
    --lr 0.0001