from consts.helpers import opposite, CognitiveFunction

# NOTE: I bashed my head against this conversion for so fucking long I cant even understand why it works any more.
# I'm glad that it does though.

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
    if attention_type == "E":
        if worldview_type == "J":
            cognitive_fn_dict["dominant"].type = decision_type
            cognitive_fn_dict["auxiliary"].type = information_type
            cognitive_fn_dict["tertiary"].type = opposite[information_type]
            cognitive_fn_dict["inferior"].type = opposite[decision_type]
        if worldview_type == "P":
            cognitive_fn_dict["dominant"].type = information_type
            cognitive_fn_dict["auxiliary"].type = decision_type
            cognitive_fn_dict["tertiary"].type = opposite[decision_type]
            cognitive_fn_dict["inferior"].type = opposite[information_type]

    if attention_type == "I":
        if worldview_type == "J":
            cognitive_fn_dict["dominant"].type = information_type
            cognitive_fn_dict["auxiliary"].type = decision_type
            cognitive_fn_dict["tertiary"].type = opposite[decision_type]
            cognitive_fn_dict["inferior"].type = opposite[information_type]

        if worldview_type == "P":
            cognitive_fn_dict["dominant"].type = decision_type
            cognitive_fn_dict["auxiliary"].type = information_type
            cognitive_fn_dict["tertiary"].type = opposite[information_type]
            cognitive_fn_dict["inferior"].type = opposite[decision_type]

    return [str(fn) for fn in cognitive_fn_dict.values()]

