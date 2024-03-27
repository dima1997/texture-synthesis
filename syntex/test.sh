CUDA_VISIBLE_DEVICES=0 python po/improved_model.py \
    --vgg19-npy-path vgg19_normalised.npz \
    --data-folder data \
    --test-only \
    --test-folder test_log \
    --test-ckpt train_log/impr/model-50000.data-00000-of-00001
