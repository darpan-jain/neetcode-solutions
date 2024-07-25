class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Use an adjacency list (and run DFS) to check all the courses and if their prequisites can be completed.
        '''

        # Init a dict which will be the adjaceny list for all courses
        preMap = { i: [] for i in range(numCourses) }
        
        # Populate the `preMap` (the adjacency list) with the prereqs for each course
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # visitedSet = all courses along the curr DFS path. Used to avoid any loops in the DFS path.
        visitedSet = set()
        
        ## Helper method to check if the current `crs` can be completed. Using recursive DFS.
        def dfs(crs):
            
            # Base case 1 - course already visited
            if crs in visitedSet:
                return False
            
            # Base case 2 - has no other prereqs/all prereqs can be completed for current course
            if preMap[crs] == []:
                return True
            
            # Here the current course has preqs remaining. 
            # Add the current course to the visited set
            visitedSet.add(crs)
            
            # And check if all the preqs for the current course can be completed
            for pre in preMap[crs]:
                # Recursive DFS on the current prerequisite to check if it cannot be completed.
                if not dfs(pre):
                    return False
                
            # Remove from visited since not checking anymore
            visitedSet.remove(crs)
            # Make the prereqs list empty in the adjacency list, since now we know 
            # that prerequisites for this course can be completed.
            preMap[crs] = []
            
            return True
            
        ## Main loop to check if can finish all courses  
        # Run the DFS to check if you can finish prerequisites for all the courses
        for crs in range(numCourses):
            if not dfs(crs): 
                return False

        # If all okay, the you can finish all courses
        return True