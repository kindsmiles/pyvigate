import inspect
import os
import importlib.util
import sys

# Define your package directory and documentation output directory here
PACKAGE_DIR = 'pyvigate'
DOCS_DIR = 'docs'

# Ensure the package directory is in the Python path
PACKAGE_PARENT_DIR = os.path.dirname(os.path.abspath(PACKAGE_DIR))
if PACKAGE_PARENT_DIR not in sys.path:
    sys.path.insert(0, PACKAGE_PARENT_DIR)

def get_signature(obj):
    """
    Generate the signature for a function, method, or class constructor.
    """
    try:
        return str(inspect.signature(obj))
    except ValueError:
        return '()'

def get_docstring(obj):
    """
    Extract the docstring of a function, class, or module.
    """
    return inspect.getdoc(obj) or ''

def write_markdown_file(file_path, content):
    """
    Write the given content to a markdown file, ensuring the directory exists.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(content)

def format_signature(signature):
    """
    Format the signature for Markdown display.
    """
    return '`' + signature + '`'

def format_docstring(docstring):
    """
    Format the docstring with proper indentation for Markdown display.
    """
    if not docstring:
        return 'No description provided.\n'
    return '\n'.join(['    ' + line for line in docstring.split('\n')]) + '\n'

def generate_docs_for_module(module_path, docs_path, base_package_path):
    """
    Enhanced documentation generation with improved formatting for readability.
    """
    module_name = os.path.splitext(os.path.basename(module_path))[0]
    full_module_name = module_path.replace(base_package_path, '').replace(os.sep, '.').strip('.').lstrip('.')
    doc_content = f"# Module `{module_name}`\n\n"
    spec = importlib.util.spec_from_file_location(full_module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except ImportError as e:
        print(f"Error importing module {module_name}: {e}")
        return

    for name, obj in inspect.getmembers(module, lambda member: inspect.isclass(member) or inspect.isfunction(member)):
        if obj.__module__ == full_module_name:
            if inspect.isclass(obj):
                doc_content += f"## Class `{name}`\n\n"
                class_docstring = get_docstring(obj)
                if class_docstring:
                    doc_content += f"{format_docstring(class_docstring)}\n"
                doc_content += "### Attributes:\n\n"
                attributes = inspect.getmembers(obj, lambda a: not(inspect.isroutine(a)))
                for attr_name, attr_value in attributes:
                    if not attr_name.startswith('_'):
                        doc_content += f"- **{attr_name}**: {attr_value}\n"
                doc_content += "\n### Methods:\n\n"
                methods = inspect.getmembers(obj, inspect.isfunction)
                for method_name, method in methods:
                    method_sig = get_signature(method)
                    method_doc = get_docstring(method)
                    doc_content += f"- **{method_name}**{format_signature(method_sig)}\n\n{format_docstring(method_doc)}\n"
            elif inspect.isfunction(obj):
                func_signature = get_signature(obj)
                func_docstring = get_docstring(obj)
                doc_content += f"## Function `{name}`{format_signature(func_signature)}\n\n{format_docstring(func_docstring)}\n"

    relative_module_path = os.path.relpath(module_path, base_package_path)
    doc_relative_path = relative_module_path.replace('.py', '.md').replace(os.sep, '/')
    doc_file_path = os.path.join(docs_path, doc_relative_path)
    write_markdown_file(doc_file_path, doc_content)

def generate_project_docs(package_dir, docs_dir):
    """
    Generate documentation for all Python files in the given package directory, maintaining the folder hierarchy.
    """
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)
    for root, dirs, files in os.walk(package_dir):
        for file in files:
            if file.endswith('.py'):
                module_path = os.path.join(root, file)
                generate_docs_for_module(module_path, docs_dir, package_dir)

if __name__ == '__main__':
    generate_project_docs(PACKAGE_DIR, DOCS_DIR)
