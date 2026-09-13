class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search max val and small val in rows and do binary search on the specific row

        rt, rb = 0, len(matrix) - 1
        cl, cr = 0, len(matrix[0]) - 1

        while rt <= rb:
            rmid = rt + (rb - rt) // 2
            if target > matrix[rmid][cr]:
                rt = rmid + 1
            elif target < matrix[rmid][cl]:
                rb = rmid - 1
            else:
                while cl <= cr:
                    cmid = cl + (cr - cl) // 2
                    if target > matrix[rmid][cmid]:
                        cl = cmid + 1
                    elif target < matrix[rmid][cmid]:
                        cr = cmid - 1
                    else:
                        return True
                return False
        return False