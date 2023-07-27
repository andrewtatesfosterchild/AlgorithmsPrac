class Solution:
    # Logic : Pair matching problem ; Stack approach

    '''
        "Stack comes to rescue in all the pair matching type of problems."

        Let's understand what collides and what not first.

        Two asteroids, Same sign, Never collide
        Two asteroids, Different sign, Always collide?

        
        To get a successful collision, The left asteroid must be right moving and the right asteroid must be left moving

        Keeping this in mind , We shall do pair matching with stack

        if not asteroids or len(asteroids) == 1:
            return asteroids
        
        In case asteroids is empty or a single value

        for a in asteroids:
            while stack and stack[-1] >= 0 and a < 0: # Collision case
                collision = stack[-1] + a # colliding
                if collision <= 0: # Stack dop destroyed
                    stack.pop()
                if collision >= 0: # New asteroid destroyed / both destroyed
                    break
            
            else:
                stack.append(a) # Never collide

            What are we doing here?

            We are working on each asteroid, Checking with the topmost right moving asteroid , if stack[-1] >=0 and a < 0 , collision is bound to happen, But if stack[-1] is not greater than 0, It is left moving and collision can never occur, So the below else case will append the asteroid a in undestroyed stack

            But what if collision case occurs?

            Then collision = stack[-1] + a
            
            Now two cases might occur:
                collision <= 0:
                This means that the asteroid was mightier than the stack top and the stack top got destroyed
                So, stack.pop()

                Are we done with this asteroid? No, Its not destroyed yet nor it is inside the stack, making it indestructible, Either should be the case with each asteroid, So the while loop will keep comparing till every last element of the stack is either popped or the asteroid is destroyed by some mightier asteroid

                collision >= 0:
                This means that the asteroid a was pulverized by our stack top asteroid.
                break

                * Why break?
                Do we have anything further to do with this asteroid a?
                No, Because it is already destroyed, We break the while loop and let the for loop go to the next asteroid for further comparisions

            
            After this, The stack will contain all the mighty and undestructable asteroid

            return stack

            That's it, Done
    '''
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        if not asteroids or len(asteroids) == 1:
            return asteroids
        
        stack = [] # Contains the undestroyed asteroids

        for a in asteroids:
            while stack and stack[-1] >= 0 and a < 0: # Collision case
                collision = stack[-1] + a # colliding
                if collision <= 0: # Stack dop destroyed
                    stack.pop()
                if collision >= 0: # New asteroid destroyed / both destroyed
                    break
            
            else:
                stack.append(a) # Never collide

        return stack