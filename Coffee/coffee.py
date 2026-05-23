import tkinter as tk
from tkinter import messagebox

class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        return f"Added {coffee.name} to your order."

    def total(self):
        return sum(item.price for item in self.items)
    
    def get_order_summary(self):
        if not self.items:
            return "No items in order."
        
        summary = "Your Order:\n"
        for i, item in enumerate(self.items, 1):
            summary += f"{i}. {item.name} - ${item.price:.2f}\n"
        summary += f"\nTotal: ${self.total():.2f}"
        return summary

    def checkout(self):
        if not self.items:
            messagebox.showwarning("Empty Cart", "Your cart is empty.")
            return False
        
        confirm = messagebox.askyesno("Checkout", f"{self.get_order_summary()}\n\nProceed to checkout?")
        if confirm:
            messagebox.showinfo("Success", "Order confirmed!! Thank You!")
            self.items.clear()
            return True
        else:
            messagebox.showinfo("Cancelled", "Checkout cancelled.")
            return False

# --- GUI Window Setup ---
def main():
    menu = [
        Coffee("Espresso", 2.5),
        Coffee("Latte", 3.5),
        Coffee("Cappuccino", 3.0),
        Coffee("Americano", 2.0)
    ]
    
    order = Order()

    # Main Window
    root = tk.Tk()
    root.title("Rose's Coffee Shop")
    root.geometry("450x570")
    
    # Color Palette Application
    BG_CREAM = "#F0DAAE"
    TEXT_ESPRESSO = "#724816"
    BTN_TERRACOTTA = "#925F49"
    BTN_HOVER_CARAMEL = "#A8783E"
    BTN_CHECKOUT_SAGE = "#9BA36A"

    root.configure(bg=BG_CREAM)

    # Title Banner
    title_label = tk.Label(root, text="-- Welcome to Rose's --", font=("Arial", 18, "bold"), bg=BG_CREAM, fg=TEXT_ESPRESSO)
    title_label.pack(pady=15)

    menu_label = tk.Label(root, text="--- Coffee Menu ---", font=("Arial", 12, "italic"), bg=BG_CREAM, fg=TEXT_ESPRESSO)
    menu_label.pack(pady=5)

    # Function to refresh the live receipt textbox
    def update_receipt_display():
        receipt_text.config(state="normal") # Temporarily enable to edit text
        receipt_text.delete("1.0", tk.END)
        receipt_text.insert(tk.END, order.get_order_summary())
        receipt_text.config(state="disabled") # Set back to read-only

    # Helper functions
    def handle_add_coffee(coffee_obj):
        status_msg = order.add_item(coffee_obj)
        messagebox.showinfo("Added", status_msg)
        update_receipt_display()

    def handle_checkout():
        if order.checkout():
            update_receipt_display()

    # Create Clickable Buttons for each Menu item
    for coffee in menu:
        btn = tk.Button(
            root, 
            text=f"Order {coffee.name} - ${coffee.price:.2f}", 
            font=("Arial", 11, "bold"),
            width=25,
            bg=BTN_TERRACOTTA,
            fg="white",
            activebackground=BTN_HOVER_CARAMEL,
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda c=coffee: handle_add_coffee(c)
        )
        btn.pack(pady=5, ipady=3)

    # Live Receipt Display Frame
    receipt_title = tk.Label(root, text="Live Receipt:", font=("Arial", 11, "bold"), bg=BG_CREAM, fg=TEXT_ESPRESSO)
    receipt_title.pack(pady=(20, 2))
    
    # Styled text box for summary
    receipt_text = tk.Text(root, height=7, width=40, font=("Arial", 10), bg="#FFFFFF", fg=TEXT_ESPRESSO, relief="solid", bd=1)
    receipt_text.pack(pady=5)
    update_receipt_display()

    # Action Buttons at the bottom
    checkout_btn = tk.Button(
        root, 
        text="🛒 Checkout", 
        font=("Arial", 12, "bold"), 
        bg=BTN_CHECKOUT_SAGE, 
        fg="white", 
        width=15, 
        relief="flat",
        bd=0,
        cursor="hand2",
        activebackground=TEXT_ESPRESSO,
        activeforeground="white",
        command=handle_checkout
    )
    checkout_btn.pack(pady=12, ipady=4)

    exit_btn = tk.Button(
        root, 
        text="Exit App", 
        font=("Arial", 9), 
        bg=BG_CREAM, 
        fg=TEXT_ESPRESSO, 
        relief="flat",
        bd=0,
        cursor="hand2",
        activebackground=BG_CREAM,
        activeforeground=BTN_TERRACOTTA,
        command=root.destroy
    )
    exit_btn.pack(pady=5)

    root.update_idletasks()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_x = int((screen_width / 2) - (window_width / 2))
    window_y = int((screen_height / 2) - (window_height / 2))

    root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
    root.mainloop()

if __name__ == "__main__":
    main() 