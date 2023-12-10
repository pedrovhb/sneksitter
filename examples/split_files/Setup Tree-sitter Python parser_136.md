### Inspirational Libraries

1. **Pandas**: Pandas DataFrame API often uses `__getitem__` for slicing and filtering data based on conditions.
    ```python
    # Simple example
    df['column_name']

    # Advanced example with predicates
    df[df['age'] > 21]
    ```

2. **SQLAlchemy**: Uses method chaining and function calls to build complex queries.
    ```python
    # Simple example
    session.query(User).filter_by(name='John')

    # Advanced example
    session.query(User).filter(or_(User.name == 'John', User.id > 5))
    ```

3. **Django ORM**: Uses double-underscore notation for related fields and complex queries.
    ```python
    # Simple example
    Entry.objects.filter(pub_date__year=2006)

    # Advanced example
    Entry.objects.filter(authors__name='John', authors__age__gt=30)
    ```

4. **Scikit-learn Pipeline**: Uses a step-based approach to chain multiple operations.
    ```python
    # Simple example
    pipe = Pipeline(steps=[('scaler', StandardScaler())])

    # Advanced example
    pipe = Pipeline(steps=[('scaler', StandardScaler()), ('classifier', RandomForestClassifier())])
    ```

5. **PySpark SQL**: Uses SQL-like string-based DSL for queries.
    ```python
    # Simple example
    df.select("name", "age")

    # Advanced example
    df.filter(df.age > 21).groupBy("age").count()
    ```

