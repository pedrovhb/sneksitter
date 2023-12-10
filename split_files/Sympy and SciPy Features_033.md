---
file: /home/pedro/Documents/chatgpt_export/Markdown/Sympy and SciPy Features.md
heading_stack: <root> -> 978f4ae8-446b-44eb-a6e1-e6e14d2d360f -> System -> 29d455d7-aacc-4725-b3ef-918114effb01 -> System -> aaa2e7d9-3bdd-4fad-911a-31b12dc2a648 -> User -> 8538284c-0352-43f1-8abc-46b21e1b06e8 -> Assistant -> SymPy -> SciPy -> aaa207bb-2094-4403-8ec6-18f904a315cd -> User -> 729fb28a-7915-4de4-b6fc-86073b9c59ea -> Assistant -> 8ba7491e-258c-4b35-adb8-30c8f6253da5 -> Tool -> 34a917f5-16d6-4338-bd6c-6494cea2cf50 -> Assistant -> SymPy: Symbolic Computing -> e221c1b0-a165-471d-8c39-314344d99fb9 -> Assistant -> 575a9e32-8e21-45b5-a224-0aae541e3df7 -> Tool -> 8fa51d1f-ce37-4660-b6e4-2a6f71562970 -> Assistant -> 63c42cc1-0fa2-479e-aeb0-f63bf89488fb -> Assistant -> f359e1ab-aeba-49b4-aceb-57b2aebb5ebc -> Tool -> 3f3de047-a51c-4010-ad4c-820419d23279 -> Assistant -> 2be30db6-989f-4daf-b8dd-3b3098b5e329 -> Assistant
---
# Assistant

```python
# Define x values for plotting
x_vals = np.linspace(-10, 10, 400)
y_vals = x_vals**2
y_prime_vals = 2 * x_vals
y_integral_vals = (x_vals**3) / 3

# Create the plots
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(x_vals, y_vals, label='$f(x) = x^2$')
plt.title('Function $f(x) = x^2$')
plt.xlabel('x')
plt.ylabel('$f(x)$')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(x_vals, y_prime_vals, label="$f'(x) = 2x$", color='orange')
plt.title("Derivative $f'(x) = 2x$")
plt.xlabel('x')
plt.ylabel("$f'(x)$")
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(x_vals, y_integral_vals, label='$\int f(x) dx = x^3/3$', color='green')
plt.title('Integral $\int f(x) dx = x^3/3$')
plt.xlabel('x')
plt.ylabel('$\int f(x) dx$')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
```

[child ⬇️](#6374a92e-ccbd-46e2-9f1b-d9774b21d029)

---

(main branch ⎇)
###### 6374a92e-ccbd-46e2-9f1b-d9774b21d029
[parent ⬆️](#2be30db6-989f-4daf-b8dd-3b3098b5e329)
