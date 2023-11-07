import time

t = time.perf_counter()
import sneksitter._node_codegen.python_node_types_mod

t_import_types = time.perf_counter()
import sneksitter._node_codegen.python_base_visitor_mod

t_import_visitor = time.perf_counter()
import libcst as cst

t_import_libcst = time.perf_counter()

import sneksitter._node_codegen.python_node_types

t_import_types2 = time.perf_counter()

print(f"import types: {t_import_types - t:.4f}")
print(f"import visitor: {t_import_visitor - t_import_types:.4f}")
print(f"import libcst: {t_import_libcst - t_import_visitor:.4f}")
print(f"import types2: {t_import_types2 - t_import_libcst:.4f}")
