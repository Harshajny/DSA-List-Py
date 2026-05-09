class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        space_stack=[]
        for asteroid in asteroids:
            stay=True
            while stay and asteroid<0 and space_stack and space_stack[-1]>0:
                if abs(asteroid)>space_stack[-1]:
                    space_stack.pop()
                    continue
                elif abs(asteroid)==space_stack[-1]:
                    space_stack.pop()
                    stay=False
                else:
                    stay=False

            if stay==True:
                space_stack.append(asteroid)
        return space_stack
                
        
        