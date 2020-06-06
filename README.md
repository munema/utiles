# Utils.py
Helper function on python3.x

## change_suffix
- change and rewrite suffix (file extention)

### Argument
- file_name
- to_suffix = '.png'

### Usage
```
# 'dataset/img1.jpeg' → 'dataset/img1.png'
change and rewrite suffix ('dataset/img1.jpeg','.png')
```

## crop_base_mask_img
- crop original image based on mask image

### Argument
- original_img_path : original image
- mask_image_path : masking image (black cover on original image)

### Usage
```
img = crop_base_mask_img('dataset/img1.png', 'dataset/img1_mask.png')
```

## change_color_img
- change image color 
- RGB → HSV → change color operation (base on color angle(H) and param min_sv (SV)) → RGB

### Argument
- img_path
- color : You can choose'red', 'blue', 'yellow', or 'green'.
- min_sv : threshold about S and V (if param (S or V) is below threshold (min_sv*255), translating to threshold)

### Usage
```
# change red image
img_red = change_color_img('dataset/img1.png', color='red', min_sv = 0.5)
```
