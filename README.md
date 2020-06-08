# Utils.py
Helper function on python3.x

## change_suffix
- change and rewrite suffix (file extention)

### Argument
- file_name (str)
- to_suffix (str) : file extention (Default : '.png')

### Usage
```
# 'dataset/img1.jpeg' → 'dataset/img1.png'
change and rewrite suffix ('dataset/img1.jpeg','.png')
```

## crop_base_mask_img
- crop original image based on mask image

### Argument
- original_img_path (str) : original image path
- mask_image_path (str) : masking image path (black cover on original image)

### Usage
```
img = crop_base_mask_img('dataset/img1.png', 'dataset/img1_mask.png')
```

## change_color_img
- change image color 
- RGB → HSV → change color operation (base on color angle(H) and param min_sv (SV)) → RGB

### Argument
- img_path (str) : image path
- color (str) : You can choose'red', 'blue', 'yellow', or 'green'.
- min_sv (float : [0,1]) : threshold about S and V (if param (S or V) is below threshold (min_sv*255), translating to threshold) (Default : 0.5)
- color_noise (bool) : if color_noise is True, this function add noise H because of color pattern diversity (Default : True)

### Usage
```
# change red image
img_red = change_color_img('dataset/img1.png', color='red', min_sv = 0.5, color_noise = True)
```
