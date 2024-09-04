class DataFrame:
    def ncol(self):
        """Report the no of columns in the DataFrame"""

    def nrow(self):
        """Report the no of rows in the DataFrame"""

    def cols(self):
        """Return the set of column names"""

    def eq(self, other):
        """Check equality with other DataFrame"""

    def get(self, col, row):
        """Get a scalar value"""

    def select(self, *names):
        """Select a named subset of columns"""

    def filter(self, func):
        """Select a subset of rows by testing values."""
