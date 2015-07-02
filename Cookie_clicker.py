"""
Cookie Clicker Simulator
"""
try:
    import simpleplot
except ImportError:
    import SimpleGUICS2Pygame.simpleplot as simpleplot

# Used to increase the timeout, if necessary
try:
    import codeskulptor
except ImportError:
    import SimpleGUICS2Pygame.codeskulptor as codeskulptor
codeskulptor.set_timeout(20)

try:
    import poc_clicker_provided
except ImportError:
    import ext.poc_clicker_provided as provided

try:
    import poc_simpletest
except ImportError:
    import ext.poc_simpletest as poc_simpletest

import math

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self.cookies_produced = 0.0
        self.cookies_current = 0.0
        self.time_current = 0.0
        self.cps_current = 0.0
        self.history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return ("self.cookies_produced:", self.cookies_produced, "self.cookies_current:", self.cookies_current,
                "self.time_current:", self.time_current, "self.cps_current:", self.cps_current)
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self.cookies_current
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self.cps_current
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self.time_current
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self.history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        #math.ceil((bribe_rate - earning_so_far)/float(salary_rate))
        result = 0
        if self.cps_current != 0:
            result = math.ceil((cookies - self.cookies_current)/float(self.cps_current))

        return result
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time <= 0.0:
            pass
        else:
            self.time_current += time
            self.cookies_current += time * self.cps_current
    
    def buy_item(self, item_name, cost, additional_cps):
        item = provided.BuildInfo()
        #print(type(provided.BuildInfo()))
        #print(type(provided.BuildInfo.build_items(item)))
        if cost > self.cookies_current:
            pass
        elif item_name in item.build_items():
            print("yes")
            self.cps_current += item.get_cps(item_name)
            self.cookies_current -= item.get_cost(item_name)
            #[(0.0, None, 0.0, 0.0)]
            self.history.append((self.time_current, item_name, item.get_cost(item_name), self.cookies_produced))
        else:
            print("no")

   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Replace with your code
    return ClickerState()


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    return None

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print(strategy_name, ":", state)

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)

if __name__ == "__main__":
    clicker = ClickerState()
    test = poc_simpletest.TestSuite()
    clicker.cps_current = 2.0
    test.run_test(clicker.time_until(20), 10, "time until")
    clicker.cookies_current = 11.00
    #self.history.append((self.time_current, item_name, item.get_cost(item_name), self.cookies_produced))
    clicker.buy_item("Cursor", 10, 10)
    print(clicker.get_history())
    #print(clicker.time_until(20))
    test.report_results()
    #run()
    

