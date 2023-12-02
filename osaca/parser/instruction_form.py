#!/usr/bin/env python3

from osaca.parser.directive import DirectiveOperand


class instructionForm:
    def __init__(
        self,
        instruction_id=None,
        operands_id=[],
        hidden_operands=[],
        directive_id=None,
        comment_id=None,
        label_id=None,
        line=None,
        line_number=None,
        semantic_operands={"source": [], "destination": [], "src_dst": []},
        throughput=None,
        latency=None,
        uops=None,
        port_pressure=None,
        operation=None,
        breaks_dep=False,
    ):
        self._instruction_id = instruction_id
        self._operands_id = operands_id
        self._hidden_operands = hidden_operands
        self._directive_id = directive_id
        self._comment_id = comment_id
        self._label_id = label_id
        self._line = line
        self._line_number = line_number

        self._semantic_operands = semantic_operands
        self._operation = operation
        self._uops = uops
        self._breaks_dep = breaks_dep
        # self.semantic_operands = {"source": [], "destination": [], "src_dst": []}
        self._latency = latency
        self._throughput = throughput
        self._latency_cp = []
        self._latency_lcd = []
        self._latency_wo_load = None
        self._port_pressure = port_pressure
        self._port_uops = []
        self._flags = []

    @property
    def semantic_operands(self):
        return self._semantic_operands

    @property
    def instruction(self):
        return self._instruction_id

    @property
    def label(self):
        return self._label_id

    @property
    def comment(self):
        return self._comment_id

    @property
    def directive(self):
        return self._directive_id

    @property
    def line_number(self):
        return self._line_number

    @property
    def line(self):
        return self._line

    @property
    def operands(self):
        return self._operands_id

    @property
    def hidden_operands(self):
        return self._hidden_operands

    @property
    def port_pressure(self):
        return self._port_pressure

    @property
    def port_uops(self):
        return self._port_uops

    @property
    def flags(self):
        return self._flags

    @property
    def uops(self):
        return self._uops

    @property
    def throughput(self):
        return self._throughput

    @property
    def latency(self):
        return self._latency

    @property
    def latency_wo_load(self):
        return self._latency_wo_load

    @property
    def operation(self):
        return self._operation

    @property
    def breaks_dep(self):
        return self._breaks_dep

    @semantic_operands.setter
    def semantic_operands(self, semantic_operands):
        self._semantic_operands = semantic_operands

    @directive.setter
    def directive(self, directive):
        self._directive_id = directive

    @line_number.setter
    def line_number(self, line_number):
        self._line_number = line_number

    @line.setter
    def line(self, line):
        self._line = line

    @operands.setter
    def operands(self, operands):
        self._operands_id = operands

    @hidden_operands.setter
    def hidden_operands(self, hidden_operands):
        self._hidden_operands = hidden_operands

    @breaks_dep.setter
    def breaks_dep(self, boolean):
        self._breaks_dep = boolean

    @instruction.setter
    def instruction(self, instruction):
        self._instruction_id = instruction

    @label.setter
    def label(self, label):
        self._label_id = label

    @comment.setter
    def comment(self, comment):
        self._comment_id = comment

    @port_pressure.setter
    def port_pressure(self, port_pressure):
        self._port_pressure = port_pressure

    @port_uops.setter
    def port_uops(self, port_uops):
        self._port_uops = port_uops

    @flags.setter
    def flags(self, flags):
        self._flags = flags

    @uops.setter
    def uops(self, uops):
        self._uops = uops

    @throughput.setter
    def throughput(self, throughput):
        self._throughput = throughput

    @operation.setter
    def operation(self, operation):
        self._operation = operation

    @latency.setter
    def latency(self, latency):
        self._latency = latency

    @latency_wo_load.setter
    def latency_wo_load(self, latency_wo_load):
        self._latency_wo_load = latency_wo_load

    def __str__(self):
        attributes = {
            "instruction_id": self.instruction,
            "operands_id": self.operands,
            "hidden_operands": self.hidden_operands,
            "directive_id": self.directive,
            "comment_id": self.comment,
            "label_id": self.label,
            "line": self.line,
            "line_number": self.line_number,
            "semantic_operands": self.semantic_operands,
            "throughput": self.throughput,
            "latency": self.latency,
            "uops": self.uops,
            "port_pressure": self.port_pressure,
            "operation": self.operation,
            "breaks_dep": self.breaks_dep,
        }
        attr_str = "\n ".join(f"{key}={value}" for key, value in attributes.items())
        return f"instructionForm({attr_str})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, instructionForm):
            return (
                self._instruction_id == other._instruction_id
                and self._operands_id == other._operands_id
                and self._directive_id == other._directive_id
                and self._comment_id == other._comment_id
                and self._label_id == other._label_id
                and self._line == other._line
                and self._line_number == other._line_number
                and self._semantic_operands == other._semantic_operands
            )
        return False
