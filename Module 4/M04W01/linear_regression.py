import numpy as np
import random
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self, lr=0.01, epochs=10):
        self.w = None
        self.b = None 
        self.lr = lr
        self.epochs = epochs
        
    def initialize_params(self):
        self.w = random.gauss(mu=0.0, sigma=0.01)
        self.b = random.gauss(mu=0.0, sigma=0.01)
        
    def y_predict(self, x):
        return self.w * x + self.b
    
    def loss(self, y_predict, y):
        return np.mean((y_predict - y) ** 2)

    def compute_gradient(self, x, y, y_hat):
        dl_dw = np.mean(2 * x * (y_hat - y))
        dl_db = np.mean(2 * (y_hat - y))
        return dl_dw, dl_db
    
    def update_w(self, dw):
        self.w = self.w - self.lr * dw
        
    def update_b(self, db):
        self.b = self.b - self.lr * db
        
    def fit(self, x, y):
        losses = []
        self.initialize_params()
        
        for i in range(self.epochs):
            y_hat = self.y_predict(x)
            current_loss = self.loss(y_hat, y)
            losses.append(current_loss)
            dw, db = self.compute_gradient(x, y, y_hat)
            self.update_w(dw)
            self.update_b(db)
                
        return losses

    def plot_loss(self, losses):

        plt.figure(figsize=(10, 6))
        plt.plot(range(len(losses)), losses, 'b-', linewidth=2, label='Training Loss')
        plt.title('Loss Function over Epochs')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.grid(True)
        plt.legend()
        plt.show()
        
    def plot_regression_line(self, x, y):
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, color='blue', label='Data Points')
        x_line = np.array([min(x), max(x)])
        y_line = self.y_predict(x_line)
        plt.plot(x_line, y_line, 'r-', linewidth=2, label=f'Regression Line (w={self.w:.2f}, b={self.b:.2f})')
        
        plt.title('Linear Regression Fit')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.legend()
        plt.show()
if __name__ == '__main__':

    np.random.seed(42)
    X = np.random.rand(100, 1) * 10    
    y = 4 * X + 3 + np.random.randn(100, 1) * 0.5
    model = LinearRegression(lr=0.001, epochs=200)
    losses = model.fit(X, y)
    model.plot_loss(losses)
    model.plot_regression_line(X, y)
    
    print(f"\nThông số tối ưu:")
    print(f"w: {model.w:.4f}")
    print(f"b: {model.b:.4f}")