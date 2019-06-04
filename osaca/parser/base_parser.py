#!usr/bin/env python3


class BaseParser(object):
    # Identifiers for operand types
    COMMENT_ID = 'comment'
    DIRECTIVE_ID = 'directive'
    IMMEDIATE_ID = 'immediate'
    LABEL_ID = 'label'
    MEMORY_ID = 'memory'
    REGISTER_ID = 'register'

    def __init__(self):
        self.construct_parser()

    def parse_file(self, file_content, start_line=0):
        '''
        Parse assembly file. This includes *not* extracting of the marked kernel and
        the parsing of the instruction forms.

        :param str file_content: assembly code
        :param int start_line: offset, if first line in file_content is meant to be not 1
        :return: list of instruction forms
        '''
        # Create instruction form list
        asm_instructions = []
        lines = file_content.split('\n')
        for i, line in enumerate(lines):
            if line == '':
                continue
            asm_instructions.append(self.parse_line(line, i + 1 + start_line))
        return asm_instructions

    def parse_line(self, line, line_number):
        # Done in derived classes
        raise NotImplementedError()

    def parse_instruction(self, instruction):
        # Done in derived classes
        raise NotImplementedError()

    def construct_parser(self):
        raise NotImplementedError()
