#!/usr/bin/python

import argparse
import re

from utils.converters import convert_mbti_to_cognitive_fns
from consts.function_descriptions import fn_descriptions, shadow_fn_descriptions

def main(parser):
    # BOILERPLATE ----------------------------------------------------------
    args = parser.parse_args()
    mbti_string = args.mbti.upper()

    # ARGPARSE GUARD CHECKS ------------------------------------------------
    if len(args.mbti) != 4:
        print("4 letters only")
        return

    letters = re.findall(r"^([IE])([SN])([TF])([PJ])$", mbti_string) 

    if len(letters) == 0:
        print("proper letters only")
        return

    letters = list(letters[0])

    if len(letters) != 4:
        print("proper mbti types only")
        return

    # CALCULATE ----------------------------------------------------------
    cognitive_fn_list = convert_mbti_to_cognitive_fns(letters)
    shadow_fn_list = convert_mbti_to_cognitive_fns(letters, calculate_shadow_fns=True)

    # PRESENT ----------------------------------------------------------
    print("-------------------------")
    print("Cognitive Fns are:")
    print("1  2  3  4")
    print(" ".join(cognitive_fn_list))
    print("-------------------------")
    print("Cognitive Function descriptions:")
    for fn in cognitive_fn_list:
        print(fn + ": " + fn_descriptions[fn])
    print("-------------------------")
    print("Shadow Fns are:")
    print("5  6  7  8")
    print(" ".join(shadow_fn_list))
    print("-------------------------")
    print("Shadow Function descriptions:")
    for fn in shadow_fn_list:
        print(fn + ": " + shadow_fn_descriptions[fn])
    print("-------------------------")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mbti", required=True, help="MBTI to calculate cognitive functions from"
    )
    
    # TODO: reverse the logic, fns -> mbti
    # parser.add_argument(
    #     "--fns", required=False, help="Primary + Secondary Functions to list likely mbti matches (e.g. TiFe)"
    # )
    main(parser)

