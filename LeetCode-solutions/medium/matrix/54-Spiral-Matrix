class Solution:
    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
