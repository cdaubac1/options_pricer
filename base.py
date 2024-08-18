from enum import Enum
from abc import ABC, abstractmethod

class OPTION_TYPE(Enum):
    CALL_OPTION = 'Call Option'
    PUT_OPTION = 'Put Option'

class OptionPricingModel(ABC):
    
    @abstractmethod
    def _calculate_call_option_price(self):
        pass

    @abstractmethod
    def _calculate_put_option_price(self):
        pass

    def calculate_option_price(self, option_type):
        if option_type == OPTION_TYPE.CALL_OPTION.value:
            return self._calculate_call_option_price()
        elif option_type == OPTION_TYPE.PUT_OPTION.value:
            return self._calculate_put_option_price()
        else:
            raise ValueError("Unknown option type")


