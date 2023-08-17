"""Sampling parameters for text generation."""
from typing import List, Optional, Union

_SAMPLING_EPS = 1e-5


class SamplingParams:

    def __init__(
        self,
        do_sample: bool = False,
        presence_penalty: float = 0.0,
        frequency_penalty: float = 0.0,
        temperature: float = 1.0,
        top_p: float = 1.0,
        top_k: int = -1,  # -1 is for all 
        ignore_eos: bool = False,
        max_new_tokens: int = 16
    ) -> None:
        self.do_sample = do_sample
        self.presence_penalty = presence_penalty
        self.frequency_penalty = frequency_penalty
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        self.ignore_eos = ignore_eos
        self.max_new_tokens = max_new_tokens
        if self.do_sample == False:
            self.temperature = 1.0
            self.top_p = 1.0
            self.top_k = 1
        if self.temperature >= 0.0 and self.temperature < _SAMPLING_EPS: # temperature is too slow, change to greedy search
            self.temperature = 1.0
            self.top_k = 1
        return
    
    def verify(self):
        if self.presence_penalty < 0.0:
            raise ValueError(f"presence_penalty must >= 0.0, got {self.presence_penalty}")
        if self.frequency_penalty < 0.0:
            raise ValueError(f"frequency_penalty must >= 0.0, got {self.frequency_penalty}")
        if self.temperature <= 0.0:
            raise ValueError(f"temperature must > 0.0, got {self.temperature}")
        if self.top_p <= 0.0 or self.top_p > 1.0:
            raise ValueError(f"top_p must in (0.0, 1.0], got {self.top_p}")
        if self.top_k < -1 or self.top_k == 0:
            raise ValueError(f"top_k must be -1 (disable), or at least 1, got {self.top_k}.")
        if self.max_new_tokens < 1:
            raise ValueError(f"max_new_tokens must be at least 1 , got {self.max_new_tokens}.")
        return 
    
    def to_dict(self):
        ret = {}
        ret["do_sample"] = self.do_sample
        ret["presence_penalty"] = self.presence_penalty
        ret["frequency_penalty"] = self.frequency_penalty
        ret["temperature"] = self.temperature
        ret["top_p"] = self.top_p
        ret["top_k"] = self.top_k
        ret["ignore_eos"] = self.ignore_eos
        ret["max_new_tokens"] = self.max_new_tokens
        return ret
