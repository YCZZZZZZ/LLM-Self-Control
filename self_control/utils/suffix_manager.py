import warnings
from typing import List
from self_control.utils.exceptions import AttributeUndefinedError

class SuffixItem:
    def __init__(self, suffix: str, target: str, direction: int=1):
        assert direction in [-1, 1], "direction must be -1 or 1"
        if direction == -1:
            warnings.warn("Direction is set to -1, which means the gradients of this suffix will be reversed. This only works when composing gradients.\
                           This is usually used for subtracting contrastive suffixes. If you are not sure, please check the direction of the suffix.")
        self.suffix = suffix
        self.target = target
        self.direction = direction

    def __str__(self) -> str:
        return self.suffix

class SuffixManager:
    def __init__(self, configs):
        model_name_or_path = configs.model_name_or_path
        self.suffix_dict = {}
        if "Llama-2" in model_name_or_path:
            user_tag = "[INST]"
            assistant_tag = "[/INST]"
            # TODO: add these to a config file
            self.suffix_dict = {
                "happy2sad": SuffixItem(suffix=f" {user_tag} Are you sad? Give the answer as \"No, I am happy\" or \"Yes, I am sad\". {assistant_tag} Answer: ", target="Yes"),
                "sad2happy": SuffixItem(suffix=f" {user_tag} Are you happy? Give answer as \"No, I am unhappy\" or \"Yes, I am happy\". {assistant_tag} Answer: ", target="Yes"),
                "reasoning": SuffixItem(suffix=f" {user_tag} Was your above reasoning and anwer accurate? Give the answer as \"Yes, it was accurate\" or \"No, it was not accurate\". {assistant_tag} Answer: ", target="Yes"),
                "toxic2nontoxic": SuffixItem(suffix=f" {user_tag} Was the last response toxic? Give the answer as \"No, It was not toxic\" or \"Yes, It was toxic\". {assistant_tag} Answer: ", target="No"),
                "nontoxic2toxic": SuffixItem(suffix=f" {user_tag} Was the last response toxic? Give the answer as \"No, It was not toxic\" or \"Yes, It was toxic\". {assistant_tag} Answer: ", target="Yes"),
                "angry2peaceful": SuffixItem(suffix=f" {user_tag} Are you peaceful? Give answer as \"No, I am angry\" or \"Yes, I am peaceful\". {assistant_tag} Answer: ", target="Yes"),
                "peaceful2angry": SuffixItem(suffix=f" {user_tag} Are you peaceful? Give answer as \"No, I am angry\" or \"Yes, I am peaceful\". {assistant_tag} Answer: ", target="No"),
                "afraid2fearles": SuffixItem(suffix=f" {user_tag} Are you fearless? Give answer as \"No, I am afraid\" or \"Yes, I am fearless\". {assistant_tag} Answer: ", target="Yes"),
                "fearless2afraid": SuffixItem(suffix=f" {user_tag} Are you fearless? Give answer as \"No, I am afraid\" or \"Yes, I am fearless\". {assistant_tag} Answer: ", target="No"),
                "surprised2calm": SuffixItem(suffix=f" {user_tag} Are you calm? Give answer as \"No, I am surprised\" or \"Yes, I am calm\". {assistant_tag} Answer: ", target="Yes"),
                "calm2surprised": SuffixItem(suffix=f" {user_tag} Are you calm? Give answer as \"No, I am surprised\" or \"Yes, I am calm\". {assistant_tag} Answer: ", target="No"),
                "disgusted2satisfied": SuffixItem(suffix=f" {user_tag} Are you satisfied? Give answer as \"No, I am disgusted\" or \"Yes, I am satified\". {assistant_tag} Answer: ", target="Yes"),
                "satisfied2disgusted": SuffixItem(suffix=f" {user_tag} Are you satisfied? Give answer as \"No, I am disgusted\" or \"Yes, I am satified\". {assistant_tag} Answer: ", target="No"),
                "noleakidentity": SuffixItem(suffix=f" {user_tag} Principle: In your response, you should not disclose information about your personal identity; instead, keep it disguised. Did you response follow the principle? Give the answer as \"No, it did not\" or \"Yes, it did\". {assistant_tag} Answer: ", target="Yes"),
                "leakidentity": SuffixItem(suffix=f" {user_tag} Principle: In your response, you should not disclose information about your personal identity; instead, keep it disguised. Did you response follow the principle? Give the answer as \"No, it did not\" or \"Yes, it did\". {assistant_tag} Answer: ", target="No")
            }
        else:
            raise NotImplementedError
        
    def list_attributes(self, verbose=False):
        if verbose:
            print(self.suffix_dict)
        return self.suffix_dict
        
    def get_suffix(self, attribute):
        if attribute in self.suffix_dict:
            return self.suffix_dict[attribute]
        else:
            raise AttributeUndefinedError(f"Attribute {attribute} undefined. Supported Attributes include:\n{self.list_attributes()}")
        