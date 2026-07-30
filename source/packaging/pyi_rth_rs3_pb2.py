# PyInstaller runtime hook: install RS3 protobuf bare-import aliases
# before any application code runs.
import importlib
import importlib.abc
import importlib.machinery
import importlib.util
import sys


class _Rs3Pb2AliasFinder(importlib.abc.MetaPathFinder):
    def __init__(self):
        self._busy = set()

    def find_spec(self, fullname, path=None, target=None):
        if "." in fullname:
            return None
        if not (fullname.endswith("_pb2") or fullname.endswith("_pb2_grpc")):
            return None

        real_name = f"rs3.generatedFiles.{fullname}"
        if fullname in self._busy or real_name in self._busy:
            return None

        existing = sys.modules.get(real_name)
        if existing is not None:
            sys.modules[fullname] = existing

            class _ExistingLoader(importlib.abc.Loader):
                def create_module(self, spec):
                    return existing

                def exec_module(self, module):
                    return None

            return importlib.util.spec_from_loader(
                fullname,
                _ExistingLoader(),
                origin=getattr(existing, "__file__", None),
            )

        self._busy.add(real_name)
        try:
            real_spec = importlib.util.find_spec(real_name)
        finally:
            self._busy.discard(real_name)

        if real_spec is None or real_spec.loader is None:
            return None

        class _AliasLoader(importlib.abc.Loader):
            def create_module(self, spec):
                module = importlib.import_module(real_name)
                sys.modules[spec.name] = module
                return module

            def exec_module(self, module):
                return None

        return importlib.util.spec_from_loader(
            fullname,
            _AliasLoader(),
            origin=getattr(real_spec, "origin", None),
        )


if not any(type(f).__name__ == "_Rs3Pb2AliasFinder" for f in sys.meta_path):
    sys.meta_path.insert(0, _Rs3Pb2AliasFinder())
