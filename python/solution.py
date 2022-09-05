#!/usr/bin/env python3

from typing import (
    List,
    Tuple,
    Union
)

from utils.image import (
    ImageType,
    PackedImage,
    StrideImage,
)

from utils.function_tracer import FunctionTracer
from utils.eye_pattern import EYE_PATTERNS, EYE_PATTERNS_SIZE


def compute_solution(images: List[Union[PackedImage, StrideImage]]):
    ft = FunctionTracer("compute_solution", "seconds")
    for image in images:
        i = 0

        # iterate through all pixels in the image
        while i <= image.resolution.height - EYE_PATTERNS_SIZE:
            j = 0
            while j <= image.resolution.width - EYE_PATTERNS_SIZE:
                if image.get_xy_pixel((i, j)).red >= 200:

                    # check for all patterns; EYE_PATTERN_3 is composed of patterns 1 and 2, hence check for it first
                    for index, (pattern, num_non_zeros) in enumerate(EYE_PATTERNS):

                        # iterate through all pixels of the template and store coords of pixels to change
                        pixel_coords_to_change = []
                        for m in range(EYE_PATTERNS_SIZE):
                            for n in range(EYE_PATTERNS_SIZE):
                                if image.get_xy_pixel((i + m, j + n)).red * (not pattern[m][n].isspace()) >= 200:
                                    pixel_coords_to_change.append((i + m, j + n))

                        # if there is a full match -> change the stored pixels
                        if len(pixel_coords_to_change) == num_non_zeros:
                            for coords in pixel_coords_to_change:
                                image.set_xy_pixel(coords)

                            # after a match, skip the next pattern width and checking for other patterns
                            j += EYE_PATTERNS_SIZE
                            break
                j += 1
            i += 1

    del ft
            