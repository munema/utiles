# Utils.py
Helper function on python3.x

## change_suffix(file_name, to_suffix = '.png')
change and rewrite suffix (file extention)

```
# 'dataset/img1.jpeg' → 'dataset/img1.png'
change and rewrite suffix ('dataset/img1.jpeg','.png')
```

## crop_base_mask_img(original_img_path, mask_image_path)
crop original image based on mask image

```
img = crop_base_mask_img('dataset/img1.png', 'dataset/img1_mask.png')
```

## change_color_img(img_path, color, min_sv = 0.5)
change color

```
# RGB → HSV → change color operation (base on color angle(H) and param min_sv (SV)) → RGB
img_red = change_color_img('dataset/img1.png', color='red', min_sv = 0.5)
```