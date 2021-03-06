import analizer.abstract.symbol as sym


class Environment:
    """
    Esta clase representa los simbolos de las variables declaradas.
    """
    def __init__(self) -> None:
        self.variables = {}
        self.types = {}

    def updateVar(self, id, value, type_):
        """
        Actualiza el valor de una llave en la tabla de simbolos
        """
        if id in self.variables:
            symbol = self.variables[id]
            symbol = sym.Symbol(
                id, value, type_, symbol.row, symbol.column)
            self.variables[id] = symbol
            return True
        return None

    def addVar(self, id, value, type_, row, column):
        """
        Inserta un nuevo simbolo en la tabla de simbolos
        """
        env = self
        if id in env.variables:
            return None
        symbol = sym.Symbol(value, type_, row, column)
        env.variables[id] = symbol
        return symbol

    def addSymbol(self, id, symbol):
        """
        Inserta un simbolo en la tabla de simbolos
        """
        env = self
        if id in env.variables:
            return None
        env.variables[id] = symbol
        return symbol

    def getVar(self, id):
        """
        docstring
        """
        if id in self.variables:
            return self.variables[id]
	
