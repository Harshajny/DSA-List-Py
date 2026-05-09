class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #Depth First Search
        starting_pixel=image[sr][sc]
        rl=len(image)
        cl=len(image[0])
        if starting_pixel==color:
            return image
        def fill(r,c):
            if r>=rl or r<0 or c<0 or c>=cl:
                return
            if image[r][c]!=starting_pixel:
                return
            image[r][c]=color
            fill(r+1,c)
            fill(r-1,c)
            fill(r,c+1)
            fill(r,c-1)

        fill(sr,sc)
        return image
    
                