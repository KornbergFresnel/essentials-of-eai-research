# Essentials of Embodied AI Research

This repository hosts a bilingual Read the Docs style learning resource for junior PhD students studying reinforcement learning, world models, embodied AI, robot learning practice, and distributed reinforcement learning systems.

## Documentation Structure

- `docs/source/index.md`: language selection page.
- `docs/source/zh_CN/`: Chinese documentation tree.
- `docs/source/en/`: English documentation tree.
- `docs/source/conf.py`: Sphinx configuration.

The Chinese and English trees should keep matching directory structures and page slugs.

## Local Build

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

Build the HTML documentation:

```bash
make -C docs html
```

Open `docs/build/html/index.html` in a browser.

## Learning Path

Start with Orientation and RL Basics, then move through World Models, Embodied AI Foundations, Robot Learning Practice, Distributed RL Systems, and Research Practice.

The RL Basics section links to [OpenAI Spinning Up](https://spinningup.openai.com/en/latest/) as an external reference for classical deep RL concepts and implementations.

## License

This project is released under the MIT License.
