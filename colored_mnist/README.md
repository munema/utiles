# mak_colored_mnist.py
## Requirments
- Numpy
- Tensorflow
- PIL
- tqdm

## Argument
- --output_path (str) : Name for dataset path (Default : '.')
- --output_label (str) : 'number' or 'color' (Default : 'number')
    - If you choose 'number', output folder (label) is 0, 1, 2, ...
    = If you choose 'color', output folder (label) is red, bule, green, yellow

## Usage
```
python make_colored_minist.py --output_path='.' --output_label='nubmer'
```

## Output Examples
