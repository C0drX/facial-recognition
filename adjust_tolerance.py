def adjust_tolerance_based_on_quality(blurriness_score, base_tolerance=0.475):
    """
    Adjust the tolerance for face matching based on image quality (blurriness score).

    Parameters:
    blurriness_score (float): Blurriness score of the image.
    base_tolerance (float): Base tolerance value. Adjustments are made relative to this.

    Returns:
    float: Adjusted tolerance for face matching.
    """
    # Define thresholds for blurriness
    # if blurriness_score < 50:  # Very blurry, increase tolerance (less strict)
    #     return base_tolerance + 0.08
    # if blurriness_score < 60:
    #     return base_tolerance + 0.10
    # if blurriness_score < 70:
    #     return base_tolerance + 0.075
    # if blurriness_score < 80:
    #     return base_tolerance + 0.050
    # if blurriness_score < 90:
    #     return base_tolerance + 0.025
    # elif blurriness_score < 100:
    #     return base_tolerance + 0.0125  # Moderately blurry, slight increase in tolerance
    # else:
    #     return base_tolerance  # High quality, use base tolerance

# -------------------------Adjusted By ChatGPT------------------------- #

    # if blurriness_score < 50:  # Very blurry, increase tolerance (less strict)
    #     return base_tolerance + 0.03
    # if blurriness_score < 60:
    #     return base_tolerance + 0.015
    # if blurriness_score < 70:
    #     return base_tolerance + 0.0075
    # if blurriness_score < 80:
    #     return base_tolerance + 0.00325
    # if blurriness_score < 90:
    #     return base_tolerance + 0.00175
    # elif blurriness_score < 100:
    #     return base_tolerance + 0.000875  # Moderately blurry, Slightly increase tolerance
    # else:
    #     return base_tolerance


#############################################################################

    # if blurriness_score < 50:  # Very blurry, increase tolerance (less strict)
    #     return base_tolerance + 0.055
    # if blurriness_score < 60:
    #     return base_tolerance + 0.075
    # if blurriness_score < 70:
    #     return base_tolerance + 0.05
    # if blurriness_score < 80:
    #     return base_tolerance + 0.025
    # if blurriness_score < 90:
    #     return base_tolerance  # No adjustment
    # elif blurriness_score < 100:
    #     return base_tolerance - 0.0125  # Slightly reduce tolerance
    # else:
    #     return base_tolerance


################################################################

    # if blurriness_score < 50:  # Very blurry, tolerance is reduced
    #     return base_tolerance - 0.17
    # if blurriness_score < 60:
    #     return base_tolerance - 0.15
    # if blurriness_score < 70:
    #     return base_tolerance - 0.175
    # if blurriness_score < 80:
    #     return base_tolerance - 0.20
    # if blurriness_score < 90:
    #     return base_tolerance - 0.225
    # elif blurriness_score < 100:
    #     return base_tolerance - 0.2375  # Slightly blurry, tolerance is slightly reduced
    # else:
    #     return base_tolerance

# * <--------------------------MOST ACCURATE TILL NOW --------------------------->

    # if blurriness_score < 50:  # Very blurry, maximum tolerance
    #     return base_tolerance + 0.025
    # if blurriness_score < 60:
    #     return base_tolerance + 0.0125
    # if blurriness_score < 70:
    #     return base_tolerance  # No change, base_tolerance
    # if blurriness_score < 80:
    #     return base_tolerance - 0.0125
    # if blurriness_score < 90:
    #     return base_tolerance - 0.025
    # elif blurriness_score < 100:
    #     return base_tolerance - 0.025  # Minimum tolerance
    # else:
    #     return base_tolerance - 0.025  # Minimum tolerance


# * <------------------------ Testing For Low quality images ----------------->

    # * <---------------PRETTY MUCH ACCURATE --------------------------->

    if blurriness_score < 50:  # Very blurry, maximum tolerance
        return base_tolerance + 0.075
    if blurriness_score < 60:
        return base_tolerance + 0.0625
    if blurriness_score < 70:
        return base_tolerance + 0.05
    if blurriness_score < 80:
        return base_tolerance + 0.0375
    if blurriness_score < 90:
        return base_tolerance + 0.025
    if blurriness_score < 100:
        return base_tolerance + 0.0125
    else:
        return base_tolerance  # No change, base tolerance remains 0.475

# ____________________________________________________

    # if blurriness_score < 50:  # Very blurry, maximum tolerance
    #     return base_tolerance + 0.1
    # if blurriness_score < 60:
    #     return base_tolerance + 0.075
    # if blurriness_score < 70:
    #     return base_tolerance + 0.05
    # if blurriness_score < 80:
    #     return base_tolerance + 0.025
    # if blurriness_score < 90:
    #     return base_tolerance  # No adjustment
    # if blurriness_score < 100:
    #     return base_tolerance - 0.0125
    # else:
    #     return base_tolerance - 0.025  # Minimum tolerance
