# Optimal transportation paper #
An implementation of [Optimal Textures: Fast and Robust Texture Synthesis and Style Transfer through Optimal Transport](https://arxiv.org/abs/2010.14702) for TU Delft CS4240.

![Simplified diagram of the algorithm](algo.jpg)

You can find a more in-depth summary of the implementation [in this blog post](https://wavefunk.xyz/optex).

## Installation
```bash
git clone https://github.com/JCBrouwer/OptimalTextures
cd OptimalTextures
pip install -r requirements.txt
python optex.py -h
```

## Texture synthesis

Generate a texture based on an example:
```bash
python3 optex.py --style images/flower_beds/images/flower_beds/FlowerBeds0008_350.jpg --size 512
```

## Test we run 
python3 optex.py --style images/flower_beds/images/flower_beds/FlowerBeds0008_350.jpg --passes [from 1 to 5]

python3 optex.py --style images/flower_beds/images/flower_beds/FlowerBeds0008_350.jpg --iters [100 - 250 - 500 - 750 - 1000]

python3 optex.py --style images/flower_beds/images/flower_beds/FlowerBeds0008_350.jpg --hist_mode ["sym", "pca", "chol", "cdf"]