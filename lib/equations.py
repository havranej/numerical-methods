class DifferentialEquationSolution:
    def __init__(self, equation, solving_function, h = 0.01, title = "Untitled solution", exact = False):
        self.equation = equation
        self.solving_function = solving_function
        self.title = title
        self.exact = exact
        
        self.update(h)
  
    def __repr__(self):
        return f"<{self.title} of {self.equation}>"
    
    def __str__(self):
        return self.title + "\nt: " + str(self.t_list) + "\nx: " + str(self.x_list)
    
    def update(self, h):
        self.h = h
        self.t_list = np.arange(self.equation.t0, self.equation.t_max + h, h)
        self.x_list = self.solving_function(self.t_list, self.equation.f, self.equation.x0)
        
    def update_plot(self):
        self.plot_line.set_data(self.t_list, self.x_list)


class DifferentialEquation:
    def __init__(self, f, x0, t0 = 0, t_max = 1):
        self.f = f
        self.x0 = x0
        self.t0 = t0
        self.t_max = t_max
        self.solutions = []
        
    def add_solution(self, solving_function, h = 0.01, title = "Untitled solution", exact = False):
        solution = DifferentialEquationSolution(self, solving_function, h, title, exact)
        self.solutions.append(solution)
        
    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        for solution in self.solutions:
            plot_line, = ax.plot(solution.t_list, solution.x_list, label = solution.title)
            solution.plot_line = plot_line
        
        ax.legend()
        
    def plot_interactive(self, h_min = 0.01, h_max = 1, h_step = 0.01):
        self.plot()
        
        def update(h):
            for solution in self.solutions:
                if not solution.exact:
                    solution.update(h)
                    solution.update_plot()
        
        interact(update, h=(h_min, h_max, h_step));
    
    def _rmse(self, a, b):
        assert np.all(a.t_list == b.t_list), f"Nodes for {a.title} and {b.title} are not the same. Maybe the step (h) is different?"
        a = np.array(a.x_list)
        b = np.array(b.x_list)
        
        return np.sqrt(((a-b)**2).mean())
    
    def measure_rmse(self):
        exact_list = [solution for solution in self.solutions if solution.exact]
        assert len(exact_list) == 1, "There was either no exact solution or multiple exact solutions. Did you use 'exact = True' exactly once?"
        exact_solution = exact_list[0]
        
        rmse_dict = {}
        for solution in self.solutions:
            if solution.exact:
                continue
            rmse = self._rmse(exact_solution, solution)
            rmse_dict[solution.title] = rmse
        return rmse_dict
        