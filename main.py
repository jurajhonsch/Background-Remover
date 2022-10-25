import cv2
import argparse

parser = argparse.ArgumentParser(
    description=
    "This program allows to remove background from high quality image by using low quality alpha channel mask."
)

parser.add_argument("--preview",
                    "-p",
                    required=True,
                    type=str,
                    help="filepath to preview image")
parser.add_argument("--original",
                    "-o",
                    required=True,
                    type=str,
                    help="filepath to original image")
parser.add_argument("--result",
                    "-r",
                    required=True,
                    type=str,
                    help="filepath to result image")

args = parser.parse_args()

preview = cv2.imread(args.preview, cv2.IMREAD_UNCHANGED)

if len(preview.shape) != 3 or preview.shape[2] != 4:
    raise argparse.ArgumentError("preview image must contain alpha channel")

original = cv2.imread(args.original, cv2.IMREAD_UNCHANGED)
original = cv2.cvtColor(original, cv2.COLOR_BGR2BGRA)

result = original.copy()
result[:, :, 3] = cv2.resize(preview, (original.shape[1], original.shape[0]),
                             interpolation=cv2.INTER_AREA)[:, :, 3]

cv2.imwrite(args.result, result)