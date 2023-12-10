---
file: /home/pedro/Documents/chatgpt_export/Markdown/Sympy and SciPy Features.md
heading_stack: <root> -> 978f4ae8-446b-44eb-a6e1-e6e14d2d360f -> System -> 29d455d7-aacc-4725-b3ef-918114effb01 -> System -> aaa2e7d9-3bdd-4fad-911a-31b12dc2a648 -> User -> 8538284c-0352-43f1-8abc-46b21e1b06e8 -> Assistant -> SymPy -> SciPy -> aaa207bb-2094-4403-8ec6-18f904a315cd -> User -> 729fb28a-7915-4de4-b6fc-86073b9c59ea -> Assistant -> 8ba7491e-258c-4b35-adb8-30c8f6253da5 -> Tool -> 34a917f5-16d6-4338-bd6c-6494cea2cf50 -> Assistant -> SymPy: Symbolic Computing -> e221c1b0-a165-471d-8c39-314344d99fb9 -> Assistant -> 575a9e32-8e21-45b5-a224-0aae541e3df7 -> Tool -> 8fa51d1f-ce37-4660-b6e4-2a6f71562970 -> Assistant -> 63c42cc1-0fa2-479e-aeb0-f63bf89488fb -> Assistant -> f359e1ab-aeba-49b4-aceb-57b2aebb5ebc -> Tool -> 3f3de047-a51c-4010-ad4c-820419d23279 -> Assistant -> 2be30db6-989f-4daf-b8dd-3b3098b5e329 -> Assistant -> 6374a92e-ccbd-46e2-9f1b-d9774b21d029 -> Tool -> 2c8f8f7d-6dd2-4d5c-a440-7aacd107b75e -> Assistant -> 5b1d05d6-728a-435f-9a49-4bad487bb77b -> Assistant -> 744424e2-f97a-4c44-8a89-fed99c0341f1 -> Tool -> 8c7b629a-c632-4706-afdf-814b17766ca1 -> Assistant -> c62752a0-f201-4ee4-96ee-0435da370067 -> Assistant -> 6fbf4829-b77e-4300-aa99-f68a48b19fb7 -> Tool -> 1d81d149-213a-4f27-857e-8d6bec21bcef -> Assistant -> aaa203e3-859d-4bd5-9df9-adb78b399b4b -> User -> 7ddc7f98-9575-4d28-b101-27f817b05527 -> Assistant -> SymPy: Advanced Features -> b267a54d-9f69-42fc-90c0-2ebc5839474f -> Assistant -> ce6a6003-0b87-47bf-82fc-c4717529ecdf -> Tool -> 40577064-962e-4ae7-93b3-f221b6a581f8 -> Assistant -> d415a7f3-4f92-4e5d-a170-15079c97f642 -> Assistant -> c12f27d2-11a4-4bb4-9240-dfeca4dece5c -> Tool -> e4f3c962-9d1c-4f50-bdc4-c3e005108fc4 -> Assistant -> 6e9f2fa6-6078-4627-a045-dc0c6a2a58e9 -> Assistant -> 3e25bced-b06f-4224-a09c-44a7adbe885d -> Tool -> 6f9cb60a-92e3-4ae9-9ff9-a97cf787e77e -> Assistant -> aaa2f9f1-add4-4e07-882e-c27258fca6a4 -> User -> c60517be-a67e-4f4d-b517-fde601274b3c -> Assistant -> SciPy: Advanced Features -> 01e74733-c2da-4dae-b23e-edbe3c46d619 -> Assistant -> 87a16e2b-fb8f-413e-9c96-7ffa1da5e422 -> Tool -> 133b267c-a5a2-4241-99e5-a9d8b41f7324 -> Assistant -> 50a06526-4d88-4690-9182-9f638815ba38 -> Assistant -> 5b31b798-d6c9-4e9d-81a3-7c5ab75f8459 -> Tool -> 748f73fa-a21c-4258-925e-098e6cf2388c -> Assistant -> 259f2564-903a-46eb-a8c2-1c61737ac402 -> Assistant -> cf4c7b14-bdd0-489c-8564-6f90da53c51a -> Tool -> 4eb0ca4d-4eb9-4539-868c-5023caca8627 -> Assistant -> 777a44e3-83bf-4084-8d6d-4066d57d41a8 -> Assistant -> 37e7b5d2-9627-4c5a-afb5-b536458e6d77 -> Tool -> 46bf0851-0ce5-48fc-9243-52a5b84eb8c3 -> Assistant -> 56e05878-e3e4-4585-b6ab-108a73a472fe -> Assistant -> 00e5b15e-f382-4c48-a0e7-a5933398de20 -> Tool -> 7fae61c3-a488-4409-bb39-730a9fa327be -> Assistant -> b3df32dc-571e-4576-9d11-a1a53d8ba0ad -> Assistant
---
# Assistant

```python
# Define the ODE dy/dt = -2y
def dydt(y, t):
    return -2 * y

# Time grid for integration
t_grid = np.linspace(0, 5, 100)

# Initial condition y(0) = 1
y0 = 1

# Solve the ODE using odeint
y_solution = odeint(dydt, y0, t_grid)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(t_grid, y_solution, label='Numerical Solution')
plt.title('Numerical Integration: Solving $\\frac{dy}{dt} = -2y$')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.show()
```

[child ⬇️](#f4711cdc-a7ec-45bd-a4c6-11c48880d0e3)

---

(main branch ⎇)
###### f4711cdc-a7ec-45bd-a4c6-11c48880d0e3
[parent ⬆️](#b3df32dc-571e-4576-9d11-a1a53d8ba0ad)
