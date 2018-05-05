# Generated from Lury.g4 by ANTLR 4.7.1

from antlr4 import *

if __name__ is not None and "." in __name__:
    from .LuryParser import LuryParser
else:
    from src.LuryParser import LuryParser


# from antlr4.tree.Tree import TerminalNode


class LuryListenerBase(ParseTreeListener):
    CONTEXT = '__$'
    CONTEXT_VALUE = '$'
    CONTEXT_VARIABLE = '$v'

    def __init__(self, output):
        self._output = output
        self.stack = []

    def push(self, text: str):
        self.stack.append(text)

    def pop(self) -> str:
        return self.stack.pop()

    def pop2(self) -> (str, str):
        return self.stack.pop(), self.stack.pop()

    def pop_or(self, text: str) -> str:
        if len(self.stack) > 0:
            return self.pop()
        else:
            return text

    def pop_take(self, count: int) -> []:
        stack_copy = []

        for _ in range(count):
            stack_copy.append(self.pop())

        stack_copy.reverse()
        return stack_copy

    def output(self, text: str):
        print(text, file=self._output)

    def output_header(self):
        print(f'(({self.CONTEXT} = {{{self.CONTEXT_VALUE}: null, {self.CONTEXT_VARIABLE}: {{}}}}) => {{', file=self._output)
        #print(
        #    f'const ;', file=self._output)

    def output_footer(self):
        print(f'return {self.CONTEXT}.{self.CONTEXT_VALUE};}})();',
              file=self._output)

    def get_context_value(self) -> str:
        return f'{self.CONTEXT}.{self.CONTEXT_VALUE}'

    def get_context_variable(self, name: str) -> str:
        return f'{self.CONTEXT}.{self.CONTEXT_VARIABLE}.{name}'


