from consts.helpers import opposite, CognitiveFunction

# in: mbti letters (list) e.g. ["X", "X", "X", "X"]
# out: cognitive functions (list) e.g. ["XX", "XX", "XX", "XX"]
# use shadow = True to find shadow functions
def convert_mbti_to_cognitive_fns(mbti_letter_list: list[str], calculate_shadow_fns: bool = False) -> list[str]:
    # SETUP ------------------------------------------------------------------
    cognitive_fn_dict = {
        "dominant": CognitiveFunction(),
        "auxiliary": CognitiveFunction(),
        "tertiary": CognitiveFunction(),
        "inferior": CognitiveFunction(),
    }

    # Attention type: I/E
    # Information type: S/N 
    # Decision type: T/F
    # Worldview type: P/J
    attention_type, information_type, decision_type, worldview_type = [ch for ch in mbti_letter_list]


    # SET ATTITUDES -----------------------------------------------------------
    slot_names = ["dominant", "auxiliary", "tertiary", "inferior"]
    e_attitudes = ["e", "i", "e", "i"]  
    i_attitudes = ["i", "e", "i", "e"] 

    attitudes = e_attitudes if attention_type == "E" else i_attitudes
    if calculate_shadow_fns:
        attitudes = i_attitudes if attention_type == "E" else e_attitudes

    for slot, attitude in zip(slot_names, attitudes):
        cognitive_fn_dict[slot].attitude = attitude

    # SET FUNCTION LETTERS -----------------------------------------------------------
    # Attention type: I/E
    # Information type: S/N 
    # Decision type: T/F
    # Worldview type: P/J
    dominant_is_judging = (attention_type == "E") == (worldview_type == "J")

    if dominant_is_judging:
        dominant_letter = decision_type
        auxiliary_letter = information_type
    else:
        dominant_letter = information_type
        auxiliary_letter = decision_type

    tertiary_letter = opposite[auxiliary_letter]
    inferior_letter = opposite[dominant_letter]

    cognitive_fn_dict["dominant"].type = dominant_letter
    cognitive_fn_dict["auxiliary"].type = auxiliary_letter
    cognitive_fn_dict["tertiary"].type = tertiary_letter
    cognitive_fn_dict["inferior"].type = inferior_letter

    return [str(fn) for fn in cognitive_fn_dict.values()]

