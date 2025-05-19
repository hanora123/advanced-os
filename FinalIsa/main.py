import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class OSAlgorithmsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OS Algorithms Simulator")
        self.root.geometry("800x600")
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create frames for each tab
        self.vm_frame = ttk.Frame(self.notebook)
        self.disk_frame = ttk.Frame(self.notebook)
        
        # Add frames to notebook
        self.notebook.add(self.vm_frame, text="Virtual Memory Algorithms")
        self.notebook.add(self.disk_frame, text="Disk Scheduling Algorithms")
        
        # Setup each tab
        self.setup_vm_tab()
        self.setup_disk_tab()
    
    def setup_vm_tab(self):
        # Algorithm selection
        algo_frame = ttk.LabelFrame(self.vm_frame, text="Algorithm Selection")
        algo_frame.pack(fill="x", padx=10, pady=10)
        
        self.vm_algo = tk.StringVar(value="FIFO")
        ttk.Radiobutton(algo_frame, text="FIFO", variable=self.vm_algo, value="FIFO").grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(algo_frame, text="LRU", variable=self.vm_algo, value="LRU").grid(row=0, column=1, padx=5, pady=5)
        ttk.Radiobutton(algo_frame, text="Optimal", variable=self.vm_algo, value="Optimal").grid(row=0, column=2, padx=5, pady=5)
        ttk.Radiobutton(algo_frame, text="Second Chance", variable=self.vm_algo, value="Second Chance").grid(row=0, column=3, padx=5, pady=5)
        
        # Input frame
        input_frame = ttk.LabelFrame(self.vm_frame, text="Input Parameters")
        input_frame.pack(fill="x", padx=10, pady=10)
        
        ttk.Label(input_frame, text="Number of Frames:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.vm_frames = ttk.Entry(input_frame, width=10)
        self.vm_frames.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Reference String (space-separated):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.vm_ref_string = ttk.Entry(input_frame, width=50)
        self.vm_ref_string.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(self.vm_frame)
        button_frame.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(button_frame, text="Run", command=self.run_vm_algorithm).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_vm).pack(side="left", padx=5)
        
        # Results frame
        self.vm_result_frame = ttk.LabelFrame(self.vm_frame, text="Results")
        self.vm_result_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Canvas for visualization
        self.vm_canvas_frame = ttk.Frame(self.vm_result_frame)
        self.vm_canvas_frame.pack(fill="both", expand=True)
    
    def setup_disk_tab(self):
        # Algorithm selection
        algo_frame = ttk.LabelFrame(self.disk_frame, text="Algorithm Selection")
        algo_frame.pack(fill="x", padx=10, pady=10)
        
        self.disk_algo = tk.StringVar(value="SSTF")
        ttk.Radiobutton(algo_frame, text="SSTF", variable=self.disk_algo, value="SSTF").grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(algo_frame, text="SCAN", variable=self.disk_algo, value="SCAN").grid(row=0, column=1, padx=5, pady=5)
        ttk.Radiobutton(algo_frame, text="C-SCAN", variable=self.disk_algo, value="C-SCAN").grid(row=0, column=2, padx=5, pady=5)
        ttk.Radiobutton(algo_frame, text="LOOK", variable=self.disk_algo, value="LOOK").grid(row=0, column=3, padx=5, pady=5)
        ttk.Radiobutton(algo_frame, text="C-LOOK", variable=self.disk_algo, value="C-LOOK").grid(row=0, column=4, padx=5, pady=5)
        
        # Input frame
        input_frame = ttk.LabelFrame(self.disk_frame, text="Input Parameters")
        input_frame.pack(fill="x", padx=10, pady=10)
        
        ttk.Label(input_frame, text="Initial Head Position:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.disk_head = ttk.Entry(input_frame, width=10)
        self.disk_head.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Max Cylinder:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.disk_max = ttk.Entry(input_frame, width=10)
        self.disk_max.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Request Queue (space-separated):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.disk_queue = ttk.Entry(input_frame, width=50)
        self.disk_queue.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(self.disk_frame)
        button_frame.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(button_frame, text="Run", command=self.run_disk_algorithm).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_disk).pack(side="left", padx=5)
        
        # Results frame
        self.disk_result_frame = ttk.LabelFrame(self.disk_frame, text="Results")
        self.disk_result_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Canvas for visualization
        self.disk_canvas_frame = ttk.Frame(self.disk_result_frame)
        self.disk_canvas_frame.pack(fill="both", expand=True)
    
    def validate_input(self, input_str, input_type="int"):
        """Validate user input"""
        if input_type == "int":
            try:
                value = int(input_str)
                if value <= 0:
                    return False, "Value must be positive"
                return True, value
            except ValueError:
                return False, "Value must be a number"
        elif input_type == "list":
            try:
                values = [int(x) for x in input_str.split()]
                if any(x < 0 for x in values):
                    return False, "Values must be non-negative"
                return True, values
            except ValueError:
                return False, "All values must be numbers"
        return False, "Unknown input type"
    
    def run_vm_algorithm(self):
        # Clear previous results
        for widget in self.vm_canvas_frame.winfo_children():
            widget.destroy()
        
        # Validate inputs
        valid_frames, frames_result = self.validate_input(self.vm_frames.get())
        if not valid_frames:
            messagebox.showerror("Input Error", f"Number of frames: {frames_result}")
            return
        
        valid_ref, ref_result = self.validate_input(self.vm_ref_string.get(), "list")
        if not valid_ref:
            messagebox.showerror("Input Error", f"Reference string: {ref_result}")
            return
        
        # Get selected algorithm
        algorithm = self.vm_algo.get()
        
        # Run the selected algorithm
        if algorithm == "FIFO":
            page_faults, frames_state = self.fifo(ref_result, frames_result)
        elif algorithm == "LRU":
            page_faults, frames_state = self.lru(ref_result, frames_result)
        elif algorithm == "Optimal":
            page_faults, frames_state = self.optimal(ref_result, frames_result)
        elif algorithm == "Second Chance":
            page_faults, frames_state = self.second_chance(ref_result, frames_result)
        
        # Display results
        self.display_vm_results(ref_result, frames_state, page_faults)
    
    def run_disk_algorithm(self):
        # Clear previous results
        for widget in self.disk_canvas_frame.winfo_children():
            widget.destroy()
        
        # Validate inputs
        valid_head, head_result = self.validate_input(self.disk_head.get())
        if not valid_head:
            messagebox.showerror("Input Error", f"Head position: {head_result}")
            return
        
        valid_max, max_result = self.validate_input(self.disk_max.get())
        if not valid_max:
            messagebox.showerror("Input Error", f"Max cylinder: {max_result}")
            return
        
        valid_queue, queue_result = self.validate_input(self.disk_queue.get(), "list")
        if not valid_queue:
            messagebox.showerror("Input Error", f"Request queue: {queue_result}")
            return
        
        # Check if all requests are within range
        if any(req > max_result for req in queue_result):
            messagebox.showerror("Input Error", "All requests must be less than or equal to max cylinder")
            return
        
        # Get selected algorithm
        algorithm = self.disk_algo.get()
        
        # Run the selected algorithm
        if algorithm == "SSTF":
            order, total_distance = self.sstf(head_result, queue_result)
        elif algorithm == "SCAN":
            order, total_distance = self.scan(head_result, queue_result, max_result)
        elif algorithm == "C-SCAN":
            order, total_distance = self.cscan(head_result, queue_result, max_result)
        elif algorithm == "LOOK":
            order, total_distance = self.look(head_result, queue_result)
        elif algorithm == "C-LOOK":
            order, total_distance = self.clook(head_result, queue_result)
        
        # Display results
        self.display_disk_results(head_result, order, total_distance)
    
    def reset_vm(self):
        self.vm_frames.delete(0, tk.END)
        self.vm_ref_string.delete(0, tk.END)
        for widget in self.vm_canvas_frame.winfo_children():
            widget.destroy()
    
    def reset_disk(self):
        self.disk_head.delete(0, tk.END)
        self.disk_max.delete(0, tk.END)
        self.disk_queue.delete(0, tk.END)
        for widget in self.disk_canvas_frame.winfo_children():
            widget.destroy()
    
    # Virtual Memory Algorithms
    def fifo(self, reference_string, num_frames):
        frames = [-1] * num_frames  # Initialize frames with -1 (empty)
        page_faults = 0
        frames_state = []  # To store the state of frames after each reference
        
        for i,page in enumerate(reference_string):
            # Check if page is already in a frame
            if page in frames:
                # Page hit, just record current state
                frames_state.append(frames.copy())
                continue
            
            # Page fault
            page_faults += 1
            
            # Place the page in the correct frame for FIFO
            # (page_faults - 1) ensures 0-indexed access for the frames array
            frames[(page_faults - 1) % num_frames] = page
            frames_state.append(frames.copy())
        
        return page_faults, frames_state
    
    def lru(self, reference_string, num_frames):
        frames = [-1] * num_frames  # Initialize frames with -1 (empty)
        page_faults = 0
        frames_state = []  # To store the state of frames after each reference
        last_used = {}  # To track when each page was last used
        
        for i, page in enumerate(reference_string):
            # Check if page is already in a frame
            if page in frames:
                # Page hit, update last used
                last_used[page] = i
                frames_state.append(frames.copy())
                continue
            
            # Page fault
            page_faults += 1
            
            # If there's an empty frame
            if -1 in frames:
                idx = frames.index(-1)
                frames[idx] = page
                last_used[page] = i
            else:
                # Find least recently used page
                lru_page = min(last_used.items(), key=lambda x: x[1] if x[0] in frames else float('inf'))[0]
                idx = frames.index(lru_page)
                del last_used[frames[idx]]
                frames[idx] = page
                last_used[page] = i
            
            frames_state.append(frames.copy())
        
        return page_faults, frames_state
    
    def optimal(self, reference_string, num_frames):
        frames = [-1] * num_frames  # Initialize frames with -1 (empty)
        page_faults = 0
        frames_state = []  # To store the state of frames after each reference
        
        for i, page in enumerate(reference_string):
            # Check if page is already in a frame
            if page in frames:
                # Page hit, just record current state
                frames_state.append(frames.copy())
                continue
            
            # Page fault
            page_faults += 1
            
            # If there's an empty frame
            if -1 in frames:
                idx = frames.index(-1)
                frames[idx] = page
            else:
                # Find the page that will not be used for the longest time
                next_use = {}
                for f in frames:
                    try:
                        next_use[f] = reference_string[i+1:].index(f) + i + 1
                    except ValueError:
                        next_use[f] = float('inf')  # Page not used again
                
                # Replace the page that will not be used for the longest time
                victim = max(next_use.items(), key=lambda x: x[1])[0]
                idx = frames.index(victim)
                frames[idx] = page
            
            frames_state.append(frames.copy())
        
        return page_faults, frames_state
    
    def second_chance(self, reference_string, num_frames):
        frames = [-1] * num_frames  # Initialize frames with -1 (empty)
        reference_bits = [0] * num_frames  # Reference bits for each frame
        page_faults = 0
        frames_state = []  # To store the state of frames after each reference
        pointer = 0  # Circular pointer for FIFO replacement
        
        for i, page in enumerate(reference_string):
            # Check if page is already in a frame
            if page in frames:
                # Page hit, set reference bit to 1
                idx = frames.index(page)
                reference_bits[idx] = 1
                frames_state.append((frames.copy(), reference_bits.copy()))
                continue
            
            # Page fault
            page_faults += 1
            
            # If there's an empty frame
            if -1 in frames:
                idx = frames.index(-1)
                frames[idx] = page
                reference_bits[idx] = 0
            else:
                # Find a victim using second chance algorithm
                while True:
                    if reference_bits[pointer] == 0:
                        # Replace this page
                        frames[pointer] = page
                        reference_bits[pointer] = 0
                        pointer = (pointer + 1) % num_frames
                        break
                    else:
                        # Give second chance
                        reference_bits[pointer] = 0
                        pointer = (pointer + 1) % num_frames
            
            frames_state.append((frames.copy(), reference_bits.copy()))
        
        return page_faults, frames_state
    
    # Disk Scheduling Algorithms
    def sstf(self, head, requests):
        current = head
        remaining = requests.copy()
        order = [current]
        total_distance = 0
        
        while remaining:
            # Find the closest request
            closest = min(remaining, key=lambda x: abs(x - current))
            distance = abs(closest - current)
            total_distance += distance
            current = closest
            order.append(current)
            remaining.remove(closest)
        
        return order, total_distance
    
    def scan(self, head, requests, max_cylinder):
        # Sort requests
        requests = sorted(requests)
        order = [head]
        total_distance = 0
        
        # Find requests greater than head
        greater = [r for r in requests if r >= head]
        # Find requests less than head
        lesser = [r for r in requests if r < head]
        
        # SCAN goes to the end first, then reverses
        if greater:
            # Go to the end
            for r in greater:
                distance = abs(r - order[-1])
                total_distance += distance
                order.append(r)
            
            # Go to the max cylinder if not already there
            if order[-1] < max_cylinder:
                distance = max_cylinder - order[-1]
                total_distance += distance
                order.append(max_cylinder)
        
        # Then go back to the beginning
        for r in sorted(lesser, reverse=True):
            distance = abs(r - order[-1])
            total_distance += distance
            order.append(r)
        
        return order, total_distance
    
    def cscan(self, head, requests, max_cylinder):
        # Sort requests
        requests = sorted(requests)
        order = [head]
        total_distance = 0
        
        # Find requests greater than head
        greater = [r for r in requests if r >= head]
        # Find requests less than head
        lesser = [r for r in requests if r < head]
        
        # C-SCAN goes to the end, then jumps to the beginning
        if greater:
            # Go to the end
            for r in greater:
                distance = abs(r - order[-1])
                total_distance += distance
                order.append(r)
            
            # Go to the max cylinder if not already there
            if order[-1] < max_cylinder:
                distance = max_cylinder - order[-1]
                total_distance += distance
                order.append(max_cylinder)
        
        # Jump to the beginning (0)
        # Note: The jump distance is not counted in C-SCAN
        if lesser:
            order.append(0)
            
            # Then go from beginning to the last request
            for r in lesser:
                distance = abs(r - order[-1])
                total_distance += distance
                order.append(r)
        
        return order, total_distance
    
    def look(self, head, requests):
        # Sort requests
        requests = sorted(requests)
        order = [head]
        total_distance = 0
        
        # Find requests greater than head
        greater = [r for r in requests if r >= head]
        # Find requests less than head
        lesser = [r for r in requests if r < head]
        
        # LOOK goes to the largest request first, then reverses
        if greater:
            # Go to the largest request
            for r in greater:
                distance = abs(r - order[-1])
                total_distance += distance
                order.append(r)
        
        # Then go back to the smallest request
        for r in sorted(lesser, reverse=True):
            distance = abs(r - order[-1])
            total_distance += distance
            order.append(r)
        
        return order, total_distance
    
    def clook(self, head, requests):
        # Sort requests
        requests = sorted(requests)
        order = [head]
        total_distance = 0
        
        # Find requests greater than head
        greater = [r for r in requests if r >= head]
        # Find requests less than head
        lesser = [r for r in requests if r < head]
        
        # C-LOOK goes to the largest request, then jumps to the smallest
        if greater:
            # Go to the largest request
            for r in greater:
                distance = abs(r - order[-1])
                total_distance += distance
                order.append(r)
        
        # Jump to the smallest request
        # Note: The jump distance is not counted in C-LOOK
        if lesser:
            order.append(lesser[0])
            total_distance += abs(lesser[0] - order[-2])
            
            # Then go from smallest to largest
            for r in lesser[1:]:
                distance = abs(r - order[-1])
                total_distance += distance
                order.append(r)
        
        return order, total_distance
    
    def display_vm_results(self, reference_string, frames_state, page_faults):
        # Create figure for visualization
        fig, ax = plt.figure(figsize=(10, 6)), plt.subplot(111)
        
        # Check if we're using Second Chance algorithm
        is_second_chance = isinstance(frames_state[0], tuple)
        
        # Number of frames
        num_frames = len(frames_state[0]) if not is_second_chance else len(frames_state[0][0])
        
        # Create a grid for visualization
        for i, ref in enumerate(reference_string):
            # Draw reference value
            ax.text(i, -1, str(ref), ha='center', va='center', fontsize=10)
            
            # Draw frame states
            if not is_second_chance:
                frame_state = frames_state[i]
                for j, frame in enumerate(frame_state):
                    
                    if frame != -1:
                        # Check if this is a page fault
                        if i==0:
                            is_fault = True
                        else:
                            is_fault = i > 0 and frame not in frames_state[i-1]

                        color = 'lightcoral' if is_fault else 'lightblue'
                        ax.add_patch(plt.Rectangle((i-0.4, j-0.4), 0.8, 0.8, fill=True, color=color))
                        ax.text(i, j, str(frame), ha='center', va='center', fontsize=10)
            else:
                frame_state, ref_bits = frames_state[i]
                for j, (frame, ref_bit) in enumerate(zip(frame_state, ref_bits)):
                    if frame != -1:
                        # Check if this is a page fault
                        is_fault = i > 0 and frame not in frames_state[i-1][0]
                        color = 'lightcoral' if is_fault else 'lightblue'
                        ax.add_patch(plt.Rectangle((i-0.4, j-0.4), 0.8, 0.8, fill=True, color=color))
                        ax.text(i, j, f"{frame} ({ref_bit})", ha='center', va='center', fontsize=8)
        
        # Set axis limits and labels
        ax.set_xlim(-1, len(reference_string))
        ax.set_ylim(-2, num_frames)
        ax.set_xticks(range(len(reference_string)))
        ax.set_yticks(range(-1, num_frames))
        ax.set_yticklabels(['Reference'] + [f'Frame {i}' for i in range(num_frames)])
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Set title
        ax.set_title(f"Page Replacement Visualization - Page Faults: {page_faults}")
        
        # Create canvas
        canvas = FigureCanvasTkAgg(fig, master=self.vm_canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def display_disk_results(self, head, order, total_distance):
        # Create figure for visualization
        fig, ax = plt.figure(figsize=(10, 6)), plt.subplot(111)
        
        # Plot the seek sequence
        ax.plot(range(len(order)), order, 'o-', markersize=8)
        
        # Annotate each point
        for i, pos in enumerate(order):
            ax.annotate(str(pos), (i, pos), textcoords="offset points", 
                        xytext=(0, 10), ha='center')
        
        # Set axis labels and title
        ax.set_xlabel('Seek Sequence')
        ax.set_ylabel('Cylinder Position')
        ax.set_title(f"Disk Scheduling - Total Seek Distance: {total_distance}")
        
        # Set y-axis limits with some padding
        max_pos = max(order)
        min_pos = min(order)
        ax.set_ylim(min_pos - 10, max_pos + 10)
        
        # Create canvas
        canvas = FigureCanvasTkAgg(fig, master=self.disk_canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        
        # Display text results
        result_text = tk.Text(self.disk_canvas_frame, height=5)
        result_text.pack(fill="x", padx=5, pady=5)
        result_text.insert(tk.END, f"Initial Head Position: {head}\n")
        result_text.insert(tk.END, f"Seek Sequence: {' -> '.join(map(str, order))}\n")
        result_text.insert(tk.END, f"Total Seek Distance: {total_distance}")
        result_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = OSAlgorithmsApp(root)
    root.mainloop()