# This class defines a complete listener for a parse tree produced by LuryParser.
# noinspection PyUnusedLocal
class LuryListener(LuryListenerBase):
    JS_NIL = 'null'
    JS_TRUE = 'true'
    JS_FALSE = 'false'

    def __init__(self, output):
        super().__init__(output)
        self.pop_count = 0

    # Enter a parse tree produced by LuryParser#program.
    def enterProgram(self, ctx: LuryParser.ProgramContext):
        self.output_header()

    # Exit a parse tree produced by LuryParser#program.
    def exitProgram(self, ctx: LuryParser.ProgramContext):
        self.output_footer()

    # Enter a parse tree produced by LuryParser#expression_statement.
    def enterExpression_statement(self, ctx: LuryParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by LuryParser#expression_statement.
    def exitExpression_statement(self, ctx: LuryParser.Expression_statementContext):
        v = self.pop_or(self.JS_NIL)
        self.output(f'{self.get_context_value()} = {v};')

    # Exit a parse tree produced by LuryParser#Assign.
    def exitAssign(self, ctx: LuryParser.AssignContext):
        right, left = self.pop2()
        self.push(f'({left} = {right})')

    # Enter a parse tree produced by LuryParser#Comma.
    def enterComma(self, ctx: LuryParser.CommaContext):
        pass

    # Exit a parse tree produced by LuryParser#Comma.
    def exitComma(self, ctx: LuryParser.CommaContext):
        pass

    # Exit a parse tree produced by LuryParser#BoolNot.
    def exitBoolNot(self, ctx: LuryParser.BoolNotContext):
        factor = self.pop()
        self.push(f'(!{factor})')

    # Exit a parse tree produced by LuryParser#Not.
    def exitNot(self, ctx: LuryParser.NotContext):
        right, left = self.pop2()
        self.push(f'({left} != {right})')

    # Exit a parse tree produced by LuryParser#Etq.
    def exitEtq(self, ctx: LuryParser.EtqContext):
        # NOTE: Etq -> Gtq
        right, left = self.pop2()
        self.push(f'({left} >= {right})')

    # Exit a parse tree produced by LuryParser#Lt.
    def exitLt(self, ctx: LuryParser.LtContext):
        right, left = self.pop2()
        self.push(f'({left} < {right})')

    # Exit a parse tree produced by LuryParser#Ltq.
    def exitLtq(self, ctx: LuryParser.LtqContext):
        right, left = self.pop2()
        self.push(f'({left} <= {right})')

    # Exit a parse tree produced by LuryParser#Eq.
    def exitEq(self, ctx: LuryParser.EqContext):
        right, left = self.pop2()
        self.push(f'({left} === {right})')

    # Exit a parse tree produced by LuryParser#Gt.
    def exitGt(self, ctx: LuryParser.GtContext):
        right, left = self.pop2()
        self.push(f'({left} > {right})')

    # Enter a parse tree produced by LuryParser#RangeOpen.
    def enterRangeOpen(self, ctx: LuryParser.RangeOpenContext):
        pass

    # Exit a parse tree produced by LuryParser#RangeOpen.
    def exitRangeOpen(self, ctx: LuryParser.RangeOpenContext):
        pass

    # Enter a parse tree produced by LuryParser#RangeClose.
    def enterRangeClose(self, ctx: LuryParser.RangeCloseContext):
        pass

    # Exit a parse tree produced by LuryParser#RangeClose.
    def exitRangeClose(self, ctx: LuryParser.RangeCloseContext):
        pass

    # Enter a parse tree produced by LuryParser#In.
    def enterIn(self, ctx: LuryParser.InContext):
        pass

    # Exit a parse tree produced by LuryParser#In.
    def exitIn(self, ctx: LuryParser.InContext):
        pass

    # Enter a parse tree produced by LuryParser#NotIn.
    def enterNotIn(self, ctx: LuryParser.NotInContext):
        pass

    # Exit a parse tree produced by LuryParser#NotIn.
    def exitNotIn(self, ctx: LuryParser.NotInContext):
        pass

    # Exit a parse tree produced by LuryParser#Or.
    def exitOr(self, ctx: LuryParser.OrContext):
        right, left = self.pop2()
        self.push(f'({left} | {right})')

    # Exit a parse tree produced by LuryParser#Xor.
    def exitXor(self, ctx: LuryParser.XorContext):
        right, left = self.pop2()
        self.push(f'({left} ^ {right})')

    # Exit a parse tree produced by LuryParser#And.
    def exitAnd(self, ctx: LuryParser.AndContext):
        right, left = self.pop2()
        self.push(f'({left} & {right})')

    # Exit a parse tree produced by LuryParser#LShift.
    def exitLShift(self, ctx: LuryParser.LShiftContext):
        right, left = self.pop2()
        self.push(f'({left} << {right})')

    # Exit a parse tree produced by LuryParser#RShift.
    def exitRShift(self, ctx: LuryParser.RShiftContext):
        right, left = self.pop2()
        self.push(f'({left} >> {right})')

    # Exit a parse tree produced by LuryParser#Add.
    def exitAdd(self, ctx: LuryParser.AddContext):
        right, left = self.pop2()
        self.push(f'({left} + {right})')

    # Exit a parse tree produced by LuryParser#Sub.
    def exitSub(self, ctx: LuryParser.SubContext):
        right, left = self.pop2()
        self.push(f'({left} - {right})')

    # Exit a parse tree produced by LuryParser#Con.
    def exitCon(self, ctx: LuryParser.ConContext):
        right, left = self.pop2()
        self.push(f'{left}.concat({right})')

    # Exit a parse tree produced by LuryParser#Div.
    def exitDiv(self, ctx: LuryParser.DivContext):
        right, left = self.pop2()
        self.push(f'({left} / {right})')

    # Exit a parse tree produced by LuryParser#Mod.
    def exitMod(self, ctx: LuryParser.ModContext):
        right, left = self.pop2()
        self.push(f'({left} % {right})')

    # Exit a parse tree produced by LuryParser#Mul.
    def exitMul(self, ctx: LuryParser.MulContext):
        right, left = self.pop2()
        self.push(f'({left} * {right})')

    # Exit a parse tree produced by LuryParser#IDiv.
    def exitIDiv(self, ctx: LuryParser.IDivContext):
        right, left = self.pop2()
        self.push(f'(({left} / {right}) | 0)')

    # Exit a parse tree produced by LuryParser#Power.
    def exitPower(self, ctx: LuryParser.PowerContext):
        if ctx.op is None:
            return

        right, left = self.pop2()
        self.push(f'Math.pow({left}, {right})')

    # Enter a parse tree produced by LuryParser#Unary.
    def enterUnary(self, ctx: LuryParser.UnaryContext):
        pass

    # Exit a parse tree produced by LuryParser#Unary.
    def exitUnary(self, ctx: LuryParser.UnaryContext):
        pass

    # Exit a parse tree produced by LuryParser#Indexer.
    def exitIndexer(self, ctx: LuryParser.IndexerContext):
        index, name = self.pop2()
        self.push(f'{name}[{index}]')

    # Enter a parse tree produced by LuryParser#PostDecrement.
    def enterPostDecrement(self, ctx: LuryParser.PostDecrementContext):
        pass

    # Exit a parse tree produced by LuryParser#PostDecrement.
    def exitPostDecrement(self, ctx: LuryParser.PostDecrementContext):
        pass

    # Enter a parse tree produced by LuryParser#PostIncrement.
    def enterPostIncrement(self, ctx: LuryParser.PostIncrementContext):
        pass

    # Exit a parse tree produced by LuryParser#PostIncrement.
    def exitPostIncrement(self, ctx: LuryParser.PostIncrementContext):
        pass

    # Enter a parse tree produced by LuryParser#PrimaryExp.
    def enterPrimaryExp(self, ctx: LuryParser.PrimaryExpContext):
        pass

    # Exit a parse tree produced by LuryParser#PrimaryExp.
    def exitPrimaryExp(self, ctx: LuryParser.PrimaryExpContext):
        pass

    # Enter a parse tree produced by LuryParser#key_index.
    def enterKey_index(self, ctx: LuryParser.Key_indexContext):
        pass

    # Exit a parse tree produced by LuryParser#key_index.
    def exitKey_index(self, ctx: LuryParser.Key_indexContext):
        pass

    # Exit a parse tree produced by LuryParser#Identifier.
    def exitIdentifier(self, ctx: LuryParser.IdentifierContext):
        self.push(self.get_context_variable(ctx.getText()))

    # Exit a parse tree produced by LuryParser#True.
    def exitTrue(self, ctx: LuryParser.TrueContext):
        self.push(self.JS_TRUE)

    # Exit a parse tree produced by LuryParser#False.
    def exitFalse(self, ctx: LuryParser.FalseContext):
        self.push(self.JS_FALSE)

    # Exit a parse tree produced by LuryParser#Nil.
    def exitNil(self, ctx: LuryParser.NilContext):
        self.push(self.JS_NIL)

    def exitParentheses(self, ctx: LuryParser.ParenthesesContext):
        exp = self.pop()
        self.push(f'({exp})')

    # Enter a parse tree produced by LuryParser#String.
    def enterString(self, ctx: LuryParser.StringContext):
        pass

    # Exit a parse tree produced by LuryParser#String.
    def exitString(self, ctx: LuryParser.StringContext):
        self.push(ctx.getText())

    # Exit a parse tree produced by LuryParser#Real.
    def exitReal(self, ctx: LuryParser.RealContext):
        self.push(ctx.getText())

    # Exit a parse tree produced by LuryParser#Integer.
    def exitInteger(self, ctx: LuryParser.IntegerContext):
        self.push(ctx.getText())

    #

    # Enter a parse tree produced by LuryParser#List.
    def enterList(self, ctx: LuryParser.ListContext):
        pass

    # Exit a parse tree produced by LuryParser#List.
    def exitList(self, ctx: LuryParser.ListContext):
        pass

    # Enter a parse tree produced by LuryParser#Hash.
    def enterHash(self, ctx: LuryParser.HashContext):
        pass

    # Exit a parse tree produced by LuryParser#Hash.
    def exitHash(self, ctx: LuryParser.HashContext):
        pass

    # Exit a parse tree produced by LuryParser#list_literal.
    def exitList_literal(self, ctx: LuryParser.List_literalContext):
        if ctx.element is None:
            self.push('[]')

        self.push(f'[{", ".join(self.pop_take(self.pop_count))}]')
        self.pop_count = 0

    # Exit a parse tree produced by LuryParser#ListElements.
    def exitListElements(self, ctx: LuryParser.ListElementsContext):
        self.pop_count += 1

    # Exit a parse tree produced by LuryParser#ListElement.
    def exitListElement(self, ctx: LuryParser.ListElementContext):
        self.pop_count += 1

    # Enter a parse tree produced by LuryParser#hash_literal.
    def enterHash_literal(self, ctx: LuryParser.Hash_literalContext):
        pass

    # Exit a parse tree produced by LuryParser#hash_literal.
    def exitHash_literal(self, ctx: LuryParser.Hash_literalContext):
        pass

    # Enter a parse tree produced by LuryParser#HashElementName.
    def enterHashElementName(self, ctx: LuryParser.HashElementNameContext):
        pass

    # Exit a parse tree produced by LuryParser#HashElementName.
    def exitHashElementName(self, ctx: LuryParser.HashElementNameContext):
        pass

    # Enter a parse tree produced by LuryParser#HashElements.
    def enterHashElements(self, ctx: LuryParser.HashElementsContext):
        pass

    # Exit a parse tree produced by LuryParser#HashElements.
    def exitHashElements(self, ctx: LuryParser.HashElementsContext):
        pass

    # Enter a parse tree produced by LuryParser#HashElement.
    def enterHashElement(self, ctx: LuryParser.HashElementContext):
        pass

    # Exit a parse tree produced by LuryParser#HashElement.
    def exitHashElement(self, ctx: LuryParser.HashElementContext):
        pass

    # Enter a parse tree produced by LuryParser#HashElementsVariable.
    def enterHashElementsVariable(self, ctx: LuryParser.HashElementsVariableContext):
        pass

    # Exit a parse tree produced by LuryParser#HashElementsVariable.
    def exitHashElementsVariable(self, ctx: LuryParser.HashElementsVariableContext):
        pass

    # Enter a parse tree produced by LuryParser#HashElementVariable.
    def enterHashElementVariable(self, ctx: LuryParser.HashElementVariableContext):
        pass

    # Exit a parse tree produced by LuryParser#HashElementVariable.
    def exitHashElementVariable(self, ctx: LuryParser.HashElementVariableContext):
        pass

    # Enter a parse tree produced by LuryParser#HashElementsName.
    def enterHashElementsName(self, ctx: LuryParser.HashElementsNameContext):
        pass

    # Exit a parse tree produced by LuryParser#HashElementsName.
    def exitHashElementsName(self, ctx: LuryParser.HashElementsNameContext):
        pass
