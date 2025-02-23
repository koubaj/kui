import random
from kuimaze2 import SearchProblem, Map, State


class Agent:
    """Simple example of a random agent."""

    def __init__(self, environment: SearchProblem):
        self.environment = environment

    def find_path(self) -> list[State]:
        """
        Find a path from the start state to any goal state.

        This method must be implemented by you.
        """
        # Get the start state from the environment
        state = self.environment.get_start()
        # Lets track the cost to reach states
        costs = {state: 0}
        print(f"Starting random search from state: {state}")

        goal_reached = False
        # Data structure to choose, which state is next
        queue = [state]
        # Create dict to store postitions, so I can backtrack in the end
        states = {state: None}

        while queue:
            state = queue.pop(0)
            actions = self.environment.get_actions(state)

            # Go through all possible actions from state
            for i in actions:
                new_state, cost = self.environment.get_transition_result(
                    state, i
                )
                if new_state in states:
                    continue

                queue.append(new_state)
                states[new_state] = state
                costs[new_state] = costs[state] + cost
                print(
                    f"Transition: {state} -> {new_state}, cost of new state: {costs[new_state]}"
                )

            # End search, if the goal is reached
            if self.environment.is_goal(state):
                goal_reached = True
                print("Goal reached!!!")
                break

            # Visualize the state of the algorithm:
            # * Use cost values as texts in cells
            # * Use cost values as colors of cells
            # * Mark current and new states
            # * Wait for keypress (read info in terminal)
            self.environment.render(
                current_state=state,
                next_states=[new_state],
                texts=costs,
                colors=costs,
                wait=True,
            )
            state = new_state

        # Use backtracking to find the path
        # If the goal was not reached, return None
        if goal_reached:
            path = [state]
            while state != self.environment.get_start():
                state = states[state]
                path.append(state)
            path.reverse()
        else:
            path = None

        self.environment.render(path=path, wait=True, use_keyboard=True)
        return path


if __name__ == "__main__":
    # Create a Map instance
    MAP = """
    .S...
    .###.
    ...#G
    """
    map = Map.from_string(MAP)
    # Create an environment as a SearchProblem initialized with the map
    env = SearchProblem(map, graphics=True)
    # Create the agent and find the path
    agent = Agent(env)
    agent.find_path()
