# Free High Quality Background Remover

This program allows to remove background from high quality image by using low quality alpha channel mask.

## How to use

- Clone repository `git clone https://github.com/jurajhonsch/Background-Remover.git`
- Install requirements (opencv, argparse)`python3 -m pip install -r requirements`
- Download low quality preview from online background remover (https://remove.bg, https://removal.ai).
- Run `python3 --original my_high_quality_original_image.jpg --preview my_low_quality_preview.png --result my_high_quality_result.png`

## Examples

Watermelon high quality original image
![Watermelon high quality original image](./watermelon.jpg?raw=true "Watermelon")

Watermelon low quality preview image
![Watermelon low quality preview image](./watermelon-removebg-preview.png?raw=true "Watermelon")

Watermelon high quality result image
![Watermelon high quality result image](./watermelon-result.png?raw=true "Watermelon")

## License

This program is released under MIT License.
