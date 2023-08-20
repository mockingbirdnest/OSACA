#!/usr/bin/env python3

from osaca.parser.operand import Operand

class DirectiveOperand(Operand):
    def __init__(self, NAME_ID = None, PARAMETER_ID = None, COMMENT_ID = None):
        super().__init__()
        self._NAME_ID = NAME_ID
        self._PARAMETER_ID = PARAMETER_ID
        self._COMMENT_ID = COMMENT_ID
    
    @property
    def name(self):
        return self._NAME_ID
    
    @property
    def parameters(self):
        return self._PARAMETER_ID
    
    @property
    def comment(self):
        return self._COMMENT_ID

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self._COMMENT_ID:
            raise StopIteration
        return self._COMMENT_ID.pop(0)

    @name.setter
    def name(self, name):
        self._NAME_ID = name
    
    @parameters.setter
    def parameters(self, parameters):
        self._PARAMETER_ID = parameters
    
    @comment.setter
    def comment(self, comment):
        self._COMMENT_ID = comment