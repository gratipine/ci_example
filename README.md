# ci_example
Example of how a CI pipeline works in github


## Environment set up 
```bash
python -m venv .venv 
pip install -r requirements.txt
.venv\Scripts\activate
```

## How to render a notebook
You need to have installed Tex and pandoc, but it is easy enough to follow the error messages.
```bash
jupyter nbconvert --to pdf notebooks\rendering_example.ipynb --output output.pdf --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags remove-cell --TagRemovePreprocessor.remove_input_tags hide-input
```