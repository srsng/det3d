# init

```bash
git submodule update --init --recursive
uv venv
uv sync
```

## RUN

train votenet on mini:

```bash
uv run python tools/train.py configs/votenet_mini_sunrgbd.py
```

fine-tune votenet on mini:

```bash
uv run python tools/train.py configs/votenet_mini_sunrgbd_finetune.py
```
